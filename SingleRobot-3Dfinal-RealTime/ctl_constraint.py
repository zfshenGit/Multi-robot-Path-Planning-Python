#单机器人实时启发式路径规划代码，返回路径

import mpc1
import cartoon
path1s = []
def total():
    map = mpc1.preset_map()
    start1, close_list1, path1s = mpc1.preset_se1(map)
    is_end1 = False
    while (not is_end1):
        #判断是否实时添加障碍物，通过按键kq添加
        keydown0 = cartoon.keydown0
        key_x0 = cartoon.key_x0
        key_y0 = cartoon.key_y0
        key_z0 = cartoon.key_z0
        if keydown0 == True:
            map[key_x0][key_y0][key_z0] = '9'
        #判断是否实时添加障碍物，通过按键ka添加
        keydown1 = cartoon.keydown1
        key_x1 = cartoon.key_x1
        key_y1 = cartoon.key_y1
        key_z1 = cartoon.key_z1
        if keydown1 == True:
            map[key_x1][key_y1][key_z1] = '9'
            
        near1 = mpc1.addAdjacentIntoOpen(start1)
        mpc1.sel_sort(near1)
        if len(path1s) == 1:
            cartoon.run(path1s)
        for i in range(len(near1) - 1, -1, -1):
            if (near1[i].x, near1[i].y, near1[i].z) in close_list1:
                continue
            elif (near1[i].x == start1.x and start1.y - near1[i].y == 1 and near1[i].z == start1.z):  # 最下层中间节点
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbm(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]                
                    path1s = mpc1.updatebm(start1, map)           
                    break
            elif (near1[i].x - start1.x == 1 and start1.y - near1[i].y == 1 and near1[i].z == start1.z):  # 最下层右
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbr(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]                
                    path1s = mpc1.updatebr(start1, map)           
                    break
            elif (near1[i].x - start1.x == 1 and start1.y - near1[i].y == 1 and near1[i].z - start1.z == 1):#最下层右下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbrd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatebrd(start1, map)           
                    break
            elif (near1[i].x - start1.x == 1 and start1.y - near1[i].y == 1 and start1.z - near1[i].z == 1): #最下层右上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbru(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatebru(start1, map)           
                    break
            elif (near1[i].x == start1.x and start1.y - near1[i].y == 1 and near1[i].z - start1.z == 1):#最下层下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatebd(start1, map)           
                    break
            elif (near1[i].x == start1.x and start1.y - near1[i].y == 1 and start1.z - near1[i].z == 1): #最下层上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatebu(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and start1.y - near1[i].y == 1 and near1[i].z - start1.z == 1): #最下层左下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbld(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatebld(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and start1.y - near1[i].y == 1 and start1.z - near1[i].z == 1): #最下层左上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictblu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]                
                    path1s = mpc1.updateblu(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and start1.y - near1[i].y == 1 and near1[i].z == start1.z): #最下层左
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbl(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatebl(start1, map)           
                    break
            #中间层
            elif (near1[i].x - start1.x == 1 and start1.y == near1[i].y and near1[i].z == start1.z):  # 中间层右
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmr(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]                
                    path1s = mpc1.updatemr(start1, map)           
                    break
            elif (near1[i].x - start1.x == 1 and start1.y == near1[i].y and near1[i].z - start1.z == 1):#中间层右下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmrd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatemrd(start1, map)           
                    break
            elif (near1[i].x - start1.x == 1 and start1.y == near1[i].y and start1.z - near1[i].z == 1): #中间层右上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmru(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatemru(start1, map)           
                    break
            elif (near1[i].x == start1.x and start1.y == near1[i].y and near1[i].z - start1.z == 1):#中间层下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatemd(start1, map)           
                    break
            elif (near1[i].x == start1.x and start1.y == near1[i].y and start1.z - near1[i].z == 1): #中间层上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatemu(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and start1.y == near1[i].y and near1[i].z - start1.z == 1): #中间层左下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmld(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatemld(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and start1.y == near1[i].y and start1.z - near1[i].z == 1): #中间层左上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmlu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]                
                    path1s = mpc1.updatemlu(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and start1.y == near1[i].y and near1[i].z == start1.z): #中间层左
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictml(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updateml(start1, map)           
                    break
            #最上层
            elif (near1[i].x == start1.x and near1[i].y - start1.y == 1 and near1[i].z == start1.z):  # 最上层中间节点
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttm(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]                
                    path1s = mpc1.updatetm(start1, map)           
                    break
            elif (near1[i].x - start1.x == 1 and near1[i].y - start1.y == 1 and near1[i].z == start1.z):  # 最上层右
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttr(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]                
                    path1s = mpc1.updatetr(start1, map)           
                    break
            elif (near1[i].x - start1.x == 1 and near1[i].y - start1.y == 1 and near1[i].z - start1.z == 1):#最上层右下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttrd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatetrd(start1, map)           
                    break
            elif (near1[i].x - start1.x == 1 and near1[i].y - start1.y == 1 and start1.z - near1[i].z == 1): #最上层右上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttru(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatetru(start1, map)           
                    break
            elif (near1[i].x == start1.x and near1[i].y - start1.y == 1 and near1[i].z - start1.z == 1):#最上层下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatetd(start1, map)           
                    break
            elif (near1[i].x == start1.x and near1[i].y - start1.y == 1 and start1.z - near1[i].z == 1): #最上层上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatetu(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and near1[i].y - start1.y == 1 and near1[i].z - start1.z == 1): #最上层左下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttld(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatetld(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and near1[i].y - start1.y == 1 and start1.z - near1[i].z == 1): #最上层左上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttlu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]                
                    path1s = mpc1.updatetlu(start1, map)           
                    break
            elif (start1.x - near1[i].x == 1 and near1[i].y - start1.y == 1 and near1[i].z == start1.z): #最上层左
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttl(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]               
                    path1s = mpc1.updatetl(start1, map)           
                    break
        print(close_list1)
        cartoon.run(path1s)
    return (path1s)
    print (path1s)

if __name__=='__main__':
    k1 = total()
    print (k1)









