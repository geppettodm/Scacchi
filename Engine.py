import chess
import random

class Engine:
    depth:int   

    def __init__(self, depth:int):
        self.depth=depth;

    def evaluate(self, board:chess.Board):
        if board.is_checkmate():
            return -999
        
        P = len(board.pieces(chess.PAWN, chess.WHITE))
        N = len(board.pieces(chess.KNIGHT, chess.WHITE))
        R = len(board.pieces(chess.ROOK, chess.WHITE))
        B = len(board.pieces(chess.BISHOP, chess.WHITE))
        Q = len(board.pieces(chess.QUEEN, chess.WHITE))

        p = len(board.pieces(chess.PAWN, chess.BLACK))
        n = len(board.pieces(chess.KNIGHT, chess.BLACK))
        r = len(board.pieces(chess.ROOK, chess.BLACK))
        b = len(board.pieces(chess.BISHOP, chess.BLACK))
        q = len(board.pieces(chess.QUEEN, chess.BLACK))

        mat = (P-p)*10 + (N-n)*30 + (B-b)*35 + (R-r)*50 + (Q-q)*90

        if(board.turn):
            return mat + random.randrange(0,5,1)
        else:
            return -mat + random.randrange(0,5,1)



    def negamax(self, board:chess.Board, depth:int, a:int, b: int):
        bestMove:chess.Move
        if (depth==0 or board.is_checkmate()):
            return self.evaluate(board)
        maxScore = -999
        for move in board.legal_moves:
            board.push(move)
            score = -self.negamax(board, depth-1, -b, -a)
            maxScore = max(score, maxScore)
            if(score>a):
                a=score
                bestMove=move
                if(a>b):
                    board.pop()
                    break
            board.pop()          
        if(depth==self.depth):
            print(bestMove)
            return bestMove
        return maxScore




