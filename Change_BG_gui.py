''' Notes on PyQt5 Gui Programming with python 3'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Gui(QWidget):

	def __init__(self):
		#call made to the parent class, which is the top level window object(QtWidgets)
		super(Gui,self).__init__()
		#call made to setGeometry function on self(setting the top level window's screen position and dimensions )
		self.setGeometry(500,250,500,250)
		#call made to setWindowTitle on self(stes the title of top level window)
		self.setWindowTitle("PyQt5 Demo Gui")
		#call made to setAutoFillBackGround on main widget(self) which allows the background to fill out the widget
		self.setAutoFillBackground(True)
		#using the Qcolor class we can create color objects and pass it into a Palette constructor of which we can use it to change the color of a widget
		backcolor = QColor("teal")
		forecolor = QColor("gray")
		self.setPalette(QPalette(forecolor,backcolor))
		#creation of a start button to start the splash window
		#call made to the splash window function
		self.splash_window()

		

	def splash_window(self):
		#creating color objects to go into our palette
		fcolor = QColor("aquamarine")
		bcolor = QColor("black")
		#creating label object and placing it into self(top level window)
		label = QLabel(self)
		#call made to setText function on label(sets the text shown on window)
		label.setText("Welcome to my PyQt5 demo gui")
		#call made to the setFont() function on label object using the constructor method
		label.setFont(QFont("proggy",pointSize = 16,weight = 50))
		#call made to move function on label(positions the label on self(top level window))
		label.move(70,175)
		#creates a label that will hold an image
		image_label = QLabel(self)
		#sets the label to hold a pixmap(image), QPixmap widget is passed through parameters which collects the image filename
		image_label.setPixmap(QPixmap("welcome.jpg"))
		image_label.move(125, 25)
		#creating a button object 
		self.btn1 = QPushButton(self)
		#by using the setText function on the object button we are able to show a text on the button
		self.btn1.setText("Try Me!")
		#call made to resize function on button object in order change the size of the button
		self.btn1.resize(75,20)
		self.btn1.clicked.connect(self.change_bg)
		#btn1_forecolor = QColor("teal")
		#btn1_backcolor = QColor("orange")
		#btn1.setPalette(QPalette(btn1_forecolor,btn1_backcolor))
		self.btn1.move(235,210)
		btn2 = QPushButton(self)
		#sets places an icon on the button object
		btn2.setText("Me Next")
		btn2.resize(75 ,20)
		btn2.move(155,210)
		#connects a signal(clicked) to a slot/function
		btn2.clicked.connect(self.change_back)
		#Adding the color palette to our buttons
		self.btn1.setPalette(QPalette(fcolor,bcolor))
		btn2.setPalette(QPalette(fcolor,bcolor))

	def change_bg(self):
		pal = QPalette(QColor("white"),QColor("blue"))
		self.setPalette(pal)

	def change_back(self):
		pal = QPalette(QColor("white"),QColor("teal"))
		self.setPalette(pal)


app = QApplication(sys.argv)
myapp = Gui()
myapp.show()
#This is our system loop, allows the UI to stay on screen.
sys.exit(app.exec_())	

