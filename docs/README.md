# Schiffe-Versenken

Dies ist die komplette Dokumentation der Schiffe-Versenken Anwendung.


## Beschreibung des Spiels

Im Spiel "Schiffe-Versenken" spielen zwei Spieler gegeneinander und versuchen jeweils die Schiffe des Gegners zu 
zerstören.

Zu Beginn wählen die Spieler jeweils aus, wo sie ihre Schiffe auf dem Feld platzieren wollen. Natürlich kann man nicht 
zwei Schiffe übereinander platzieren. Danach wechseln sich die Spieler ab und wählen immer eine Koordinate aus mit dem Ziel, 
die Schiffe des Gegners zu treffen. Der Spieler, welcher als Erstes alle Schiffe des Gegners zerstört, gewinnt das Spiel.


## Starten des Spiels

Um das Spiel mit zwei Spielern zu spielen, müssen beide Spieler ein Command Prompt öffnen. Nun müssen beide Spieler die 
Pfade für das Programm einfügen. Mit dem ersten Pfad lässt sich Python aufrufen und mit dem zweiten Pfad können wir die 
Main des Schiffe-Versenken-Spiels aufrufen.

Als nächstes muss ein Spieler einen beliebigen Spielernamen und eine Portnummer eingeben und dann auf `Enter` drücken um
das Spielfeld für diesen Spieler zu initialisieren. Der zweite Spieler gibt einen anderen Spielernamen und auch eine
andere Portnummer ein. Außerdem muss dieser auch die IP-Adresse des ersten Spielers eingeben und dessen Portnummer.
Falls beide Spieler auf dem gleichen Rechner sind, verwendet man für die IP-Adresse `127.0.0.1` oder `localhost`.

Das Ganze würde dann so aussehen:

    python.exe main.py <player_name> <local_port> [<remote_ip> <remote_port>]

Nachdem beide Spieler alle ihre Schiffe auf dem Spielfeld platzieren, werden sie miteinander verbunden und können anfangen,
das Spiel zu spielen.


## Aufbau




## Probleme beim Coden

Die erste Herausforderung war es, Python erstmal zu lernen. Dies haben wir zum Beispiel mit Hilfe von verschiedenen Videos
gemacht. Die Webseite https://www.w3schools.com/python/default.asp war auch sehr hilfreich.
