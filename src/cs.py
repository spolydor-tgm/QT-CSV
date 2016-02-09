import sys
from PySide.QtGui import QApplication, QWidget

from src import gui
import csv

class cs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.myForm = gui.Ui_Form()
        self.myForm.setupUi(self)
        self.myForm.el.clicked.connect(self.buttonHit)  #Button verbinden mit Methode

    def read(self):
        with open('tcs.csv', newline='') as csvfile:    #csv File oeffnen
            txt = ""
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')  #csv-File einlesen
            for row in spamreader: #jede reihe durchgehen
                txt += str(', '.join(row)) + "\n"   #jede spalte der reihe auslesen

            self.myForm.tb.setText(txt) #ausgelesenes csv-File in der GUI anzeigen/ausgeben

    def buttonHit(self):
        self.read() #Methode zum einlesen ausfuehren

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = cs()
    c.show()
    sys.exit(app.exec_())