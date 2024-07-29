from pathlib import Path
from xml.etree.ElementTree import tostring
import pygame, eyed3
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time
import vlc


canciones = []
titulos = []
artistas = []
albumnes = []
numeros = []
i = 0
with open("listaCanciones.txt") as fname:
    lineas = fname.readlines()
    num = 1
    for linea in lineas:
        canciones.append(linea.strip('\n'))
        numeros.append(num)
        num += 1
        
instance = vlc.Instance()
player = instance.media_player_new()
#Parametros pantalla Oled

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

disp.fill(0)
disp.show()

image = Image.new('1', (128, 64))

draw = ImageDraw.Draw(image)

#font = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
#font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
#font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 10)
#font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 10)
#font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 10)
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 10)



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.i = 0
        self.pause_estate = False
        self.lista_canciones = canciones
        self.cancion = self.lista_canciones[self.i]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.f_titulo = QtWidgets.QFrame(self.centralwidget)
        self.f_titulo.setGeometry(QtCore.QRect(0, 0, 800, 51))
        self.f_titulo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.f_titulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_titulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_titulo.setObjectName("f_titulo")
        self.label_3 = QtWidgets.QLabel(self.f_titulo)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 211, 31))
        self.label_3.setStyleSheet("font: 20pt \"Segoe Script\";\n"
"color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 50, 801, 551))
        self.frame.setStyleSheet("background-color: rgb(0, 187, 45);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 9, 281, 471))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.c_lista = QtWidgets.QListWidget(self.frame_2)
        self.c_lista.setGeometry(QtCore.QRect(10, 11, 256, 381))
        self.c_lista.setObjectName("c_lista")
        self.c_lista.setStyleSheet("color: rgb(255, 255, 255);")
        self.n_cancion = QtWidgets.QLabel(self.frame_2)
        self.n_cancion.setGeometry(QtCore.QRect(10, 400, 259, 13))
        self.n_cancion.setStyleSheet("color: rgb(0, 187, 45);")
        self.n_cancion.setObjectName("n_cancion")
        self.n_album = QtWidgets.QLabel(self.frame_2)
        self.n_album.setGeometry(QtCore.QRect(10, 440, 259, 13))
        self.n_album.setStyleSheet("color: rgb(0, 187, 45);")
        self.n_album.setObjectName("n_album")
        self.n_artista = QtWidgets.QLabel(self.frame_2)
        self.n_artista.setGeometry(QtCore.QRect(10, 420, 259, 13))
        self.n_artista.setStyleSheet("color: rgb(0, 187, 45);")
        self.n_artista.setObjectName("n_artista")
        self.espectro = QtWidgets.QFrame(self.frame)
        self.espectro.setGeometry(QtCore.QRect(310, 10, 481, 221))
        self.espectro.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.espectro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.espectro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.espectro.setObjectName("espectro")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(310, 240, 481, 241))
        self.frame_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.slider = QtWidgets.QSlider(self.frame_4)
        self.slider.setGeometry(QtCore.QRect(30, 20, 431, 31))
        self.slider.setStyleSheet("color: rgb(0, 187, 45);")
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(30, 60, 51, 21))
        self.label.setStyleSheet("color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(430, 60, 51, 21))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.b_play = QtWidgets.QPushButton(self.frame_4)
        self.b_play.setGeometry(QtCore.QRect(260, 120, 71, 40))
        self.b_play.setStyleSheet("color: rgb(0, 187, 45);\n"
"border-radius:15px;\n"
"border:2px solid rgb(255, 255, 255);")
        self.b_play.setCheckable(True)
        self.b_play.setObjectName("b_play")
        self.b_previus = QtWidgets.QPushButton(self.frame_4)
        self.b_previus.setGeometry(QtCore.QRect(20, 120, 71, 41))
        self.b_previus.setStyleSheet("color: rgb(0, 187, 45);\n"
"border-radius:15px;\n"
"border:2px solid rgb(255, 255, 255);")
        self.b_previus.setObjectName("b_previus")
        self.b_pause = QtWidgets.QPushButton(self.frame_4)
        self.b_pause.setGeometry(QtCore.QRect(150, 120, 71, 40))
        self.b_pause.setStyleSheet("color: rgb(0, 187, 45);\n"
"border-radius:15px;\n"
"border:2px solid rgb(255, 255, 255);")
        self.b_pause.setCheckable(True)
        self.b_pause.setObjectName("b_pause")
        self.b_next = QtWidgets.QPushButton(self.frame_4)
        self.b_next.setGeometry(QtCore.QRect(390, 120, 71, 40))
        self.b_next.setStyleSheet("color: rgb(0, 187, 45);\n"
"border-radius:15px;\n"
"border:2px solid rgb(255, 255, 255);")
        self.b_next.setObjectName("b_next")
        self.radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton.setGeometry(QtCore.QRect(410, 210, 82, 17))
        self.radioButton.setStyleSheet("color: rgb(0, 187, 45);")
        self.radioButton.setObjectName("radioButton")
        self.c_number = QtWidgets.QLabel(self.frame_2)
        self.c_number.setGeometry(QtCore.QRect(240, 450, 61, 21))
        self.c_number.setStyleSheet("color: rgb(0, 187, 45);\n"
"font: 11pt \"Arial\";")
        self.c_number.setObjectName("c_number")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.b_play.clicked.connect(self.play)
        self.b_pause.clicked.connect(self.pausa)
        self.b_next.clicked.connect(self.siguiente)
        self.b_previus.clicked.connect(self.anterior)
        self.n_cancion.setText(f'Cancion {self.cancion}')
        self.slider.sliderMoved.connect(self.tiempo)
        #self.label.setText(f'{self.tiempo}')
        

    #def lista(self):
        j = 0
        numero = 1 
        for j in  self.lista_canciones:
                
            newItem = (str(numero)+".- "+str(j))
            self.c_lista.addItem(newItem)
            numero += 1
            ruta = str("Canciones/"+str(j))
            audiofile = eyed3.load(ruta)
            artista = str(audiofile.tag.artist)
            album = str(audiofile.tag.album)
            titulo = str(audiofile.tag.title)

            artistas.append(artista)
            albumnes.append(album)
            titulos.append(titulo)

        self.n_cancion.setText(f'Cancion {titulos[self.i]}')        
        self.n_artista.setText(f'Artista: {artistas[self.i]}')
        self.n_album.setText(f'Album: {albumnes[self.i]}')

                


    def siguiente(self): 
        if (self.i < 100 and self.radioButton.isChecked()):
            aleatorio = random.randint(1, 100)
            self.i = aleatorio  
            music.vlcPlay("Canciones/"+canciones[self.i])
            self.n_cancion.setText(f'Cancion {titulos[self.i]}') 
            self.n_artista.setText(f'Artista: {artistas[self.i]}')
            self.n_album.setText(f'Album: {albumnes[self.i]}')
            self.c_number.setText(f'{self.i+1}/100')
        elif (self.i < 100 ):
            self.i += 1   
            music.vlcPlay("Canciones/"+canciones[self.i])
            self.n_cancion.setText(f'Cancion {titulos[self.i]}') 
            self.n_artista.setText(f'Artista: {artistas[self.i]}')
            self.n_album.setText(f'Album: {albumnes[self.i]}')
            self.c_number.setText(f'{self.i+1}/100')
        self.pantallaInfo()
                

    def anterior(self):
        if(self.i > 1 and self.radioButton.isChecked()):
            aleatorio = random.randint(1, 100)
            self.i = aleatorio
            music.vlcPlay("Canciones/"+canciones[self.i])
            self.n_cancion.setText(f'Cancion {titulos[self.i]}') 
            self.n_artista.setText(f'Artista: {artistas[self.i]}')
            self.n_album.setText(f'Album: {albumnes[self.i]}')
            self.c_number.setText(f'{self.i+1}/100')
        elif(self.i >= 1):
            self.i -= 1
            music.vlcPlay("Canciones/"+canciones[self.i])
            self.n_cancion.setText(f'Cancion {titulos[self.i]}') 
            self.n_artista.setText(f'Artista: {artistas[self.i]}')
            self.n_album.setText(f'Album: {albumnes[self.i]}')
            self.c_number.setText(f'{self.i+1}/100')
        self.pantallaInfo()
            

    def play(self):
        self.pantallaInfo()
        music.vlcPlay("Canciones/"+canciones[self.i])
    
    def pausa(self):
        if (self.pause_estate == False):
            music.pause()
            self.pause_estate = True
        else:
            music.reanude()
            self.pause_estate =False

    def reanudar(self):
        music.reanude()

    def parar(self):
        music.stop()

    def tit(self):
        music.titulo(canciones[self.i])

    def artis(self):
        music.artista(canciones[self.i])

    def alb(self):
        music.album(canciones[self.i])

    def tiempo(self):
        #music.time(canciones[self.i])
        music.time()

    def pantallaInfo(self):
        pantalla.printInfo(titulos[self.i], artistas[self.i], albumnes[self.i])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Music Player"))
        self.n_cancion.setText(_translate("MainWindow", "Cancion: "))
        self.n_album.setText(_translate("MainWindow", "Album:"))
        self.n_artista.setText(_translate("MainWindow", "Artista:"))
        self.c_number.setText(_translate("MainWindow", "1/100"))
        self.label.setText(_translate("MainWindow", "00:00"))
        self.label_2.setText(_translate("MainWindow", "00:00"))
        self.b_play.setText(_translate("MainWindow", ">||"))
        self.b_previus.setText(_translate("MainWindow", "|<"))
        self.b_pause.setText(_translate("MainWindow", "||"))
        self.b_next.setText(_translate("MainWindow", ">|"))
        self.radioButton.setText(_translate("MainWindow", "Aleatorio"))

class reproductor:
    
    def vlcPlay(self, cancion):
        
        media = instance.media_new(cancion)
        player.set_media(media)
        player.play()
        
 
    """def reproducir(self,cancion):
        pygame.mixer.init() #Starts the mixer
        pygame.mixer.music.load(cancion)
        pygame.mixer.music.play()"""
        

    def pause(self):
        player.pause()
        #pygame.mixer.music.unpause()
        #pygame.mixer.music.pause()
    
    def reanude(self):
        player.pause()
#          pygame.mixer.music.unpause()
    
    def stop(self):
        pygame.mixer.music.stop()

    def titulo(self, cancion):
        audiofile = eyed3.load(cancion)
        title = str(audiofile.tag.title)
        return title

    def artista(self, cancion):
        audiofile = eyed3.load(cancion)
        artist = str(audiofile.tag.artist)
        return  artist

    def album(self, cancion):
        audiofile = eyed3.load(cancion)
        albu = str(audiofile.tag.album)
        return albu

    def time(self):
        return player.get_time()
        """pos_time = pygame.mixer.music.get_pos()
        s = pos_time // 1000
        m, s = divmod(s, 60)
        m, s = int(m), int(s)
        print(str(m)+":"+str(s))"""

class oled:
    
    
    def printInfo(self, name, artist, album):
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        
        draw.text((10, 5),    '-Cancion: ',  font=font1, fill=255)
        draw.text((55, 15), name, font=font, setFont = 18,  fill=255)
        draw.text((10, 25),    '-Artista: ',  font=font1, fill=255)
        draw.text((50, 35), artist, font=font, setFont = 18,  fill=255)
        draw.text((10, 45),    '-Album: ',  font=font1, fill=255)
        draw.text((50, 53), album, font=font, setFont = 18,  fill=255)

        # Muestra Texto
        disp.image(image)
        disp.show()
        
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    music = reproductor()
    pantalla = oled()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())