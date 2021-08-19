#单机器人实时启发式路径规划代码，返回路径

import mpc1
path1s = []
def total():
    map = mpc1.preset_map()
    start1, close_list1, path1s = mpc1.preset_se1(map)
    is_end1 = False
    while (not is_end1):
        near1 = mpc1.addAdjacentIntoOpen(start1)
        mpc1.sel_sort(near1)
        for i in range(len(near1) - 1, -1, -1):
            if (near1[i].row, near1[i].col) in close_list1:
                continue
            elif (near1[i].row == start1.row and near1[i].col - start1.col == 1):  # 右
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictr(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]                
                    path1s = mpc1.updater(start1, map)           
                    break
            elif (near1[i].row - start1.row == 1 and near1[i].col - start1.col == 1):#右下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictrd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]                
                    path1s = mpc1.updaterd(start1, map)           
                    break
            elif (start1.row - near1[i].row == 1 and near1[i].col - start1.col == 1): #右上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictru(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]                
                    path1s = mpc1.updateru(start1, map)           
                    break
            elif (near1[i].row - start1.row == 1 and near1[i].col == start1.col):#下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]                
                    path1s = mpc1.updated(start1, map)           
                    break
            elif (start1.row - near1[i].row == 1 and near1[i].col == start1.col): #上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]                
                    path1s = mpc1.updateu(start1, map)           
                    break
            elif (near1[i].row - start1.row == 1 and start1.col - near1[i].col == 1): #左下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictld(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]                
                    path1s = mpc1.updateld(start1, map)           
                    break
            elif (start1.row - near1[i].row == 1 and start1.col - near1[i].col == 1): #左上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictlu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]                
                    path1s = mpc1.updatelu(start1, map)           
                    break
            elif (start1.row == near1[i].row and start1.col - near1[i].col == 1): #左
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictl(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]                
                    path1s = mpc1.updatel(start1, map)           
                    break
        print(close_list1)
    return (path1s)
    print (path1s)











