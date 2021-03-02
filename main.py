import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        navbar = QToolBar()
        self.addToolBar(navbar)


        back_button = QAction('🠔', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)
        

        forward_button = QAction('🠖', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)


        reload_button = QAction('🗘', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)
        
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        

        self.browser.urlChanged.connect(self.update_url)

    def update_url(self, url):
        self.url_bar.setText(url.toString())


    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl("https://" + url))


app = QApplication(sys.argv)
QApplication.setApplicationName('Browser')
window = MainWindow()
app.exec_()
