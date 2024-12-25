# 导入pygame库，用于游戏开发
import pygame
# 从pygame.locals模块导入所有常量，方便使用
from pygame.locals import *
# 从const模块导入所有内容，假设const模块包含一些常量定义
from const import *
# 从player模块导入所有内容，假设player模块包含玩家相关的逻辑
from player import *
# 从ball模块导入所有内容，假设ball模块包含球相关的逻辑
from ball import *
# 从level模块导入所有内容，假设level模块包含关卡相关的逻辑
from level import *
# 从block模块导入所有内容，假设block模块包含方块相关的逻辑
from block import *




class Game(object):
    def __init__(self, surface):
        # 初始化pygame的混音器模块
        pygame.mixer.init()
        # 设置游戏窗口的表面对象
        self.surface = surface
        # 加载第一关
        self.Load(1)


    
    def Load(self, lv):#默认加载第一关
        # 创建一个Level对象，传入关卡编号
        self.level = Level(lv)
        # 设置游戏未结束
        self.isGameOver = False
        # 清空球的列表
        self.balls = []
        # 加载玩家
        self.loadPlayer()
        # 加载一个球
        #self.player.GetRect().x：这是玩家对象（self.player）的矩形区域的 x 坐标，即玩家在屏幕上的水平位置
        # self.player.GetRect().y - SPRITE_SIZE_H - 5：这是玩家对象的矩形区域的 y 坐标减去一个固定的值，
        # 即玩家在屏幕上的垂直位置减去一个固定的高度减去一个固定的偏移量。
        #- 5 是一个额外的偏移量，它将球的初始位置稍微向上移动了一点，
        # 这样球在开始时就不会完全与玩家的顶部边缘对齐，而是稍微高出一点。
        #至于 1, -1 这两个参数，它们分别代表了球在水平和垂直方向上的初始速度。
        # 1 表示球在水平方向上向右移动的速度，-1 表示球在垂直方向上向上移动的速度。这里的速度值是相对于游戏窗口的坐标系统而言的
        self.loadOneBall(self.player.GetRect().x, self.player.GetRect().y - SPRITE_SIZE_H - 5, 1, -1)
        # 加载方块的图像
        self.loadBlockImages()
    
    def loadPlayer(self):
        # 创建一个Player对象，传入玩家的资源文件路径、初始位置和移动范围
        self.player = Player(
            PLAYER_RES, 
            (GAME_SIZE[0] - PLAYER_SIZE_W)/2, GAME_SIZE[1] - PLAYER_SIZE_H, 
            SPRITE_SIZE_W, GAME_SIZE[0] - PLAYER_SIZE_W - SPRITE_SIZE_W)
    
    def loadOneBall(self, x, y, dirX, dirY):
        # 创建一个Ball对象，传入球的资源文件路径、初始位置和初始速度
        ball = Ball(BALL_RES, x, y, dirX, dirY)
        # 将球添加到球的列表中
        self.balls.append(ball)

    def loadBlockImages(self):
        # 清空方块的列表
        self.blocks = []
        # 遍历关卡中的所有方块
        for block in self.level.GetBlocks():
            # 创建一个Block对象，传入方块的类型、行索引、列索引和相对位置
            sp = Block(block[2], block[0], block[1], (0, 0))
            # 将方块添加到方块的列表中
            self.blocks.append(sp)
    
    def update(self):
      #v001
        # 如果游戏结束，直接返回
        if self.isGameOver:
             # 处理游戏结束时的事件
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if self.restart_button_rect.collidepoint(event.pos):
                        self.reset()
            return
        
        # 更新玩家的状态
        self.player.update()
        # 更新所有球的状态
        [ball.update() for ball in self.balls]
        # 检查碰撞
        self.checkCollide()
        # 如果游戏胜利，加载下一关
        if self.isGameWin():
            self.Load( self.level.level + 1 )




    def draw(self):
        # 如果游戏结束，绘制游戏结束的画面
        if self.isGameOver:
            #img = pygame.image.load(GAME_OVER_RES)
            #self.surface.blit(img, img.get_rect())
            self.draw_game_over()
            return 
        # 绘制玩家
        self.player.draw(self.surface)
        # 绘制所有方块
        [block.draw(self.surface) for block in self.blocks]
        # 绘制所有球
        [ball.draw(self.surface) for ball in self.balls]

    def draw_game_over(self):
        # 绘制游戏结束画面
        img = pygame.image.load(GAME_OVER_RES)
        self.surface.blit(img, img.get_rect())
        
       

#v001
    def reset(self):
        # 重新加载当前关卡
        self.Load(self.level.level)
# 重置游戏状态
        self.isGameOver = False


    def checkBallBlockCollide(self):
        
        # 遍历所有球
        for ball in self.balls:
            # 遍历所有方块
            for block in self.blocks:
                # 如果球与方块发生碰撞
                if ball.GetRect().colliderect( block.GetRect() ):
                    # 改变球的方向
                    ball.changeDirection( block.GetRect() )
                    # 处理方块
                    self.processBlock(ball, block)
                    # 跳出内层循环
                    break




    def processBlock(self, ball, block):
      
        # 如果方块的类型是复制
        if block.GetBlockType() == BlockType.COPY:
            # 复制球
            self.copyBalls()
        # 如果方块的类型是加速
        if block.GetBlockType() == BlockType.SPEED_UP:
            # 设置球的速度为1.5
            ball.SetSpeed(1.5)
        # 如果方块的类型是减速
        if block.GetBlockType() == BlockType.SPEED_DOWN:
            # 设置球的速度为0.2
            ball.SetSpeed(0.2)
        # 如果方块的类型是墙壁
        if block.GetBlockType() == BlockType.WALL:
            # 直接返回
            return
        # 从方块的列表中移除方块
        self.blocks.remove(block)
 
    def checkBallPlayerCollide(self):
      
        # 遍历所有球
        for ball in self.balls:
            # 如果球与玩家发生碰撞
            if ball.GetRect().colliderect( self.player.GetRect() ):
                # 改变球的y方向
                ball.changeYDirection( self.player.GetRect() )
                # 跳出循环
                break

    def checkCollide(self):
       
        # 检查球与方块的碰撞
        self.checkBallBlockCollide()
        # 检查球与玩家的碰撞
        self.checkBallPlayerCollide()

        # 设置标志位为True
        flag = True
        # 当标志位为True时，循环执行
        while flag:
            # 设置标志位为False
            flag = False
            # 遍历所有球
            for ball in self.balls:
                # 如果球的y坐标大于游戏窗口的高度
                if ball.GetRect().y > GAME_SIZE[1]:
                    # 从球的列表中移除球
                    self.balls.remove(ball)
                    # 设置标志位为True
                    flag = True
                    # 跳出循环
                    break
        # 如果球的列表为空
        if len(self.balls) == 0:
            # 设置游戏结束
            self.isGameOver = True
    
    def copyBalls(self):
        
        # 获取当前所有球的列表
        balls = [ball for ball in self.balls]
        # 遍历所有球
        for ball in balls:
            # 加载一个新的球
            self.loadOneBall(ball.GetRect().x, ball.GetRect().y, 1, -1)

    def isGameWin(self):
       
        # 遍历所有方块
        for block in self.blocks:
            # 如果方块的类型不是墙壁
            if block.GetBlockType() != BlockType.WALL:
                # 返回False
                return False
        # 返回True
        return True
