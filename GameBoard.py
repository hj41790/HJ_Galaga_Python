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

        self.MAXLV = 5
        self.level = 0
        self.num_stages = 0
        self.list_stages = list()
        self.read_stages()
        self.newstage(self.level)

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
        cnt = 99999
        try:
            if self.speed == 0:
                # move enemies
                cnt = 0
                for y in reversed(range(GameBoard.board_height-1)):
                    for x in range(GameBoard.board_width):
                        if self.board[y][x] > 2:
                            if y+1 == GameBoard.board_height - 1:
                                # GAME OVER
                                self.playscreen.stop_game()
                                return
                            self.board[y+1][x] = self.board[y][x]
                            self.board[y][x] = 0
                            cnt += 1
                self.speed = self.MAXLV - self.level
            else:
                self.speed -= 1

            # move bullets
            for blt in self.bullets:
                self.board[blt.y][blt.x] = 0
                if blt.y > 0:
                    if self.board[blt.y][blt.x] > 2:
                        self.playscreen.update_score(self.board[blt.y][blt.x]**2)
                        self.board[blt.y][blt.x] = 0
                        self.bullets.remove(blt)
                        cnt -= 1;
                        continue

                    blt.y -= 1
                    if self.board[blt.y][blt.x] > 2:
                        self.playscreen.update_score(self.board[blt.y][blt.x]**2)
                        self.board[blt.y][blt.x] = 0
                        self.bullets.remove(blt)
                        cnt -= 1;
                    else:
                        self.board[blt.y][blt.x] = 2
                else:
                    self.bullets.remove(blt)

            if cnt == 0:
                self.level += 1
                self.newstage(self.level%self.num_stages)

        finally:
            self.lock.release()

        if self.playscreen.isFocused:
            t = threading.Timer(0.2, self.calculate_bullet)
            t.daemon = True
            t.start()

    def read_stages(self):
        f = open('.stages', 'r')
        self.num_stages = int(f.readline())
        for i in range(self.num_stages):
            num = int(f.readline())
            stage = list()
            for j in range(num):
                line = [int(n) for n in list(f.readline().replace('\n', ''))]
                stage.append(line)
            self.list_stages.append(stage)
#        print(self.list_stages)
        f.close()
        a = list(range(12))
        a.reverse()
        print(a)

    def newstage(self, lv):
        if self.level == self.MAXLV:
            # GAME OVER
            self.playscreen.stop_game()
            return

        self.speed = self.MAXLV - self.level

        self.bullets.clear()
        for y in range(GameBoard.board_height):
            for x in range(GameBoard.board_width):
                self.board[y][x] = 0

        self.board[self.plane[0]][self.plane[1]] = 1

        stage = self.list_stages[lv]
        for n in range(len(stage)):
            self.board[n] = stage[n][:]

class Bullet:
    def __init__(self, column):
        self.x = column
        self.y = 17