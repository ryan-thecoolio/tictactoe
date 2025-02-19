class TicTacToe():
    def __init__(self,board,width,height):
        self.board = board
        self.width = width
        self.height = height
        self.length = len(self.board)
        self.round = 0

    def start(self):
        play = Interactive()
        play.start_round()

class Check():
    def __init__(self,board):
        self.board = board
        self.length = len(self.board)
    def winner(self):
        for i in range(self.length):
            total_row = sum(self.board[i])
            r = self.find_row(i,total_row)
            total_col = self.sum_col(i)
            c = self.find_col(i,total_col)
            total_dia1 = self.sum_dia1()
            d1 = self.find_dia1(total_dia1)
            total_dia2 = self.sum_dia2()
            d2 = self.find_dia2(total_dia2)
 
            if r == 3 or c == 3 or d1 == 3 or d2 == 3:
                return 3
            if r == 6 or c == 6 or d1 == 6 or d2 == 6: return 6
        
    def find_row(self,i,total):
        count = 0
        for row in range(self.length): #0 1 2
            if self.board[i][row] == 0:
                break
            else:
                if total == 6 and self.board[i][row] == 2: count += 2
                else:
                    if self.board[i][row] == 1: count += 1
        return count
    
    def sum_col(self,i):
        total_col = 0
        for count in range(self.length):
            total_col += self.board[count][i]
        return total_col

    def find_col(self,i,total):
        count = 0
        for col in range(self.length):
            if self.board[col][i] == 0:
                break
            else:
                if total == 6 and self.board[col][i] == 2:
                    count += 2
                else:
                    if self.board[col][i] == 1:
                        count += 1
        return count
    
    def sum_dia1(self):
        total_dia = 0
        for j in range(self.length):
            total_dia += self.board[j][j]
        return total_dia
    
    def sum_dia2(self):
        total_dia = 0
        for j in range(self.length):
            total_dia += self.board[j][(self.length-j)-1]
        return total_dia
    def find_dia1(self,total):
        count = 0
        for j in range(self.length):
            if self.board[j][j] == 0:
                break
            else:
                if total == 6 and self.board[j][j] == 2:
                    count += 2
                else:
                    if self.board[j][j] == 1:
                        count+=1
        return count

    def find_dia2(self,total):
        count = 0
        for j in range(self.length):
            if self.board[j][(self.length-j)-1] == 0:
                break
            else:
                if total == 6 and self.board[j][(self.length-j)-1] == 2:
                    count += 2
                else:
                    if self.board[j][(self.length-j)-1] == 1:
                        count+=1
        return count

#  ---    ---    --- 
# |  0  |  0  |  0  |
#  ---    ---   ---
# |  0 |  0  |  0  |
#   ---   ---   ---
# |  0  |  0  |  0  |
#  ---   ---    ---

class Interactive():
    def __init__(self):
        self.board = board
        self.pos = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    def start_round(self):
        while True:
            self.p1_turn()
            self.display(self.pos)
            if Check(self.board).winner() == 3:
                print("PLAYER 1 WINS")
                break
            self.p2_turn()
            self.display(self.pos)
            if Check(self.board).winner() == 3:
                print("PLAYER 1 WINS")
                break
            if Check(self.board).winner() == 6:
                print("PLAYER 2 WINS")
                break
    def display(self,pos):
        board_display = (f"-------\n|{pos[1]}|{pos[2]}|{pos[3]}|\n-------\n|{pos[4]}|{pos[5]}|{pos[6]}|\n-------\n|{pos[7]}|{pos[8]}|{pos[9]}|\n-------")
        print(board_display)
    def p1_turn(self):
        p1_input = input("Player 1 | Enter a valid position (1,1)-(3,3): ")
        p1_input = p1_input.replace("(","").replace(")","").split(",")
        while self.board[int(p1_input[0])-1][int(p1_input[1])-1] != 0:
            print("--- Player 1 | Position Taken ---\n")
            p1_input = input("Player 1 | Please enter a different position (1,1)-(3,3): ")
            p1_input = p1_input.replace("(","").replace(")","").split(",")
            if self.board[int(p1_input[0])-1][int(p1_input[1])-1] == 0:
                break
        self.board[int(p1_input[0])-1][int(p1_input[1])-1] = 1
        if int(p1_input[0]) == 1:
            self.pos[int(p1_input[1])] = "X"
        elif int(p1_input[0]) == 2:
            self.pos[int(p1_input[1])+3] = "X"
        else:
            self.pos[int(p1_input[1])+6] = "X"
    def p2_turn(self):
        p2_input = input("Player 2| Enter a valid position (1,1)-(3,3): ")
        p2_input = p2_input.replace("(","").replace(")","").split(",")
        while self.board[int(p2_input[0])-1][int(p2_input[1])-1] != 0:
            print("--- Player 2 | Position Taken ---")
            p2_input = input("Player 2 | Please enter a different position (1,1)-(3,3): ")
            p2_input = p2_input.replace("(","").replace(")","").split(",")
            if self.board[int(p2_input[0])-1][int(p2_input[1])-1] == 0:
                break
        self.board[int(p2_input[0])-1][int(p2_input[1])-1] = 2
        if int(p2_input[0]) == 1:
            self.pos[int(p2_input[1])] = "O"
        elif int(p2_input[0]) == 2:
            self.pos[int(p2_input[1])+3] = "O"
        else:
            self.pos[int(p2_input[1])+6] = "O"
board = [
    [0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

if __name__ == "__main__":
    game = TicTacToe(board,3,3)
    game.start()
