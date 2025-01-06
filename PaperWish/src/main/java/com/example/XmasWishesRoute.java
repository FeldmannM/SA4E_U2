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
                exchange.getIn().setBody(wish);
                log.info("Wunsch verarbeitet: " + wish.getWish());
            })
            .marshal().json() // Wunsch in JSON konvertieren
            .setHeader("Content-Type", constant("application/json"))
            .to("http://localhost:8080/wishes") // URL des API-Gateways
            .log("Wunsch erfolgreich gesendet: ${body}")
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
