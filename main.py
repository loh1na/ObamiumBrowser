# coded by loh1na
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import *
import sys ,qdarktheme
#import threading

class MainWindow(QMainWindow):

	def __init__(self):
		super(MainWindow,self).__init__()

		# load browser
		defurl = 'https://duckduckgo.com'
		self.browser = QWebEngineView()
		self.browser.setUrl(defurl)
		self.setCentralWidget(self.browser)
		self.browser.loadStarted.connect(lambda: self.loadisstarted())
		self.browser.loadFinished.connect(lambda: self.loadisfinished())



		# navigation bar
		self.nav_bar = QToolBar('Navigation bar')
		self.addToolBar(self.nav_bar)

		self.nav_bar.addSeparator()

		#line
		self.edit = QLineEdit()
		self.edit.returnPressed.connect(lambda: self.GoTo())
		self.nav_bar.addWidget(self.edit)

		#dark theme 
		dark_bt = QAction("dark mode", self)
		dark_bt.triggered.connect(self.setdarktheme)
		self.nav_bar.addAction(dark_bt)

		#progress bar
		self.progress = QProgressBar()
		self.nav_bar.addWidget(self.progress)
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

	def setdarktheme(self):
		main.setStyleSheet(qdarktheme.load_stylesheet())

	def loadisstarted(self):
		self.count = 0
		self.startthread()
		print("loading a web page...")
		while True:
			self.count+=1
			#print(self.count)
			if self.count == 101:
				self.progress.setValue(0)
				break
			self.progress.setValue(self.count)

	def loadisfinished(self):
		print("loaded sucsessfully")
		#self.count = 0
		self.stopthread()


	def startthread(self):
		self.thread = threading(parent=None, index=2)
		self.thread.start()	

	def stopthread(self):
		self.thread.stop()



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

class threading(QThread):

	any_signal = Signal(int)

	def __init__(self, parent=None, index=0):
		super(threading, self).__init__(parent)

		self.index = index

	def run(self):
		print("starting thread ",self.index)
		while True:
			window = MainWindow.__init__
			self.any_signal.emit(window)

	def stop(self):
		self.terminate()
		print("stopping thread", self.index)

		


if __name__ == '__main__':
	main = QApplication()
	main.setApplicationName('Obamium')
	window = MainWindow()


	main.exec()
