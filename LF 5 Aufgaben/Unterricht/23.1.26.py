#1. Lesen Sie den Dateinamen von der Tastatur ein.
#2. Önen Sie die Datei zum Lesen.
#3. Lesen Sie die Datei ein. (Sie können die Datei lorem_ipsum.txt verwenden.)
#4. Geben Sie den Dateiinhalt aus.
#5. Schlieÿen Sie die Datei, wenn der ganze Inhalt ausgegeben wurde.



Dateiname = input("Gib Dateiname an:")

file = open(Dateiname, "r")
content = file.read()

print(content)

