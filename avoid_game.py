import pyxel
import random

class SimpleGame:
    def __init__(self):
        pyxel.init(160, 120)
        self.player_x = 72
        self.player_y = 100
        self.obstacles = []
        self.score = 0
        self.game_over = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R):
                self.__init__()
            return

        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 8)

        if pyxel.frame_count % 10 == 0:
            self.obstacles.append([random.randint(0, pyxel.width - 8), 0])

        for obs in self.obstacles:
            obs[1] += 2

        for obs in self.obstacles:
            if (self.player_x < obs[0] + 8 and self.player_x + 8 > obs[0] and
                self.player_y < obs[1] + 8 and self.player_y + 8 > obs[1]):
                self.game_over = True

        self.obstacles = [obs for obs in self.obstacles if obs[1] < pyxel.height]
        self.score += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.player_x, self.player_y, 8, 8, 11)
        for obs in self.obstacles:
            pyxel.rect(obs[0], obs[1], 8, 8, 8)
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        if self.game_over:
            pyxel.text(40, 60, "GAME OVER! R to Restart", pyxel.frame_count % 16)

SimpleGame()


## 安装black