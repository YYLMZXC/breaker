class Level(object):
    def __init__(self, level):
     
        # 初始化方块列表
        self.blocks = []
        # 设置关卡编号
        self.level = level
        # 打开关卡文件
        with open ('data/level/' + str(self.level) + '.x', 'r') as f:
            # 初始化行索引
            r = 0
            # 遍历文件中的每一行
            for line in f.readlines():
                # 获取当前行的列数
                col = len(line)
                # 遍历当前行的每一列
                for c in range(col - 1):
                    # 如果当前列的字符不是'0'
                    if line[c] != '0':
                        # 将当前方块的信息添加到方块列表中
                        self.blocks.append(  (r, c, int(line[c])) )
                # 行索引加1
                r += 1
                
    def GetBlocks(self):
    
        # 返回方块列表
        return self.blocks
