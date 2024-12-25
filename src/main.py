# 导入pygame库，用于游戏开发
import pygame, sys
#Pygame是一组用于编写游戏的Python模块。它基于优秀的SDL库编写。
# 这使得您可以使用Python语言创建功能齐全的游戏和多媒体程序。
# 该软件包具有高度的可移植性，游戏可以在Windows、MacOS、OS X、BeOS、FreeBSD、IRIX和Linux上运行。
# 从pygame.locals模块导入所有常量，方便使用
#
from pygame.locals import *
# 从game模块导入所有内容，假设game模块包含游戏的主要逻辑，在模块的本地命名空间中拥有一组来自Pygame的方便函数。
from game import *
# 从const模块导入所有内容，假设const模块包含一些常量定义
from const import *





# 初始化pygame
pygame.init()
# 设置游戏窗口的大小为GAME_SIZE
DISPLAYSURF = pygame.display.set_mode(GAME_SIZE)
# 创建一个Game对象，传入游戏窗口对象
game = Game(DISPLAYSURF)



# 游戏主循环
while True:
    # 遍历所有事件
    for event in pygame.event.get():
        # 如果事件类型是QUIT（即用户点击了关闭按钮）
        if event.type == QUIT:
            # 退出pygame
            pygame.quit()
            # 退出程序
            sys.exit()
 # 处理重来事件
        elif event.type == KEYDOWN:
            if event.key == K_r:  # 如果按下R键
                game.reset()  # 重置游戏状态


    # 更新游戏状态
    game.update()
    # 填充游戏窗口为白色
    DISPLAYSURF.fill( (255, 255, 255) )
    # 绘制游戏画面
    game.draw()
    # 更新游戏窗口显示
    pygame.display.update()

    """注释 """
    """注释 """
    



'''
初始化：
导入必要的模块和库，包括 pygame、sys、pygame.locals、game 和 const。
初始化 pygame 和 pygame.mixer，设置游戏窗口的大小为 GAME_SIZE。
创建一个 Game 对象，传入游戏窗口对象。
游戏主循环：
游戏主循环是一个无限循环，用于不断更新游戏状态和绘制游戏画面。
在每次循环中，首先处理游戏事件，如用户点击关闭按钮时退出游戏。
然后更新游戏状态，调用 game.update() 方法。
填充游戏窗口为白色，调用 DISPLAYSURF.fill((255, 255, 255))。
绘制游戏画面，调用 game.draw() 方法。
更新游戏窗口显示，调用 pygame.display.update()。
游戏结束：
当游戏结束时（例如，玩家完成所有关卡或达到失败条件），循环结束，程序退出。
这种设计模式是游戏开发中常见的结构，称为“游戏循环”。游戏循环负责处理游戏的核心逻辑，
包括输入处理、更新游戏状态、渲染画面等。通过不断循环，游戏能够实时响应用户输入，并保持画面的流畅更新。
总结来说，main.py 的运行逻辑是为了创建一个游戏窗口，初始化游戏环境，然后进入一个无限循环，
不断更新游戏状态和绘制游戏画面，直到游戏结束。
'''