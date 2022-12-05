import chess
import random

class Engine:
    depth:int   

    pawntable = [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, -20, -20, 10, 10, 5,
        5, -5, -10, 0, 0, -10, -5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, 5, 10, 25, 25, 10, 5, 5,
        10, 10, 20, 30, 30, 20, 10, 10,
        50, 50, 50, 50, 50, 50, 50, 50,
        0, 0, 0, 0, 0, 0, 0, 0]

    knightstable = [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50]

    bishopstable = [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20]

    rookstable = [
        0, 0, 0, 5, 5, 0, 0, 0,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        5, 10, 10, 10, 10, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0]

    queenstable = [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 5, 5, 5, 5, 5, 0, -10,
        0, 0, 5, 5, 5, 5, 0, -5,
        -5, 0, 5, 5, 5, 5, 0, -5,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20]

    kingstable = [
        20, 30, 10, 0, 0, 10, 30, 20,
        20, 20, 0, 0, 0, 0, 20, 20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30]

    def __init__(self, depth:int):
        self.depth=depth;

    # def quiesce(self, board:chess.Board):
    #     ex=False;
    #     maxim= -1000;
    #     for move in board.legal_moves:
    #         if board.is_capture(move):
    #             ex=True;
    #             board.push(move)
    #             print("+")
    #             score = -self.evaluate(board)
    #             maxim = max(score,maxim)
    #             board.pop();
    #     if ex:
    #         return maxim;
    #     else:
    #          return self.evaluate(board)


    def evaluate(self, board:chess.Board):
        if board.is_checkmate():
            return -9999
        if board.is_stalemate():
            return 0
        if board.is_insufficient_material():
            return 0
        

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

        mat = (P-p)*100 + (N-n)*300 + (B-b)*350 + (R-r)*500 + (Q-q)*900

        pawns = sum([self.pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)]) - sum(
            [self.pawntable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])
        knights = sum([self.knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)]) - sum(
            [self.knightstable[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.BLACK)])
        bishops = sum([self.bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)]) - sum(
            [self.bishopstable[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])        
        rooks = sum([self.rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) - sum(
            [self.rookstable[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.BLACK)])        
        queens = sum([self.queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) - sum(
            [self.queenstable[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.BLACK)])        
        kings = sum([self.kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)]) - sum(
            [self.kingstable[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])

        if(board.turn):
            return mat+pawns+knights+bishops+rooks+queens+kings
        else:
            return -(mat+pawns+knights+bishops+rooks+queens+kings)



    def negamax(self, board:chess.Board, depth:int, a:int, b: int):
        bestMove:chess.Move
        if (depth==0):
            return self.evaluate(board)
        if (board.is_checkmate() or board.is_insufficient_material()):
            return self.evaluate(board);
        maxScore = -9999
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
            return bestMove
        return maxScore




