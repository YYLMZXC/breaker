# 游戏窗口的大小
GAME_SIZE = (800, 600)
# 玩家的宽度
PLAYER_SIZE_W = 96
# 玩家的高度
PLAYER_SIZE_H = 128
# 精灵的宽度
SPRITE_SIZE_W = 40
# 精灵的高度
SPRITE_SIZE_H = 40

# 玩家的资源文件路径
PLAYER_RES = (
    'res/player/0.png',
    'res/player/1.png',
    'res/player/2.png',
    'res/player/3.png',
    'res/player/4.png',
    'res/player/5.png',
    'res/player/6.png',
)

# 球的资源文件路径
BALL_RES = "res/ball.png"
# 方块的资源文件路径格式
BLOCK_RES_FMT = "res/block/%d.png"

# 游戏结束的资源文件路径
GAME_OVER_RES = "res/lose.png"

class BlockType:
    # 空方块
    NULL = 0
    # 加速方块
    SPEED_UP = 1
    # 普通方块
    NORMAL = 2
    # 复制方块
    COPY = 3
    # 减速方块
    SPEED_DOWN = 6
    # 墙壁方块
    WALL = 9

class SoundRes:
    # 声音资源：JNTM
    JNTM = 'snd/jntm.WAV'
    # 声音资源：NGM
    NGM = 'snd/niganma.WAV'
