#### Grundsätzliche Idee und Planung
hiermit setze ich fürs Erste kleine Meilensteine.
- Projekt Erstellung auf Github (Repository) & meinen Kollegen Lucas als mit Entwickler hinzufügen (Collaborators).
- Das Repository auf den eigenen Laptop laden (clone, pull), bearbeiten (add, commit) & hochladen (push).

Um zukünftig immer wieder zu reproduzieren und um zu verinnerlichen, schreibe ich die Schritte, die man für diese Meilensteine benötigt hiermit auf.

#### Das Repository erstellen:
Um sein Projekt für eine Gruppe oder Online zu erstellen gibt es auf Github.com die Möglichkeit einen Repository zu erstellen es ist so zu sagen ein Ordner in den man mehrere Inhalte wie z.B. Code-Programme legen kann. Dafür brauch man auf der Webseite einen Account. Ist der Account angelegt, so navigiert man zum Dashboard dort hat man ein Überblick auf seine bereits erstellten Repo's oder zum Erstellen von einer Repo nutzt man den Button (NEW) dort gibt man dem Projekt einen Namen, eine Beschreibung und Konfigurationen, dann klickt man auf erstellen und landet auf der Start (<>Code) Seite seines Projekts und in den Einstellungen kann man unter Collaborators dann weitere Entwickler hinzufügen.

#### Das Arbeiten in der Repository
hier möchte ich einmal den Workflow festhalten und aufzeigen wie genau man Dateien Lokal ladet. Bearbeitet und wieder hochläd.

**Dateien aus das Repository laden:**
Um den Inhalt ordnungsgemäß zu laden, um im Nachhinein damit zu arbeiten, benötigen wir die Quelle die finden wir auf der Startseite der Repo mit dem Button (Code) findet man direkt den Reiter HTTPS dort kopiert man die URL und öffnet die Kommandozeile seines Geräts z.B. CMD/Powershell dort navigiert man zuerst zu dem Ort, in dem man das Projekt bearbeiten möchte in unserem Beispiel den Desktop mit dem Befehl
```powershell
cd Desktop
```
Dort nutzen wir dann den Clone Befehl, um das Repo lokal auf unserem Gerät zu laden.
```powershell
git clone [url]
```
Um weiterhin im CMD/Powershell zu arbeiten ist es wichtig wieder zu der Repo zu navigieren mit:
```
cd pygame-tetris
```
Aber es ist nun auch möglich einfach visuell auf dem Repo zu arbeiten da dieser als Ordner auf dem Desktop oder im ausgesuchten Ort liegt.

**Dateien mit Git als bearbeiten listen:**
Nun haben wir das Repo Lokal auf dem Gerät damit können wir bereits bestehende Programme bearbeiten oder neue Dateien darin erstellen dabei ist es nicht relevant wie diese Dateien erstellt/bearbeitet werden. Sobald eine neue Datei angelegt wurde, gibt es zwei Befehle 
```powershell
git add [Datei]
``` 
Dieser Fügt eine spezifische Datei zur Staging Area hinzu.
```powershell
git add .
```
Dieser Fügt alle geänderten und neuen Dateien im aktuellen Verzeichnis zur Staging Area hinzu.
Sobald eine Datei soweit fertig erstellt bzw. bearbeitet wurde, nutzt man ein Commit Befehl, um einen festen Speicherpunkt in der Historie mit einer Nachricht zu versehen. 
```powershell
git commit -m "Die Beispielnachricht"
```
Der Parameter `-m "[Text]"`übergibt die Commit-Nachricht direkt in der Befehlszeile, ohne einen Texteditor zu öffnen.
Alle Daten die im git add dann Commited wurden liegen nun im Lokalen Repository.

**Lokales Repository auf Github laden:**
sofern alle Neuerung und Änderung gesetzt wurden, gibt es den Befehl
```
git push
```
Um alle Commits aus das lokale Repo in das Github zu laden. 

git pull !!!
ist das Lokal Repo mit dem Clone Befehl auf dem Gerät so wird zukünftig mit dem pull Befehl gearbeitet dafür navigieren wir erst wieder zu dem Repo mit
```powershell
cd C:\Users\Jeffrey\Desktop\pygame-tetris
```
und nutzten dann den Pull Befehl:
```
git pull
```
Dieser Befehl hat insgesamt 3 Ausgaben
- Already up to date. 
- 1 file changed, 15 insertions(+)
- CONFLICT
es sagt im Grunde aus, ob es ein Update gab, wenn ja, dann macht er das Update und sollte das Update nicht mehr mit dein bearbeiteten daten übereinstimmen markiert es die Stelle in der Datei und man müsst dann im Editor kurz händisch entscheiden, welcher Code behalten werden soll.

**Zusammenfassend ist der tägliche Arbeitsablauf also:** 
`git pull` ➔ _Programmieren_ ➔ `git add .` ➔ `git commit -m "Mein Fortschritt"` ➔ `git push`.


Die weiteren Meilensteine:
- main.py erstellen und Grundbausteine anwenden.
- Die .json Datei anlegen und die Konfiguration festlegen.