# 导入pygame库，用于游戏开发
import pygame
# 从const模块导入所有内容，假设const模块包含一些常量定义
from const import *

class Block(pygame.sprite.Sprite):
    def __init__(self, blockType, rowIdx, colIdx, relativePos):
       
        # 调用父类Sprite的构造函数，确保Block类继承了Sprite的所有属性和方法
        super(Block, self).__init__()
        # 设置方块的类型
        self.blockType = blockType
        # 使用pygame.image.load函数加载指定路径的图像文件
        self.image = pygame.image.load( BLOCK_RES_FMT % blockType )
        # 使用pygame.transform.scale函数将图像缩放到指定的大小（SPRITE_SIZE_W, SPRITE_SIZE_H）
        self.image = pygame.transform.scale(self.image, (SPRITE_SIZE_W, SPRITE_SIZE_H))
        # 获取图像的矩形区域，并将其赋值给Block类的rect属性
        self.rect = self.image.get_rect()
        # 设置方块的x坐标
        self.rect.x = relativePos[1] + colIdx * self.rect.width
        # 设置方块的y坐标
        self.rect.y = relativePos[0] + rowIdx * self.rect.height
    
    def draw(self, surface):
       
        # 在指定的表面上绘制方块的图像
        surface.blit(self.image, self.rect)

    def GetBlockType(self):
      
        # 返回方块的类型
        return self.blockType
        
    def GetRect(self):
       
        # 返回方块的矩形区域
        return self.rect
