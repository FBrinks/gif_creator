# Image GIF Creator

## Overview
Image GIF Creator är en Python-applikation som låter användare ladda in, sortera och skapa animerade GIF:ar av bilder. Programmet har ett användarvänligt grafiskt gränssnitt byggt med Tkinter och använder Pillow, imageio och OpenCV för bildhantering och bearbetning.

## Funktioner
- Ladda in flera bilder från filsystemet (`*.jpeg`, `*.jpg`, `*.png`).
- Sortera bilder manuellt (flytta upp/ned i listan).
- Skapa och spara en GIF med standardvisningstid per bild.
- GIF:en sparas i samma mapp som de inlästa bilderna.
- (Förberett för framtida bildbehandling och filter.)

## Projektstruktur
```
image-gif-creator
├── src
│   ├── main.py            # Startar applikationen
│   ├── gui.py             # GUI-komponenter och logik
│   ├── image_loader.py    # Funktioner för att ladda bilder
│   ├── image_sorter.py    # Funktioner för att sortera/flytta bilder
│   ├── image_processor.py # Bildbehandling (förberett för filter mm)
│   ├── gif_creator.py     # Skapar och sparar GIF
│   └── utils.py           # Hjälpfunktioner
├── requirements.txt       # Projektberoenden
└── README.md              # Dokumentation
```

## Installation
Installera beroenden med pip:

```
pip install -r requirements.txt
```

## Användning
1. Starta programmet:
   ```
   python src/main.py
   ```
2. Använd GUI:t för att:
   - Ladda in bilder från din dator.
   - Sortera bilderna genom att flytta dem upp eller ned i listan.
   - Klicka på "Skapa och spara GIF" och ange ett filnamn.
   - GIF:en sparas i samma mapp som dina bilder.

## Beroenden
- tkinter
- Pillow
- imageio
- opencv-python

## Licens
Detta projekt är licensierat under MIT-licensen – se LICENSE för detaljer.

## Vidare utveckling
- Implementera en manuell hantering av tidsinställningar för varje bild i GIF:en.
- Implementera en komprimeringsfunktion för att minska GIF:ens filstorlek.
- Implementera en bildhantering som säkerställer att bilderna är i rätt format och storlek innan de läggs till i GIF:en.