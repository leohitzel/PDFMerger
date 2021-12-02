import PyPDF2
from pathlib import Path
import sys

pdfs = []

name = input('Wie soll die fertige PDF Datei heißen? (.pdf nicht nötig) >>> ') + '.pdf'
if len(name) < 5:                   # Definition eines Standardnamens für die Datei
    name = 'merged_pdf.pdf'

print('TIPP: Shift + Rechtsklick auf eine Datei in Windows -> "Als Pfad kopieren"')
target_path = input(f'In welchem Ordner soll {name} gespeichert werden? >>> ')
target_path = target_path.lstrip('"').rstrip('"')
print(f'Bitte kontrollieren Sie ihren Zielordner -> {Path(target_path)}')

if not Path(target_path).exists():
    while True:
        print('Pfad existiert nicht!')
        target_path = input(f'In welchen Ordner soll {name} gespeichert werden? >>> ')
        target_path = target_path.lstrip('"').rstrip('"')
        if Path(target_path).exists():
            break
else:
    pass

while True:
    folder_or_files = input("""Wollen Sie einen Ordner auswählen, in dem alle vorhandenen PDFs zu einem gemerged
werden, oder wollen Sie alle PDFs einzeln auswählen? ((O)rdner/(E)inzeln/(A)bbruch) >>> """).lower()
    if folder_or_files == 'o' or folder_or_files == 'e':
        break
    elif folder_or_files == 'a':
        sys.exit('Programm abgebrochen!')
    else:
        print('Entschuldige, dieses Command verstehe ich nicht!')

# Ab hier ist der Code spezifisch für einzelne PDF Dateien
if folder_or_files == 'e':
    while True:
        user_input = input('Geben Sie einen Pfad eines PDF Dokumentes an (q zum fertigstellen) >>> ')
        user_input = user_input.lstrip('"').rstrip('"')
        if user_input == 'q' or user_input == 'Q':
            break
        if Path(user_input).exists() and Path(user_input).suffix == '.pdf':
            pdfs.append(user_input)
        else:
            print('Pfad existiert nicht, oder Datei ist kein PDF!')

# Ab hier ist der Code spezifisch für Ordner
elif folder_or_files == 'o':
    user_input = input('Geben Sie einen Pfad eines Ordners an >>> ')
    user_input = user_input.lstrip('"').rstrip('"')
    while not Path(user_input).exists():
        print('Pfad existiert nicht!')
        user_input = input('Geben Sie einen Pfad eines Ordners an >>> ')
        user_input = user_input.lstrip('"').rstrip('"')
    for p in Path(user_input).glob('*.pdf'):
        pdfs.append(str(p))


merger = PyPDF2.PdfFileMerger()

while True:
    question1 = input('Wollen Sie die fertige Datei speichern? (y/n) >>> ').lower()
    if question1 == 'y':
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(target_path + fr'\{name}')
        break
    elif question1 == 'n':
        print('Bis zum nächsten mal!')
        break
    else:
        print('Entschuldige, dieses Command verstehe ich nicht!')
