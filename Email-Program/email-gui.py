from PyQt5.QtWidgets import *
from PyQt5 import QtCore
 
class Email(QWidget):
	def __init__(self, parent=None):
		super(Email, self).__init__(parent)
		self.resize(600,300)
 
		contentLabel = QLabel("Content:")
		self.contentText = QTextEdit()
				
		listLabel = QLabel("List:")
		self.listText=QTextEdit()
		self.listText.setMaximumWidth(100)
		
		hourLabel = QLabel("Hour:")
		self.hourCombo = QComboBox()
		self.hourCombo.setMaximumWidth(100)

		minuteLabel = QLabel("Minute:")
		self.minuteCombo = QComboBox()
		self.minuteCombo.setMaximumWidth(100)
		
		hourlist=['00시', '02시', '04시', '06시']
		self.hourCombo.addItems(hourlist)
		
		minutelist=['00분', '10분', '20분', '30분', '40분', '50분']
		self.minuteCombo.addItems(minutelist)
		
		self.submitButton = QPushButton("Submit")
		self.submitButton.setMaximumWidth(100)
		
		HLayout = QHBoxLayout()
		HLayout.addWidget(contentLabel)
		HLayout.addWidget(self.contentText)
		HLayout.addWidget(listLabel)
		HLayout.addWidget(self.listText)

		HLayout1 = QHBoxLayout()
		#addWidget(위젯, 얼마나 늘릴지 배수인듯 (비율을 맞춰주면됨 1:1:1:1처럼), 늘린 것 안에서의 배열)
		HLayout1.addWidget(hourLabel, 1, QtCore.Qt.AlignRight)
		HLayout1.addWidget(self.hourCombo, 0, QtCore.Qt.AlignRight)
		HLayout1.addWidget(minuteLabel, 0, QtCore.Qt.AlignLeft)
		HLayout1.addWidget(self.minuteCombo, 0, QtCore.Qt.AlignLeft)
		#VLayout = QGridLayout()
		#VLayout.addWidget(self.submitButton)

		 
		self.submitButton.clicked.connect(self.submitContact)
 
		mainLayout = QVBoxLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
		mainLayout.addLayout(HLayout)
		mainLayout.addLayout(HLayout1)
		mainLayout.addWidget(self.submitButton, 0, QtCore.Qt.AlignRight)
 		 
		self.setLayout(mainLayout)
		self.setWindowTitle("Hyun-suk Email Program")
 
	def submitContact(self):
		name = self.contextText.text()
 
		if name == "":
			QMessageBox.information(self, "Empty Field",
                                    "Please enter a name and address.")
			return
		else:
			QMessageBox.information(self, "Success!",
                                    "Hello %s!" % name)
 
if __name__ == '__main__':
	import sys
 
	app = QApplication(sys.argv)
	#app= App(redirect=False)
	
	screen = Email()
	screen.show()
 
	sys.exit(app.exec_())