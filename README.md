# DUE
Postás András | SNRW3J
Egy adatkezelő programot készítettem, amelyben lehetőségünk van felvenni egysorban bármilyen adatot, azt törölni, megnyitni, majd az adatlistát elmenteni, felülírni és betölteni
2 fő fájl van, ebből:
-bead_snrw3j.py : fő saját modul
	-ebben lévő meghívott modulok	: tanult modul : tkinter
					                      : bemutatandó modul :atexit
-class.py : saját modul amely osztályt tartalmaz, amit könyvelésre példányosítunk

def Felvetel():a beírt szöveget felvesszük a listára

def Torles():a kijelölt szöveget kitöröljük a listából

def LabelAtiras(event): ezt a függvényt használjuk (eseménykezeléssel), hogy frissítsük az éppen kijelölt szövegnek a kiírását

def FajlBetoltes(): betöltünk egy listát fájlból

def FajlMentes(): mentjük és/vagy felülírjuk a listát fájlba

def konyveles(): függvény amivel fájlba könyvelünk lista elemszámot példányozott osztályból
