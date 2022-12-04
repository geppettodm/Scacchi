import chess
import chess.polyglot
from Engine import Engine


class Chess:

    def __init__(self):
        self.board = chess.Board()
        self.engine:Engine;

    def startGame(self):
        color=None
        depth=0

        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        while(depth < 2 or depth > 7):
            depth = int(input("""Depth: """)) 
        self.engine=Engine(depth);

        if color=="w":
            while (not self.board.is_checkmate()):
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("The engine is thinking...")
                self.playEngineMove(depth)
            print(self.board)
            print(self.board.outcome())
        elif color=="b":
            while (not self.board.is_checkmate()):
                print("The engine is thinking...")
                self.playEngineMove(depth)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())  

    def playHumanMove(self):
        try:
            print(self.board.legal_moves)
            play = input("Your move: ")
            self.board.push_san(play)
        except:
            self.playHumanMove()

    #play engine move
    def playEngineMove(self, depth):
        try:
            self.board.push(chess.polyglot.MemoryMappedReader("lib/computer.bin").weighted_choice(self.board).move)
        except:
            self.board.push(self.engine.negamax(self.board, depth))