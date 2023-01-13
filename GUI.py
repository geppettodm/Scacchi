
from threading import Thread
import chess
import chess.svg


import sys
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget




class GUI(QWidget):

    def __init__(self, board:chess.Board):
        self.app = QApplication(sys.argv)
        super().__init__()

        self.setGeometry(100, 100, 620, 620)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 600, 600)

        self.chessboardSvg = chess.svg.board(board).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)
        


    def run(self):
        self.show()
        sys.exit(self.app.exec_())
    
    def update(self, board:chess.Board, w):
        if w==0:
            _board = board.transform(chess.flip_horizontal).transform(chess.flip_vertical)

        else: _board = board
        self.chessboardSvg = chess.svg.board(_board).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)
        self.show()

        
        

        


    
