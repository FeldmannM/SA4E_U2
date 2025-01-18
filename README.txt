Software Architectures for Enterprises SA4E
Übungsblatt 2

Um den vollständigen Service starten zu können, sollte Docker auf dem Rechner intsalliert sein.
Alle anderen Abhängigkeiten werden automatisch über die jeweiligen requirements.txt-Dateien gezogen.
Um die gesamte Anwendung zu starten, führen Sie bitte auf ihrer Konsole im Ordner Service den folgenden Befehl aus:
docker-compose up --build
Danach können Sie auf die Anwendungen unter folgenden URLs in ihrem Webbrowser zu greifen:
XmasWishes: 		http://localhost:8080/
Elfen&Rentier-Logistik: http://localhost:8081/
Santas Übersicht: 	http://localhost:8082/
DB mit den Wünschen:	http://localhost:5000/wishes
DB mit den Nutzern:	http://localhost:5001/users
DB mit dem Status:	http://localhost:5002/status

Um einen API-Call-Test auszuführen verwenden Sie bitte den folgenden Befehl im Ordner APICallRate:
python api_call_rate_api.py

Um die Apache Camel Anwendung zu starten können Sie im Ordner PaperWish die Anwendung einmal bei Ihnen mit Gradle builden:
gradle build
Da ich schon eine gebuildete Version mithochgeladen habe, sollte normalerweise die Ausführung reichen:
gradle run
Ich habe Gradle verwendet, damit die Abhängigkeiten für Apache Camel automatisch gezogen werden.


Weitere interessante Befehle z.B. zur Übersicht von Docker sind in den Befehle.txt Dateien.

