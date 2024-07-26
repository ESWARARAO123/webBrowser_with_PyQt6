from PyQt6.QtWidgets import *
import sys
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import *
from PyQt6.QtGui import QAction
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #nav bar
        navbar=QToolBar()
        self.addToolBar(navbar)
        back_btn=QAction('Back',self)
        back_btn.triggered.connect(self.browser.back) 
        navbar.addAction(back_btn)
        front_btn=QAction('front',self)
        front_btn.triggered.connect(self.browser.forward) 
        navbar.addAction(front_btn)
        reload_btn=QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        home_btn=QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.url_update)
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    def navigate_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def url_update(self,q):
        self.url_bar.setText(q.toString())
        
        
app=QApplication(sys.argv)
QApplication.setApplicationName("my own browser")
window=MainWindow()
window.show()
sys.exit(app.exec())
        