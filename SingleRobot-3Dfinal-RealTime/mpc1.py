#单机器人核心代码(mpc1)


_3dmap = [] #地图数组
_adjacent = []#相邻26个节点，分三层，按照最下层，中间层，最上层的顺序添加方格；每层先添加中间节点（中间层没有），再添加左下右上节点，再添加左上、左下、右下、右上节点
start = None #起始点
end = None #终止点
open_list = {} #开启列表，包含待检查方格的列表
close_list = {} #关闭列表，保存所有不需要再次检查的方格
close_list2 = {}
block_list = {} #障碍物列表
map_border = () #地图尺寸
remove = []
path1 = []
flag = 0
flag2 = 0

class Node:
    def __init__(this, father, x, y, z):#row 表示行，col 表示列
        if x < 0 or x >= map_border[0] or y < 0 or y >= map_border[1] or z < 0 or z >= map_border[2]:
            raise Exception("node position can't beyond the border!")
        this.father = father
        this.x = x
        this.y = y
        this.z = z
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
    x1 = abs(node1.x - node2.x)
    y1 = abs(node1.y - node2.y)
    z1 = abs(node1.z - node2.z)
    if (x1 == 1 and y1 == 0 and z1 == 0): # 左右邻接点
        return 10 # same row
    if (x1 == 0 and y1 == 1 and z1 == 0): # 上下邻接点
        return 10 # same col
    if (x1 == 0 and y1 == 0 and z1 == 1): # 前后邻接点
        return 10 # same col
        
    if (x1 == 1 and y1 == 1 and z1 == 0): # 对角线点
        return 14 # cross
    if (x1 == 1 and y1 == 0 and z1 == 1): # 对角线点
        return 14 # cross
    if (x1 == 0 and y1 == 1 and z1 == 1): # 对角线点
        return 14 # cross
    
    if (x1 == 1 and y1 == 1 and z1 == 1): # 斜对角线点
        return 17 # cross
       
    else:
        return 0

#计算 H 值
def calc_H(cur, end):
    return abs(end.x - cur.x) * 10 + abs(end.y - cur.y) * 10 + abs(end.z - cur.z) * 10

#添加相邻26个节点
def addAdjacentIntoOpen(node):
# 相邻节点要注意边界的情况
    _adjacent = []#初始化为空集
    try:
        _adjacent.append(Node(node , node.x, node.y - 1, node.z)) #最下层中间节点，第一个元素代表父节点
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y - 1, node.z)) #最下层左
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x, node.y - 1, node.z + 1)) #最下层下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y - 1, node.z)) #最下层右
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x, node.y - 1, node.z - 1)) #最下层上
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y - 1, node.z - 1)) #最下层左上
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y - 1, node.z + 1)) #最下层左下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y - 1, node.z + 1)) #最下层右下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y - 1, node.z - 1)) #最下层右上
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y, node.z)) #中间层左
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x, node.y, node.z + 1)) #中间层下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y, node.z)) #中间层右
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x, node.y, node.z - 1)) #中间层上
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y, node.z - 1)) #中间层左上
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y, node.z + 1)) #中间层左下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y, node.z + 1)) #中间层右下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y, node.z - 1)) #中间层右上
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x, node.y + 1, node.z)) #最上层中间节点
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y + 1, node.z)) #最上层左
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x, node.y + 1, node.z + 1)) #最上层下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y + 1, node.z)) #最上层右
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x, node.y + 1, node.z - 1)) #最上层上
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y + 1, node.z - 1)) #最上层左上
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x - 1, node.y + 1, node.z + 1)) #最上层左下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y + 1, node.z + 1)) #最上层右下
    except Exception as e:
        pass
    try:
        _adjacent.append(Node(node , node.x + 1, node.y + 1, node.z - 1)) #最上层右上
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
        print("x,y,z,F", _adjacent[i].x, _adjacent[i].y,_adjacent[i].z, _adjacent[i].F)

#每次预测两步,最下层
def predictbm(node,_3dmap):#该代码表示向最下层中间节点
    try:
        if ((_3dmap[node.x][node.y - 1][node.z] == '0') and (_3dmap[node.x][node.y - 2][node.z] == '0' or _3dmap[node.x][node.y - 2][node.z] == '2')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或R1的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_3dmap[node.x][node.y - 1][node.z] == '2'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 2][node.z] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictbr(node,_3dmap):#该代码表示向最下层右节点
    try:
        if ((_3dmap[node.x + 1][node.y - 1][node.z] == '0') and (_3dmap[node.x + 2][node.y - 2][node.z] == '0' or _3dmap[node.x + 2][node.y - 2][node.z] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y - 1][node.z] == '2'):   #下一步为目标点
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y - 1][node.z] == '9' or _3dmap[node.x + 2][node.y - 2][node.z] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictbl(node,_3dmap):#该代码表示最下层向左
    try:
        if ((_3dmap[node.x - 1][node.y - 1][node.z] == '0') and (_3dmap[node.x - 2][node.y - 2][node.z] == '0' or _3dmap[node.x - 2][node.y - 2][node.z] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y - 1][node.z] == '2'):   #下一步为目标点
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y - 1][node.z] == '9' or _3dmap[node.x - 2][node.y - 2][node.z] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictbu(node,_3dmap):#该代码表示最下层向上
    try:
        if ((_3dmap[node.x][node.y - 1][node.z - 1] == '0') and (_3dmap[node.x][node.y - 2][node.z - 2] == '0' or _3dmap[node.x][node.y - 2][node.z - 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x][node.y - 1][node.z - 1] == '2'):   #下一步为目标点
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x][node.y - 1][node.z - 1] == '9' or _3dmap[node.x][node.y - 2][node.z - 2] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictbd(node,_3dmap):#该代码表示最下层向下
    try:
        if ((_3dmap[node.x][node.y - 1][node.z + 1] == '0') and (_3dmap[node.x][node.y - 2][node.z + 2] == '0' or _3dmap[node.x][node.y - 2][node.z + 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x][node.y - 1][node.z + 1] == '2'):   #下一步为目标点
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x][node.y - 1][node.z + 1] == '9' or _3dmap[node.x][node.y - 2][node.z + 2] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def updatebm(node,_3dmap): #该代码表示最下层中间节点
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x
    node.y = node.y - 1
    node.z = node.z
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatebr(node,_3dmap): #该代码表示最下层向右，则向左，向上，向下同理可知
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y - 1
    node.z = node.z
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatebl(node,_3dmap): #该代码表示最下层向左
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y - 1
    node.z = node.z
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1
    
def updatebu(node,_3dmap): #该代码表示最下层向上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x
    node.y = node.y - 1
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatebd(node,_3dmap): #该代码表示最下层向下
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x
    node.y = node.y - 1
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def predictbrd(node,_3dmap): #该代码表示最下层向右下，则向右上，向左下，向左上同理
    try:
        if (_3dmap[node.x + 1][node.y - 1][node.z + 1] == '0' and (_3dmap[node.x + 2][node.y - 2][node.z + 2] == '0' or _3dmap[node.x + 2][node.y - 2][node.z + 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 1][node.z + 1] == '9' or _3dmap[node.x + 1][node.y - 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x + 1][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y - 1][node.z + 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 1][node.z + 1] == '9' or _3dmap[node.x + 1][node.y - 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x + 1][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x + 1][node.y - 1][node.z + 1] == '9' or _3dmap[node.x + 2][node.y - 2][node.z + 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictbru(node,_3dmap): #该代码表示最下层向右上
    try:
        if (_3dmap[node.x + 1][node.y - 1][node.z - 1] == '0' and (_3dmap[node.x + 2][node.y - 2][node.z - 2] == '0' or _3dmap[node.x + 2][node.y - 2][node.z - 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 1][node.z - 1] == '9' or _3dmap[node.x + 1][node.y - 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x + 1][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y - 1][node.z - 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 1][node.z - 1] == '9' or _3dmap[node.x + 1][node.y - 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x + 1][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x + 1][node.y - 1][node.z - 1] == '9' or _3dmap[node.x + 2][node.y - 2][node.z - 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictbld(node,_3dmap): #该代码表示最下层向左下
    try:
        if (_3dmap[node.x - 1][node.y - 1][node.z + 1] == '0' and (_3dmap[node.x - 2][node.y - 2][node.z + 2] == '0' or _3dmap[node.x - 2][node.y - 2][node.z + 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 1][node.z + 1] == '9' or _3dmap[node.x - 1][node.y - 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x - 1][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y - 1][node.z + 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 1][node.z + 1] == '9' or _3dmap[node.x - 1][node.y - 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x - 1][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x - 1][node.y - 1][node.z + 1] == '9' or _3dmap[node.x - 2][node.y - 2][node.z + 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictblu(node,_3dmap): #该代码表示最下层向左上
    try:
        if (_3dmap[node.x - 1][node.y - 1][node.z - 1] == '0' and (_3dmap[node.x - 2][node.y - 2][node.z - 2] == '0' or _3dmap[node.x - 2][node.y - 2][node.z - 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 1][node.z - 1] == '9' or _3dmap[node.x - 1][node.y - 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x - 1][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y - 1][node.z - 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x][node.y - 1][node.z] == '9' or _3dmap[node.x][node.y - 1][node.z - 1] == '9' or _3dmap[node.x - 1][node.y - 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x - 1][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x - 1][node.y - 1][node.z - 1] == '9' or _3dmap[node.x - 2][node.y - 2][node.z - 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def updatebrd(node,_3dmap): #该代码表示最下层向右下，则向右上，向左下，向左上同理
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y - 1
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatebru(node,_3dmap): #该代码表示最下层向右上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y - 1
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatebld(node,_3dmap): #该代码表示最下层向左下
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y - 1
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updateblu(node,_3dmap): #该代码表示最下层向左上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y - 1
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

#每次预测两步,中间层
def predictmr(node,_3dmap):#该代码表示向中间层右节点
    try:
        if ((_3dmap[node.x + 1][node.y][node.z] == '0') and (_3dmap[node.x + 2][node.y][node.z] == '0' or _3dmap[node.x + 2][node.y][node.z] == '2')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或其他机器人的当前位置或Rk的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_3dmap[node.x + 1][node.y][node.z] == '2'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x + 2][node.y][node.z] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictml(node,_3dmap):#该代码表示中间层向左
    try:
        if ((_3dmap[node.x - 1][node.y][node.z] == '0') and (_3dmap[node.x - 2][node.y][node.z] == '0' or _3dmap[node.x - 2][node.y][node.z] == '2')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或其他机器人的当前位置或Rk的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_3dmap[node.x - 1][node.y][node.z] == '2'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x - 2][node.y][node.z] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictmu(node,_3dmap):#该代码表示中间层向上
    try:
        if ((_3dmap[node.x][node.y][node.z - 1] == '0') and (_3dmap[node.x][node.y][node.z - 2] == '0' or _3dmap[node.x][node.y][node.z - 2] == '2')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或R1的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_3dmap[node.x][node.y][node.z - 1] == '2'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x][node.y][node.z - 2] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictmd(node,_3dmap):#该代码表示中间层向下
    try:
        if ((_3dmap[node.x][node.y][node.z + 1] == '0') and (_3dmap[node.x][node.y][node.z + 2] == '0' or _3dmap[node.x][node.y][node.z + 2] == '2')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或R1的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_3dmap[node.x][node.y][node.z + 1] == '2'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x][node.y][node.z + 2] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def updatemr(node,_3dmap): #该代码表示中间层向右，则向左，向上，向下同理可知
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y
    node.z = node.z
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updateml(node,_3dmap): #该代码表示中间层向左
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y
    node.z = node.z
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1
    
def updatemu(node,_3dmap): #该代码表示中间层向上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x
    node.y = node.y
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatemd(node,_3dmap): #该代码表示中间层向下
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x
    node.y = node.y
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def predictmrd(node,_3dmap): #该代码表示中间层向右下，则向右上，向左下，向左上同理
    try:
        if (_3dmap[node.x + 1][node.y][node.z + 1] == '0' and (_3dmap[node.x + 2][node.y ][node.z + 2] == '0' or _3dmap[node.x + 2][node.y ][node.z + 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y][node.z + 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x + 1][node.y][node.z + 1] == '9' or _3dmap[node.x + 2][node.y][node.z + 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictmru(node,_3dmap): #该代码表示中间层向右上
    try:
        if (_3dmap[node.x + 1][node.y][node.z - 1] == '0' and (_3dmap[node.x + 2][node.y][node.z - 2] == '0' or _3dmap[node.x + 2][node.y][node.z - 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' ):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y][node.z - 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' ):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x + 1][node.y][node.z - 1] == '9' or _3dmap[node.x + 2][node.y][node.z - 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictmld(node,_3dmap): #该代码表示中间层向左下
    try:
        if (_3dmap[node.x - 1][node.y][node.z + 1] == '0' and (_3dmap[node.x - 2][node.y][node.z + 2] == '0' or _3dmap[node.x - 2][node.y][node.z + 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y][node.z + 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x - 1][node.y][node.z + 1] == '9' or _3dmap[node.x - 2][node.y][node.z + 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predictmlu(node,_3dmap): #该代码表示中间层向左上
    try:
        if (_3dmap[node.x - 1][node.y][node.z - 1] == '0' and (_3dmap[node.x - 2][node.y][node.z - 2] == '0' or _3dmap[node.x - 2][node.y][node.z - 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y][node.z - 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x - 1][node.y][node.z - 1] == '9' or _3dmap[node.x - 2][node.y][node.z - 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def updatemrd(node,_3dmap): #该代码表示中间层向右下，则向右上，向左下，向左上同理
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatemru(node,_3dmap): #该代码表示中间层向右上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y 
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatemld(node,_3dmap): #该代码表示中间层向左下
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatemlu(node,_3dmap): #该代码表示中间层向左上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y 
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

#每次预测两步,最上层
def predicttm(node,_3dmap):#该代码表示向最上层中间节点
    try:
        if ((_3dmap[node.x][node.y + 1][node.z] == '0') and (_3dmap[node.x][node.y + 2][node.z] == '0' or _3dmap[node.x][node.y + 2][node.z] == '2')):
            flag =0                         #下一步为空闲状态，并且下下一步为空闲状态或R1的目标点
            flag2 = 0
            return False, flag,flag2
        elif (_3dmap[node.x][node.y + 1][node.z] == '2'):   #下一步为目标点
            flag = 0
            flag2 = 0
            return True, flag,flag2
        elif (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 2][node.z] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predicttr(node,_3dmap):#该代码表示向最上层右节点
    try:
        if ((_3dmap[node.x + 1][node.y + 1][node.z] == '0') and (_3dmap[node.x + 2][node.y + 2][node.z] == '0' or _3dmap[node.x + 2][node.y + 2][node.z] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y + 1][node.z] == '2'):   #下一步为目标点
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x + 1][node.y + 1][node.z] == '9' or _3dmap[node.x + 2][node.y + 2][node.z] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predicttl(node,_3dmap):#该代码表示最上层向左
    try:
        if ((_3dmap[node.x - 1][node.y + 1][node.z] == '0') and (_3dmap[node.x - 2][node.y + 2][node.z] == '0' or _3dmap[node.x - 2][node.y + 2][node.z] == '2')):
            flag2 = 0
            if (_3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y + 1][node.z] == '2'):   #下一步为目标点
            flag2 = 0
            if (_3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y + 1][node.z] == '9' or _3dmap[node.x - 2][node.y + 2][node.z] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predicttu(node,_3dmap):#该代码表示最上层向上
    try:
        if ((_3dmap[node.x][node.y + 1][node.z - 1] == '0') and (_3dmap[node.x][node.y + 2][node.z - 2] == '0' or _3dmap[node.x][node.y + 2][node.z - 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x][node.y + 1][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x][node.y + 1][node.z - 1] == '2'):   #下一步为目标点
            flag2 = 0
            if (_3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x][node.y + 1][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x][node.y + 1][node.z - 1] == '9' or _3dmap[node.x][node.y + 2][node.z - 2] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predicttd(node,_3dmap):#该代码表示最上层向下
    try:
        if ((_3dmap[node.x][node.y + 1][node.z + 1] == '0') and (_3dmap[node.x][node.y + 2][node.z + 2] == '0' or _3dmap[node.x][node.y + 2][node.z + 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x][node.y + 1][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x][node.y + 1][node.z + 1] == '2'):   #下一步为目标点
            flag2 = 0
            if (_3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x][node.y + 1][node.z] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x][node.y + 1][node.z + 1] == '9' or _3dmap[node.x][node.y + 2][node.z + 2] == '9' ):
            flag = 1 #下个状态或下下个状态存在障碍物     下一步为障碍物或下下一步为障碍物或下一步为其他机器人的目标点
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def updatetm(node,_3dmap): #该代码表示最上层中间节点
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x
    node.y = node.y + 1
    node.z = node.z
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatetr(node,_3dmap): #该代码表示最上层向右，则向左，向上，向下同理可知
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y + 1
    node.z = node.z
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatetl(node,_3dmap): #该代码表示最上层向左
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y + 1
    node.z = node.z
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1
    
def updatetu(node,_3dmap): #该代码表示最上层向上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x
    node.y = node.y + 1
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatetd(node,_3dmap): #该代码表示最上层向下
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x
    node.y = node.y + 1
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def predicttrd(node,_3dmap): #该代码表示最上层向右下，则向右上，向左下，向左上同理
    try:
        if (_3dmap[node.x + 1][node.y + 1][node.z + 1] == '0' and (_3dmap[node.x + 2][node.y + 2][node.z + 2] == '0' or _3dmap[node.x + 2][node.y + 2][node.z + 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z + 1] == '9' or _3dmap[node.x + 1][node.y + 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x + 1][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y + 1][node.z + 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z + 1] == '9' or _3dmap[node.x + 1][node.y + 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x + 1][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x + 1][node.y + 1][node.z + 1] == '9' or _3dmap[node.x + 2][node.y + 2][node.z + 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predicttru(node,_3dmap): #该代码表示最上层向右上
    try:
        if (_3dmap[node.x + 1][node.y + 1][node.z - 1] == '0' and (_3dmap[node.x + 2][node.y + 2][node.z - 2] == '0' or _3dmap[node.x + 2][node.y + 2][node.z - 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z - 1] == '9' or _3dmap[node.x + 1][node.y + 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x + 1][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x + 1][node.y + 1][node.z - 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z - 1] == '9' or _3dmap[node.x + 1][node.y + 1][node.z] == '9' or _3dmap[node.x + 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x + 1][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x + 1][node.y + 1][node.z - 1] == '9' or _3dmap[node.x + 2][node.y + 2][node.z - 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predicttld(node,_3dmap): #该代码表示最上层向左下
    try:
        if (_3dmap[node.x - 1][node.y + 1][node.z + 1] == '0' and (_3dmap[node.x - 2][node.y + 2][node.z + 2] == '0' or _3dmap[node.x - 2][node.y + 2][node.z + 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z + 1] == '9' or _3dmap[node.x - 1][node.y + 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x - 1][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y + 1][node.z + 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z + 1] == '9' or _3dmap[node.x - 1][node.y + 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z + 1] == '9' or _3dmap[node.x - 1][node.y][node.z + 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x - 1][node.y + 1][node.z + 1] == '9' or _3dmap[node.x - 2][node.y + 2][node.z + 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def predicttlu(node,_3dmap): #该代码表示最上层向左上
    try:
        if (_3dmap[node.x - 1][node.y + 1][node.z - 1] == '0' and (_3dmap[node.x - 2][node.y + 2][node.z - 2] == '0' or _3dmap[node.x - 2][node.y + 2][node.z - 2] == '2')):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z - 1] == '9' or _3dmap[node.x - 1][node.y + 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x - 1][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return False,flag,flag2
        elif (_3dmap[node.x - 1][node.y + 1][node.z - 1] == '2'):
            flag2 = 0
            if (_3dmap[node.x][node.y + 1][node.z] == '9' or _3dmap[node.x][node.y + 1][node.z - 1] == '9' or _3dmap[node.x - 1][node.y + 1][node.z] == '9' or _3dmap[node.x - 1][node.y][node.z] == '9' or _3dmap[node.x][node.y][node.z - 1] == '9' or _3dmap[node.x - 1][node.y][node.z - 1] == '9'):
                flag2 = 1
            else:
                pass
            flag = 0
            return True,flag,flag2
        elif (_3dmap[node.x - 1][node.y + 1][node.z - 1] == '9' or _3dmap[node.x - 2][node.y + 2][node.z - 2] == '9' ):
            flag = 1
            flag2 = 0
            return False, flag,flag2
        else:
            flag = 0
            flag2 = 1
            return False, flag, flag2
    except Exception as e:
        pass

def updatetrd(node,_3dmap): #该代码表示最上层向右下，则向右上，向左下，向左上同理
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y + 1
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatetru(node,_3dmap): #该代码表示最上层向右上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x + 1
    node.y = node.y + 1
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatetld(node,_3dmap): #该代码表示最上层向左下
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y + 1
    node.z = node.z + 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def updatetlu(node,_3dmap): #该代码表示最上层向左上
    _3dmap[node.x][node.y][node.z] = '0' # 更新起始状态坐标
    node.x = node.x - 1
    node.y = node.y + 1
    node.z = node.z - 1
    _3dmap[node.x][node.y][node.z] = '1' # 更新起始状态坐标
    path1.append((node.x, node.y, node.z))
    return path1

def preset_map():
    global map_border
    
    #沿着x轴方向的7层分别由_3dmap1-_3dmap7共7个列表存储
    _3dmap1 = []
    _3dmap1.append('0 0 0 0 0 0 0'.split())
    _3dmap1.append('0 0 0 0 0 0 0'.split())
    _3dmap1.append('0 0 0 0 0 0 0'.split())
    _3dmap1.append('0 0 0 0 0 0 0'.split())
    _3dmap1.append('0 0 0 0 0 0 0'.split())
    _3dmap1.append('0 0 0 0 0 0 0'.split())
    _3dmap1.append('0 0 0 0 0 0 0'.split())
    _3dmap2 = []
    _3dmap2.append('0 0 0 0 0 0 0'.split())
    _3dmap2.append('0 0 0 1 0 0 0'.split())
    _3dmap2.append('0 0 0 0 0 0 0'.split())
    _3dmap2.append('0 0 0 0 0 0 0'.split())
    _3dmap2.append('0 0 0 0 0 0 0'.split())
    _3dmap2.append('0 0 0 0 0 0 0'.split())
    _3dmap2.append('0 0 0 0 0 0 0'.split())
    _3dmap3 = []
    _3dmap3.append('0 0 0 0 0 0 0'.split())
    _3dmap3.append('0 0 0 0 0 0 0'.split())
    _3dmap3.append('0 0 0 0 0 0 0'.split())
    _3dmap3.append('0 0 0 0 0 0 0'.split())
    _3dmap3.append('0 0 0 0 0 0 0'.split())
    _3dmap3.append('0 0 0 0 0 0 0'.split())
    _3dmap3.append('0 0 0 0 0 0 0'.split())
    _3dmap4 = []
    _3dmap4.append('0 0 0 0 0 0 0'.split())
    _3dmap4.append('0 0 0 0 0 0 0'.split())
    _3dmap4.append('0 0 0 0 0 0 0'.split())
    _3dmap4.append('0 0 9 9 9 0 0'.split())
    _3dmap4.append('0 0 0 0 0 0 0'.split())
    _3dmap4.append('0 0 0 0 0 0 0'.split())
    _3dmap4.append('0 0 0 0 0 0 0'.split())
    _3dmap5 = []
    _3dmap5.append('0 0 0 0 0 0 0'.split())
    _3dmap5.append('0 0 0 0 0 0 0'.split())
    _3dmap5.append('0 0 0 0 0 0 0'.split())
    _3dmap5.append('0 0 0 0 0 0 0'.split())
    _3dmap5.append('0 0 0 0 0 0 0'.split())
    _3dmap5.append('0 0 0 0 0 0 0'.split())
    _3dmap5.append('0 0 0 0 0 0 0'.split())
    _3dmap6 = []
    _3dmap6.append('0 0 0 0 0 0 0'.split())
    _3dmap6.append('0 0 0 0 0 0 0'.split())
    _3dmap6.append('0 0 0 0 0 0 0'.split())
    _3dmap6.append('0 0 0 0 0 0 0'.split())
    _3dmap6.append('0 0 0 0 0 0 0'.split())
    _3dmap6.append('0 0 0 2 0 0 0'.split())
    _3dmap6.append('0 0 0 0 0 0 0'.split())
    _3dmap7 = []
    _3dmap7.append('0 0 0 0 0 0 0'.split())
    _3dmap7.append('0 0 0 0 0 0 0'.split())
    _3dmap7.append('0 0 0 0 0 0 0'.split())
    _3dmap7.append('0 0 0 0 0 0 0'.split())
    _3dmap7.append('0 0 0 0 0 0 0'.split())
    _3dmap7.append('0 0 0 0 0 0 0'.split())
    _3dmap7.append('0 0 0 0 0 0 0'.split())
    
    _3dmap.append(_3dmap1)
    _3dmap.append(_3dmap2)
    _3dmap.append(_3dmap3)
    _3dmap.append(_3dmap4)
    _3dmap.append(_3dmap5)
    _3dmap.append(_3dmap6)
    _3dmap.append(_3dmap7)
    map_border = (len(_3dmap),len(_3dmap[0]),len(_3dmap[0][0]))
    return _3dmap

def preset_se1(_3dmap):
    global start, end
    x_index = 0 # x索引
    for yz in _3dmap: # row 表示_2dmap 中的每一行
        y_index = 0
        for z in yz: # n 表示一行中的各个元素
            z_index = 0
            for n in z: 
                if n == '1':
                    start = Node(None, x_index, y_index, z_index) # 添加起始点坐标
                    close_list[(start.x, start.y, start.z)] = start
                elif n == '2':
                    end = Node(None, x_index, y_index, z_index) # 添加终止点坐标
                z_index = z_index + 1
            y_index = y_index + 1
        x_index = x_index + 1
    path1.append((start.x, start.y, start.z))
    return start,close_list,path1
