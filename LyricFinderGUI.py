import lyricScrub
import rhymeDetector
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QVBoxLayout)
from PyQt5.QtCore import pyqtSlot


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.createTopLeftGroupBox()
        self.createLyricsView()
        topLayout = QHBoxLayout()
        topLayout.addWidget(self.topLeftGroupBox)
        topLayout.addStretch(50)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.lyricsView, 0, 3)
        mainLayout.setRowStretch(0, 0)
        mainLayout.setRowStretch(0, 0)
        mainLayout.setColumnStretch(0, 0)
        mainLayout.setColumnStretch(0, 0)
        self.setLayout(mainLayout)

        self.setGeometry(200, 100, 600, 500)

    def createLyricsView(self):
        self.lyricsView = QTextEdit()
        self.lyricsView.setFrameShape(QtWidgets.QFrame.Box)
        self.lyricsView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lyricsView.setLineWidth(3)
        self.lyricsView.setMidLineWidth(1)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Song Details")

        # Song input
        self.songEdit = QLineEdit()
        songLabel = QLabel("&Song:")
        songLabel.setBuddy(self.songEdit)

        # Artist Input
        self.artistEdit = QLineEdit()
        artistLabel = QLabel("Artist:")
        songLabel.setBuddy(self.artistEdit)

        # "Find" button
        findPushButton = QPushButton("Find Lyrics")
        findPushButton.clicked.connect(self.on_click)

        # 'reset button'
        resetPushButton = QPushButton("Reset")
        resetPushButton.clicked.connect(self.resetView)

        # Group box layout
        layout = QVBoxLayout()
        layout.addWidget(songLabel)
        layout.addWidget(self.songEdit)
        layout.addWidget(artistLabel)
        layout.addWidget(self.artistEdit)
        layout.addWidget(findPushButton)
        layout.addWidget(resetPushButton)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        song = self.songEdit.text()
        artist = self.artistEdit.text()

        # Find the lyrics for the song
        lyricScrub.lyricFind(song, artist)
        # Then run the code to figure out the rhyme schemes
        rhymeDetector.get_Lyric_Sounds()
        self.lyricsView.setText(rhymeDetector.Lyrics)

    @pyqtSlot()
    def resetView(self):
        self.songEdit.setText('')
        self.songEdit.update()
        self.artistEdit.clear()
        self.artistEdit.show()
        self.lyricsView.clear()
        lyricScrub.LYRICS = ['']


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
