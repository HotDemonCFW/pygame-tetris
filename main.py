# Bibliothek die wir für das Spiel nutzen.
import pygame
import random
import json
import os

# Das Grid-Pattern + Info-Panel
quadrat_größe       = 30    # Die größe in Pixel.
spalten             = 10    # Wie viel Spalten es geben soll.
reihen              = 20    # Wie viele Reihen es geben soll.
info_panel          = 200   # Wie viel Pixel das Info-Panel groß sein soll.
breite              = spalten * reihen + info_panel
höhe                = reihen * spalten
FPS                 = 60    #Damit wir die Geräte nicht überfordern!

# Steuerung einbinden
with open("controls.json", "r") as file:
    controls_data = json.load(file)

# Highscore-Liste einbinden
with open("highscores.json", "r") as file:
    highscores_data = json.load(file)

if __name__ == '__main__':