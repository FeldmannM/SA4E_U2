package com.example;

import org.apache.camel.CamelContext;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.impl.DefaultCamelContext;

import java.util.ArrayList;
import java.util.List;

public class XmasWishesRoute extends RouteBuilder {

    public static void main(String[] args) throws Exception {
        CamelContext context = new DefaultCamelContext();
        context.addRoutes(new XmasWishesRoute());
        context.start();

        // Halte das Programm am Laufen, damit Camel die Dateien verarbeiten kann
        while (context.isStarted()) {
            Thread.sleep(100);
        }
    }

    @Override
    public void configure() throws Exception {
        from("file:src/main/resources/scanned/files?noop=true") // Ordner, in dem die eingescannten Dateien liegen
            .routeId("XmasWishesRoute")
            .log("Datei empfangen: ${header.CamelFileName}")
            .process(exchange -> {
                String content = exchange.getIn().getBody(String.class);
                log.info("Text empfangen: " + content);
                List<Wish> wishes = new ArrayList<>();
                String[] lines = content.split("\\r?\\n");
                for (String line : lines) {
                    String[] parts = line.split(":");
                    if (parts.length == 2) {
                        Wish wish = new Wish();
                        wish.setName(parts[0].trim());
                        wish.setWish(parts[1].trim());
                        wishes.add(wish);
                    }
                }
                exchange.getIn().setBody(wishes);
                log.info("Wünsche extrahiert: " + wishes.size());
            })
            .split().body() // Jeder Wunsch wird einzeln verarbeitet
            .process(exchange -> {
                Wish wish = exchange.getIn().getBody(Wish.class);
                String namePayload = "{\"name\": \"" + wish.getName() + "\"}";
                String wishPayload = "{\"wish\": \"" + wish.getWish() + "\"}";

                // Speichere Payloads als Properties
                exchange.setProperty("namePayload", namePayload);
                exchange.setProperty("wishPayload", wishPayload);

                log.info("Sende Name an users service: " + namePayload);
                exchange.getIn().setBody(namePayload);
            })
            .setHeader("Content-Type", constant("application/json"))
            .to("http://localhost:8080/users") // URL des API-Gateways für Benutzer
            .log("Name erfolgreich gesendet: ${body}")

            // Sende Wunsch an den API-Gateway
            .process(exchange -> {
                String wishPayload = exchange.getProperty("wishPayload", String.class);
                log.info("Sende Wunsch an wishes service: " + wishPayload);
                exchange.getIn().setBody(wishPayload);
            })
            .setHeader("Content-Type", constant("application/json"))
            .to("http://localhost:8080/wishes") // URL des API-Gateways für Wünsche
            .log("Wunsch erfolgreich gesendet: ${body}")

            // Sende Status "Formuliert" an den API-Gateway
            .process(exchange -> {
                String statusPayload = "{\"status\": \"Formuliert\"}";
                log.info("Sende Status an status service: " + statusPayload);
                exchange.getIn().setBody(statusPayload);
            })
            .setHeader("Content-Type", constant("application/json"))
            .to("http://localhost:8080/status") // URL des API-Gateways für Status
            .log("Status erfolgreich gesendet: ${body}")

            .end()
            .process(exchange -> {
                // Beende das Programm nach dem Senden aller Wünsche
                log.info("Alle Wünsche wurden erfolgreich gesendet.");
                exchange.getContext().stop();
            });
    }

    public static class Wish {
        private String name;
        private String wish;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getWish() {
            return wish;
        }

        public void setWish(String wish) {
            this.wish = wish;
        }
    }
}
