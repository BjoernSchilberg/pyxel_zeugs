import pyxel
import sqlite3
from datetime import datetime


class HighscoreGame:
    def __init__(self):
        # Initialisiere Pyxel
        pyxel.init(160, 120, title="Highscore Game")
        self.reset_game()

        # SQLite-Datenbank initialisieren
        self.conn = sqlite3.connect("highscores.db")
        self.create_table()

        pyxel.run(self.update, self.draw)

    def create_table(self):
        # Tabelle erstellen, falls nicht vorhanden
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS highscores (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    score INTEGER,
                    date TEXT
                )
            """)

    def reset_game(self):
        # Spielvariablen zurücksetzen
        self.player_x = 80
        self.player_y = 60
        self.score = 0
        self.time_left = 30  # Sekunden
        self.objects = [(pyxel.rndi(0, 150), pyxel.rndi(0, 110)) for _ in range(10)]
        self.game_over = False

    def update(self):
        if not self.game_over:
            # Spieler bewegen
            if pyxel.btn(pyxel.KEY_LEFT):
                self.player_x = max(0, self.player_x - 2)
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.player_x = min(150, self.player_x + 2)
            if pyxel.btn(pyxel.KEY_UP):
                self.player_y = max(0, self.player_y - 2)
            if pyxel.btn(pyxel.KEY_DOWN):
                self.player_y = min(110, self.player_y + 2)

            # Objekte einsammeln
            self.objects = [
                (x, y)
                for x, y in self.objects
                if not (abs(self.player_x - x) < 5 and abs(self.player_y - y) < 5)
            ]
            self.score += 10 * (10 - len(self.objects))  # Punkte addieren

            # Zeit herunterzählen
            self.time_left -= 1 / 30
            if self.time_left <= 0:
                self.game_over = True
        else:
            # Nach Spielende Highscore speichern
            if pyxel.btnp(pyxel.KEY_RETURN):
                name = input("Name eingeben: ")
                self.save_highscore(name)
                self.reset_game()

    def save_highscore(self, name):
        # Highscore in die Datenbank speichern
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO highscores (name, score, date)
                VALUES (?, ?, ?)
            """,
                (name, self.score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            )

    def draw(self):
        pyxel.cls(0)
        if not self.game_over:
            # Spiel zeichnen
            pyxel.text(5, 5, f"Score: {self.score}", 7)
            pyxel.text(100, 5, f"Time: {int(self.time_left)}", 7)
            pyxel.rect(self.player_x, self.player_y, 5, 5, 9)
            for x, y in self.objects:
                pyxel.circ(x, y, 3, 10)
        else:
            # Spielende-Bildschirm
            pyxel.text(50, 60, "GAME OVER", 8)
            pyxel.text(30, 80, "Drücke RETURN für Highscore", 7)


if __name__ == "__main__":
    HighscoreGame()
