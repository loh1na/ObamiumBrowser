# coded by loh1na
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
import sys
#import threading

class MainWindow(QMainWindow):

	def __init__(self):
		super(MainWindow,self).__init__()
		# load browser
		defurl = 'https://duckduckgo.com'
		self.browser = QWebEngineView()
		self.browser.setUrl(defurl)
		self.setCentralWidget(self.browser)

		#multithreading not ended
		# self.thread = QThread()

		# navigation bar
		self.nav_bar = QToolBar('Navigation bar')
		self.addToolBar(self.nav_bar)

		self.nav_bar.addSeparator()

		#line
		self.edit = QLineEdit()
		self.edit.returnPressed.connect(lambda: self.GoTo())
		self.nav_bar.addWidget(self.edit)


		#back button
		back_bt = QAction("<", self)
		back_bt.triggered.connect(self.browser.back)
		self.nav_bar.addAction(back_bt)

		#refresh button
		ref_bt = QAction("O", self)
		ref_bt.triggered.connect(self.browser.reload)
		self.nav_bar.addAction(ref_bt)

		#Forward
		forw_bt = QAction(">", self)
		forw_bt.triggered.connect(self.browser.forward)
		self.nav_bar.addAction(forw_bt)





		self.show()


	def GoTo(self):
		if 'https://' in self.edit.text():
			self.browser.setUrl(QUrl(self.edit.text()))
			#print("https")
		elif '.com' in self.edit.text():
			self.browser.setUrl(QUrl("https://" + self.edit.text()))
			#print(".com")
		else:
			self.browser.setUrl(QUrl("https://duckduckgo.com/?q=" + self.edit.text()))
			#print("find")



if __name__ == '__main__':
	main = QApplication()
	main.setApplicationName('Obamium')
	window = MainWindow()


	main.exec()
