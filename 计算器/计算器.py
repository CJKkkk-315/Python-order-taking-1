from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import sys,math,string

class Calculator(QWidget):
  def __init__(self,parent=None):
    QWidget.__init__(self,parent=parent)
    self.initUI()
    self.last=[]
  def initUI(self):
    list=['&','**','s','C',7,8,9,'+',4,5,6,'-',1,2,3,'*',0,'.','=','/']
    length=len(list)
    #创建动态按钮
    for i in range (length):
      self.button=QPushButton(str(list[i]),self)
      #将按钮的clicked信号与onButtonClick函数相连
      self.button.clicked.connect(self.onButtonClick)
      x=i%4
      y=int(i/4)
      self.button.move(x*40+10,y*40+100)
      self.button.resize(30,30)
    #创建文本框
    self.lineEdit=QLineEdit('',self)
    self.lineEdit.move(10,10)
    self.lineEdit.resize(150,70)
    self.setGeometry(200,200,170,300)
    self.setWindowTitle('计算器')
    self.show()
  def onButtonClick(self):
    t=self.lineEdit.text()#获取文本框文本
    new=self.sender().text()
    self.last.append(new)
    print(self.last)
    self.lineEdit.setText(t+new)
    if new== "=":
      result=eval(str(t))#计算
      self.lineEdit.setText(str(result))
    if new=='C':
      self.lineEdit.setText('')
    if new=='sqrt':
      self.lineEdit.setText('')
      result=math.sqrt(string.atof(t))
      self.lineEdit.setText(str(result))
    if new=="**":
      self.lineEdit.setText('')
      result=string.atof(t)**2
      self.lineEdit.setText(str(result))

app=QApplication(sys.argv)
w=Calculator()
w.show()
sys.exit(app.exec_())