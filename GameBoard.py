import threading
import time


class GameBoard:
    board_width = 12
    board_height = 19

    def __init__(self, parent):
        self.playscreen = parent
        self.lock = threading.Lock()

        self.board = [[0] * GameBoard.board_width for _ in range(GameBoard.board_height)]
        self.bullets = list()

        self.plane = [18, 5]
        self.board[self.plane[0]][self.plane[1]] = 1

        self.calculate_bullet()

    def move(self, direction):
        if direction == 'left':
            self.board[self.plane[0]][self.plane[1]] = 0
            if self.plane[1] > 0: self.plane[1] -= 1
            self.board[self.plane[0]][self.plane[1]] = 1

        elif direction == 'right':
            self.board[self.plane[0]][self.plane[1]] = 0
            if self.plane[1] < (GameBoard.board_width - 1): self.plane[1] += 1
            self.board[self.plane[0]][self.plane[1]] = 1

        elif direction == 'shoot':
            blt = Bullet(self.plane[1])
            self.board[blt.y][blt.x] = 2
            self.bullets.append(blt)

        #self.playscreen.refresh()

    def calculate_bullet(self):
        self.lock.acquire()
        try:
            for blt in self.bullets:
                self.board[blt.y][blt.x] = 0
                if blt.y > 0 :
                    blt.y -= 1
                    self.board[blt.y][blt.x] = 2
                else:
                    self.bullets.remove(blt)
        finally:
            self.lock.release()

        if self.playscreen.isFocused:
            t = threading.Timer(0.2, self.calculate_bullet)
            t.daemon = True
            t.start()


class Bullet:
    def __init__(self, column):
        self.x = column
        self.y = 17