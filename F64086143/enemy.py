import pygame
import math
import os
from settings import PATH
from settings import PATH_2

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))

# 決定走順向或逆向
global decide_path
decide_path = 0

class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        if decide_path % 2 == 0:
            self.path = PATH
        else:
            self.path = PATH_2
        self.path_pos = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]

    def draw(self, win):
        # draw enemy畫出敵人
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        # 畫出血條
        # 血條位置要隨著敵人座標變動
        pygame.draw.rect(win,(255, 0, 0), [(self.x - self.width // 2)+5,(self.y - self.height // 2)-10, 3*(self.max_health), 4])
        pygame.draw.rect(win,(0,255,0), [(self.x - self.width // 2)+5,(self.y - self.height // 2)-10, 3*(self.health), 4])

    def move(self):
        stride = 1
        # 座標點持續更新
        ax, ay = self.path[self.path_pos]  # x, y position of point A
        bx, by = self.path[self.path_pos+1]
        distance_A_B = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2) # 計算距離
        max_count = int(distance_A_B / stride)  # 計算需要多少步數

        if self.move_count < max_count: # 當還未到達總步數時
            unit_vector_x = (bx - ax) / distance_A_B
            unit_vector_y = (by - ay) / distance_A_B
            delta_x = unit_vector_x * stride
            delta_y = unit_vector_y * stride
            # update the coordinate and the counter
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_pos += 1
        """
        Enemy move toward path points every frame
        :return: None
        """
        # ...(to be done)


class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = [Enemy()]  # don't change this line until you do the EX.3 

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """
        # HINT:self.expedition.append(self.reserved_members.pop())
        # ...(to be done)
        self.gen_count += 1
        if self.reserved_members and self.gen_count == self.gen_period: # 當有敵人且gen_count=120
            self.expedition.append(self.reserved_members.pop()) # 將reserved_members的敵人轉給expedition.append
            self.gen_count = 0 # 歸零

    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        # 將enemy存在self.reserved_members，依序出現
        for i in range(num):
            self.reserved_members.append(Enemy())

        decide_path += 1

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)






