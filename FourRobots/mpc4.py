#单机器人核心代码(mpc4)

_2dmap = [] #地图数组
_adjacent = []#相邻八个节点，先添加左下右上节点，再添加左上、左下、右下、右上节点
start = None #起始点
end = None #终止点
open_list = {} #开启列表，包含待检查方格的列表
close_list = {} #关闭列表，保存所有不需要再次检查的方格
close_list2 = {}
block_list = {} #障碍物列表
map_border = () #地图尺寸
remove = []
path4 = []
flag = 0
flag2 = 0

class Node:
    def __init__(this, father, row, col):#row 表示行，col 表示列
        #if row < 0 or row >= map_border[0] or col < 0 or col >= map_border[1]:
            #raise Exception("node position can't beyond the border!")
        this.father = father
        this.row = row
        this.col = col
        if father != None:
            this.G = calc_G(father, this)
            this.H = calc_H(this, end)
            this.F = this.G + this.H
        else:
            this.G = 0
            this.H = 0
            this.F = 0

#计算 G 值
def calc_G(node1, node2):
    x1 = abs(node1.row - node2.row)
    y1 = abs(node1.col - node2.col)
    if (x1 == 1 and y1 == 0): # 左右邻接点
        return 10 # same row
    if (x1 == 0 and y1 == 1): # 上下邻接点
        return 10 # same col
    if (x1 == 1 and y1 == 1): # 对角线点
        return 14 # cross
    else:
        return 0

#计算 H 值
def calc_H(cur, end):
    return abs(end.row - cur.row) * 10 + abs(end.col - cur.col) * 10

#添加相邻八个节点
def addAdjacentIntoOpen(node):
# 相邻节点要注意边界的情况
    _adjacent = []#初始化为空集
    try:
        _adjacent.append(Node(node , node.row , node.col - 1)) #第一个元素代表父节点
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.row + 1 , node.col ))
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.row , node.col + 1))
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.row - 1 , node.col))
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.row - 1 , node.col - 1))
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.row+1 , node.col - 1))
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.row + 1 , node.col + 1))
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.row - 1 , node.col + 1))
    except Exception as e:
        pass
    return _adjacent

#相邻节点 F 值从高到低排列
def sel_sort(_adjacent):
    for i in range(len(_adjacent)-1,-1,-1):
        min_j = i
        for j in range(i-1,-1,-1):
            if _adjacent[j].F < _adjacent[min_j].F:min_j = j
        _adjacent[i],_adjacent[min_j] = _adjacent[min_j],_adjacent[i]
    for i in range(len(_adjacent) - 1, -1, -1):
        print("row1,col,F", _adjacent[i].row, _adjacent[i].col, _adjacent[i].F)

#每次预测两步
def predictr(node,_2dmap):#该代码表示向右，则向左，向上，向下同理可知
    try:
        if ((_2dmap[node.row][node.col + 1] == '0') and (_2dmap[node.row][node.col +2] == '0' or _2dmap[node.row][node.col + 2] == '1' or _2dmap[node.row][node.col + 2] =='5' or _2dmap[node.row][node.col + 2] == '3' or _2dmap[node.row][node.col + 2] == '8')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或其他机器人的当前位置或Rk的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_2dmap[node.row][node.col + 1] == '8'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_2dmap[node.row][node.col + 1] == '9' or _2dmap[node.row][node.col + 2] == '9' or _2dmap[node.row][node.col + 1] == '2' or _2dmap[node.row][node.col + 1] == '6' or _2dmap[node.row][node.col + 1] == '4'):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictl(node,_2dmap):#该代码表示向左
    try:
        if ((_2dmap[node.row][node.col - 1] == '0') and (_2dmap[node.row][node.col -2] == '0' or _2dmap[node.row][node.col - 2] == '1' or _2dmap[node.row][node.col - 2] =='5' or _2dmap[node.row][node.col - 2] == '3' or _2dmap[node.row][node.col - 2] == '8')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或其他机器人的当前位置或Rk的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_2dmap[node.row][node.col - 1] == '8'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_2dmap[node.row][node.col - 1] == '9' or _2dmap[node.row][node.col - 2] == '9' or _2dmap[node.row][node.col - 1] == '2' or _2dmap[node.row][node.col - 1] == '6' or _2dmap[node.row][node.col - 1] == '4'):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictu(node,_2dmap):#该代码表示向上
    try:
        if ((_2dmap[node.row - 1][node.col] == '0') and (_2dmap[node.row -2][node.col] == '0' or _2dmap[node.row - 2][node.col] == '1' or _2dmap[node.row - 2][node.col] =='5' or _2dmap[node.row - 2][node.col] == '3' or _2dmap[node.row - 2][node.col] == '8')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或其他机器人的当前位置或Rk的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_2dmap[node.row - 1][node.col] == '8'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_2dmap[node.row - 1][node.col] == '9' or _2dmap[node.row - 2][node.col] == '9' or _2dmap[node.row - 1][node.col] == '2' or _2dmap[node.row - 1][node.col] == '6' or _2dmap[node.row - 1][node.col] == '4'):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictd(node,_2dmap):#该代码表示向下
    try:
        if ((_2dmap[node.row + 1][node.col] == '0') and (_2dmap[node.row +2][node.col] == '0' or _2dmap[node.row + 2][node.col] == '1' or _2dmap[node.row + 2][node.col] =='5' or _2dmap[node.row + 2][node.col] == '3' or _2dmap[node.row + 2][node.col] == '8')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或其他机器人的当前位置或Rk的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_2dmap[node.row + 1][node.col] == '8'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_2dmap[node.row + 1][node.col] == '9' or _2dmap[node.row + 2][node.col] == '9' or _2dmap[node.row + 1][node.col] == '2' or _2dmap[node.row + 1][node.col] == '6' or _2dmap[node.row + 1][node.col] == '4'):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def updater(node,_2dmap): #该代码表示向右，则向左，向上，向下同理可知
    _2dmap[node.row][node.col] = '0' # 更新起始状态坐标
    node.row = node.row
    node.col = node.col + 1
    _2dmap[node.row][node.col] = '7' # 更新起始状态坐标
    path4.append((node.row, node.col))
    return path4

def updatel(node,_2dmap): #该代码表示向左
    _2dmap[node.row][node.col] = '0' # 更新起始状态坐标
    node.row = node.row
    node.col = node.col - 1
    _2dmap[node.row][node.col] = '7' # 更新起始状态坐标
    path4.append((node.row, node.col))
    return path4
    
def updateu(node,_2dmap): #该代码表示向上
    _2dmap[node.row][node.col] = '0' # 更新起始状态坐标
    node.row = node.row - 1
    node.col = node.col 
    _2dmap[node.row][node.col] = '7' # 更新起始状态坐标
    path4.append((node.row, node.col))
    return path4

def updated(node,_2dmap): #该代码表示向下
    _2dmap[node.row][node.col] = '0' # 更新起始状态坐标
    node.row = node.row + 1
    node.col = node.col 
    _2dmap[node.row][node.col] = '7' # 更新起始状态坐标
    path4.append((node.row, node.col))
    return path4

def predictrd(node,_2dmap): #该代码表示向右下，则向右上，向左下，向左上同理
    try:
        if (_2dmap[node.row + 1][node.col + 1] == '0' and (_2dmap[node.row + 2][node.col + 2] == '0' or _2dmap[node.row + 2][node.col + 2] == '1' or _2dmap[node.row + 2][node.col + 2] == '5' or _2dmap[node.row + 2][node.col + 2] == '3' or _2dmap[node.row + 2][node.col + 2] == '8')):
            flag2 = 0
            if (_2dmap[node.row][node.col + 1] == '9' or _2dmap[node.row + 1][node.col] == '9' or _2dmap[node.row][node.col + 1] == '2' or _2dmap[node.row + 1][node.col] == '2' or _2dmap[node.row][node.col + 1] == '6' or _2dmap[node.row + 1][node.col]== '6' or _2dmap[node.row][node.col + 1] == '4' or _2dmap[node.row + 1][node.col] == '4'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_2dmap[node.row + 1][node.col + 1] == '8'):
            flag2 = 0
            if (_2dmap[node.row][node.col + 1] == '9' or _2dmap[node.row + 1][node.col] == '9' or _2dmap[node.row][node.col + 1] == '2' or _2dmap[node.row + 1][node.col] == '2' or _2dmap[node.row][node.col + 1] == '6' or _2dmap[node.row + 1][node.col] == '6' or _2dmap[node.row][node.col + 1] == '4' or _2dmap[node.row + 1][node.col] == '4'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_2dmap[node.row + 1][node.col + 1] == '9' or _2dmap[node.row + 2][node.col + 2] == '9' or _2dmap[node.row + 1][node.col + 1] == '2' or _2dmap[node.row + 1][node.col + 1] == '6' or _2dmap[node.row + 1][node.col + 1] == '4'):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictru(node,_2dmap): #该代码表示向右上
    try:
        if (_2dmap[node.row - 1][node.col + 1] == '0' and (_2dmap[node.row - 2][node.col + 2] == '0' or _2dmap[node.row - 2][node.col + 2] == '1' or _2dmap[node.row - 2][node.col + 2] == '5' or _2dmap[node.row - 2][node.col + 2] == '3' or _2dmap[node.row - 2][node.col + 2] == '8')):
            flag2 = 0
            if (_2dmap[node.row][node.col + 1] == '9' or _2dmap[node.row - 1][node.col] == '9' or _2dmap[node.row][node.col + 1] == '2' or _2dmap[node.row - 1][node.col] == '2' or _2dmap[node.row][node.col + 1] == '6' or _2dmap[node.row - 1][node.col]== '6' or _2dmap[node.row][node.col + 1] == '4' or _2dmap[node.row - 1][node.col] == '4'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_2dmap[node.row - 1][node.col + 1] == '8'):
            flag2 = 0
            if (_2dmap[node.row][node.col + 1] == '9' or _2dmap[node.row - 1][node.col] == '9' or _2dmap[node.row][node.col + 1] == '2' or _2dmap[node.row - 1][node.col] == '2' or _2dmap[node.row][node.col + 1] == '6' or _2dmap[node.row - 1][node.col] == '6' or _2dmap[node.row][node.col + 1] == '4' or _2dmap[node.row - 1][node.col] == '4'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_2dmap[node.row - 1][node.col + 1] == '9' or _2dmap[node.row - 2][node.col + 2] == '9' or _2dmap[node.row - 1][node.col + 1] == '2' or _2dmap[node.row - 1][node.col + 1] == '6' or _2dmap[node.row - 1][node.col + 1] == '4'):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictld(node,_2dmap): #该代码表示向左下
    try:
        if (_2dmap[node.row + 1][node.col - 1] == '0' and (_2dmap[node.row + 2][node.col - 2] == '0' or _2dmap[node.row + 2][node.col - 2] == '1' or _2dmap[node.row + 2][node.col - 2] == '5' or _2dmap[node.row + 2][node.col - 2] == '3' or _2dmap[node.row + 2][node.col - 2] == '8')):
            flag2 = 0
            if (_2dmap[node.row][node.col - 1] == '9' or _2dmap[node.row + 1][node.col] == '9' or _2dmap[node.row][node.col - 1] == '2' or _2dmap[node.row + 1][node.col] == '2' or _2dmap[node.row][node.col - 1] == '6' or _2dmap[node.row + 1][node.col]== '6' or _2dmap[node.row][node.col - 1] == '4' or _2dmap[node.row + 1][node.col] == '4'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_2dmap[node.row + 1][node.col - 1] == '8'):
            flag2 = 0
            if (_2dmap[node.row][node.col - 1] == '9' or _2dmap[node.row + 1][node.col] == '9' or _2dmap[node.row][node.col - 1] == '2' or _2dmap[node.row + 1][node.col] == '2' or _2dmap[node.row][node.col - 1] == '6' or _2dmap[node.row + 1][node.col] == '6' or _2dmap[node.row][node.col - 1] == '4' or _2dmap[node.row + 1][node.col] == '4'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_2dmap[node.row + 1][node.col - 1] == '9' or _2dmap[node.row + 2][node.col - 2] == '9' or _2dmap[node.row + 1][node.col - 1] == '2' or _2dmap[node.row + 1][node.col - 1] == '6' or _2dmap[node.row + 1][node.col - 1] == '4'):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictlu(node,_2dmap): #该代码表示向左上
    try:
        if (_2dmap[node.row - 1][node.col - 1] == '0' and (_2dmap[node.row - 2][node.col - 2] == '0' or _2dmap[node.row - 2][node.col - 2] == '1' or _2dmap[node.row - 2][node.col - 2] == '5' or _2dmap[node.row - 2][node.col - 2] == '3' or _2dmap[node.row - 2][node.col - 2] == '8')):
            flag2 = 0
            if (_2dmap[node.row][node.col - 1] == '9' or _2dmap[node.row - 1][node.col] == '9' or _2dmap[node.row][node.col - 1] == '2' or _2dmap[node.row - 1][node.col] == '2' or _2dmap[node.row][node.col - 1] == '6' or _2dmap[node.row - 1][node.col]== '6' or _2dmap[node.row][node.col - 1] == '4' or _2dmap[node.row - 1][node.col] == '4'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_2dmap[node.row - 1][node.col - 1] == '8'):
            flag2 = 0
            if (_2dmap[node.row][node.col - 1] == '9' or _2dmap[node.row - 1][node.col] == '9' or _2dmap[node.row][node.col - 1] == '2' or _2dmap[node.row - 1][node.col] == '2' or _2dmap[node.row][node.col - 1] == '6' or _2dmap[node.row - 1][node.col] == '6' or _2dmap[node.row][node.col - 1] == '4' or _2dmap[node.row - 1][node.col] == '4'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_2dmap[node.row - 1][node.col - 1] == '9' or _2dmap[node.row - 2][node.col - 2] == '9' or _2dmap[node.row - 1][node.col - 1] == '2' or _2dmap[node.row - 1][node.col - 1] == '6' or _2dmap[node.row - 1][node.col - 1] == '4'):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def updaterd(node,_2dmap): #该代码表示向右下，则向右上，向左下，向左上同理
    _2dmap[node.row][node.col] = '0' # 更新起始状态坐标
    node.row = node.row + 1
    node.col = node.col + 1
    _2dmap[node.row][node.col] = '7' # 更新起始状态坐标
    path4.append((node.row, node.col))
    return path4

def updateru(node,_2dmap): #该代码表示向右上
    _2dmap[node.row][node.col] = '0' # 更新起始状态坐标
    node.row = node.row - 1
    node.col = node.col + 1
    _2dmap[node.row][node.col] = '7' # 更新起始状态坐标
    path4.append((node.row, node.col))
    return path4

def updateld(node,_2dmap): #该代码表示向左下
    _2dmap[node.row][node.col] = '0' # 更新起始状态坐标
    node.row = node.row + 1
    node.col = node.col - 1
    _2dmap[node.row][node.col] = '7' # 更新起始状态坐标
    path4.append((node.row, node.col))
    return path4

def updatelu(node,_2dmap): #该代码表示向左上
    _2dmap[node.row][node.col] = '0' # 更新起始状态坐标
    node.row = node.row - 1
    node.col = node.col - 1
    _2dmap[node.row][node.col] = '7' # 更新起始状态坐标
    path4.append((node.row, node.col))
    return path4

def preset_map():
    global map_border
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())        
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 3 0 1 0 9 9 0 0 4 0 2 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 5 0 7 0 0 0 0 0 6 0 8 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    _2dmap.append('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split())
    map_border = (len(_2dmap),len(_2dmap[0]))
    return _2dmap

def preset_se4(_2dmap):
    global start, end
    row_index = 0 # 行索引
    for roww in _2dmap: # row 表示_2dmap 中的每一行
        col_index = 0
        for n in roww: # n 表示一行中的各个元素
            if n == '7':
                start = Node(None, row_index, col_index) # 添加起始点坐标
                close_list[(start.row, start.col)] = start
            elif n == '8':
                end = Node(None, row_index, col_index) # 添加终止点坐标
            col_index = col_index + 1
        row_index = row_index + 1
    path4.append((start.row, start.col))
    return start,close_list,path4