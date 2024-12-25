# 导入pygame库，用于游戏开发
import pygame
# 从pygame.locals模块导入所有常量，方便使用
from pygame.locals import *
# 从utils模块导入所有内容，假设utils模块包含一些工具函数
from utils import *
# 从const模块导入所有内容，假设const模块包含一些常量定义
from const import *

class Player(pygame.sprite.Sprite):
    def __init__(self, imgPaths, x, y, xMin, xMax):
     
        # 调用父类Sprite的构造函数，确保Player类继承了Sprite的所有属性和方法
        super(Player, self).__init__()
        # 初始化玩家的图像列表
        self.images = []
        # 初始化当前显示的图像索引
        self.imageIndex = 0
        # 设置玩家的初始x坐标
        self.posX = x
        # 设置玩家的初始y坐标
        self.posY = y
        # 设置玩家的x坐标最小值
        self.posXMin = xMin
        # 设置玩家的x坐标最大值
        self.posXMax = xMax
        # 设置上一次图像切换的时间
        self.preChangeTime = getCurrentTime()
        # 遍历图像文件路径列表
        for path in imgPaths:
            # 加载图像文件
            img = pygame.image.load(path)
            # 将图像缩放到指定的大小（PLAYER_SIZE_W, PLAYER_SIZE_H）
            img = pygame.transform.scale(img, (PLAYER_SIZE_W, PLAYER_SIZE_H))
            # 将图像添加到图像列表中
            self.images.append( img )

    def update(self):
      
        # 获取当前按下的键盘按键
        pressed = pygame.key.get_pressed()
        # 如果按下了左箭头键
        if pressed[K_LEFT]:
            # 如果玩家的x坐标大于最小值
            if self.posX > self.posXMin:
                # 将玩家的x坐标向左移动3个单位
                self.posX -= 3
        # 如果按下了右箭头键
        if pressed[K_RIGHT]:
            # 如果玩家的x坐标小于最大值
            if self.posX < self.posXMax:
                # 将玩家的x坐标向右移动3个单位
                self.posX += 3
        
        # 如果当前时间与上一次图像切换的时间间隔大于200毫秒
        if getCurrentTime() - self.preChangeTime > 200:
            # 更新上一次图像切换的时间
            self.preChangeTime = getCurrentTime()
            # 更新当前显示的图像索引
            self.imageIndex = (self.imageIndex + 1) % len(self.images)

    def GetRect(self):
      
        # 获取当前显示的图像
        image = self.images[ self.imageIndex ]
        # 获取图像的矩形区域
        rect = image.get_rect()
        # 设置矩形区域的x坐标
        rect.x = self.posX
        # 设置矩形区域的y坐标
        rect.y = self.posY
        # 返回矩形区域
        return rect
    
    def draw(self, surface):
      
        # 获取当前显示的图像
        image = self.images[ self.imageIndex ]
        # 在指定的表面上绘制玩家的图像
        surface.blit(image, self.GetRect())
