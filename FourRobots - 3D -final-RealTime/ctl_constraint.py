#单机器人实时启发式路径规划代码，返回路径

import mpc1,mpc2,mpc3,mpc4
import cartoon
path1s = []
path2s = []
path3s = []
path4s = []
def total():
    map = mpc1.preset_map()
    start1, close_list1, path1s = mpc1.preset_se1(map)
    start2, close_list2, path2s = mpc2.preset_se2(map)
    start3, close_list3, path3s = mpc3.preset_se3(map)
    start4, close_list4, path4s = mpc4.preset_se4(map)
    is_end1 = False
    is_end2 = False
    is_end3 = False
    is_end4 = False
    while ((not is_end1) or (not is_end2) or (not is_end3) or (not is_end4)):
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
        near2 = mpc2.addAdjacentIntoOpen(start2)
        mpc2.sel_sort(near2)
        near3 = mpc3.addAdjacentIntoOpen(start3)
        mpc3.sel_sort(near3)
        near4 = mpc4.addAdjacentIntoOpen(start4)
        mpc4.sel_sort(near4)
        if len(path1s) == 1:
            cartoon.run(path1s,path2s,path3s,path4s)
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
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x == start2.x and start2.y - near2[j].y == 1 and near2[j].z == start2.z):  # 最下层中间节点
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictbm(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x == start3.x and start3.y - near3[k].y == 1 and near3[k].z == start3.z):  # 最下层中间节点
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictbm(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x == start4.x and start4.y - near4[l].y == 1 and near4[l].z == start4.z):  # 最下层中间节点
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictbm(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatebm(start1, map)
                                                                    path2s = mpc2.updatebm(start2, map)
                                                                    path3s = mpc3.updatebm(start3, map)
                                                                    path4s = mpc4.updatebm(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue                   
            elif (near1[i].x - start1.x == 1 and start1.y - near1[i].y == 1 and near1[i].z == start1.z):  # 最下层右
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbr(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and start2.y - near2[j].y == 1 and near2[j].z == start2.z):  # 最下层右
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictbr(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and start3.y - near3[k].y == 1 and near3[k].z == start3.z):  # 最下层右
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictbr(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and start4.y - near4[l].y == 1 and near4[l].z == start4.z):  # 最下层右
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictbr(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatebr(start1, map)
                                                                    path2s = mpc2.updatebr(start2, map)
                                                                    path3s = mpc3.updatebr(start3, map)
                                                                    path4s = mpc4.updatebr(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x - start1.x == 1 and start1.y - near1[i].y == 1 and near1[i].z - start1.z == 1):#最下层右下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbrd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and start2.y - near2[j].y == 1 and near2[j].z - start2.z == 1):#最下层右下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictbrd(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and start3.y - near3[k].y == 1 and near3[k].z - start3.z == 1):#最下层右下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictbrd(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and start4.y - near4[l].y == 1 and near4[l].z - start4.z == 1):#最下层右下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictbrd(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatebrd(start1, map)
                                                                    path2s = mpc2.updatebrd(start2, map)
                                                                    path3s = mpc3.updatebrd(start3, map)
                                                                    path4s = mpc4.updatebrd(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x - start1.x == 1 and start1.y - near1[i].y == 1 and start1.z - near1[i].z == 1): #最下层右上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbru(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and start2.y - near2[j].y == 1 and start2.z - near2[j].z == 1): #最下层右上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictbru(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and start3.y - near3[k].y == 1 and start3.z - near3[k].z == 1): #最下层右上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictbru(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and start4.y - near4[l].y == 1 and start4.z - near4[l].z == 1): #最下层右上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictbru(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatebru(start1, map)
                                                                    path2s = mpc2.updatebru(start2, map)
                                                                    path3s = mpc3.updatebru(start3, map)
                                                                    path4s = mpc4.updatebru(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x == start1.x and start1.y - near1[i].y == 1 and near1[i].z - start1.z == 1):#最下层下1
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x == start2.x and start2.y - near2[j].y == 1 and near2[j].z - start2.z == 1):#最下层下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictbd(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x == start3.x and start3.y - near3[k].y == 1 and near3[k].z - start3.z == 1):#最下层下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictbd(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x == start4.x and start4.y - near4[l].y == 1 and near4[l].z - start4.z == 1):#最下层下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictbd(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatebd(start1, map)
                                                                    path2s = mpc2.updatebd(start2, map)
                                                                    path3s = mpc3.updatebd(start3, map)
                                                                    path4s = mpc4.updatebd(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x == start1.x and start1.y - near1[i].y == 1 and start1.z - near1[i].z == 1): #最下层上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x == start2.x and start2.y - near2[j].y == 1 and start2.z - near2[j].z == 1): #最下层上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictbu(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x == start3.x and start3.y - near3[k].y == 1 and start3.z - near3[k].z == 1): #最下层上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictbu(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x == start4.x and start4.y - near4[l].y == 1 and start4.z - near4[l].z == 1): #最下层上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictbu(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatebu(start1, map)
                                                                    path2s = mpc2.updatebu(start2, map)
                                                                    path3s = mpc3.updatebu(start3, map)
                                                                    path4s = mpc4.updatebu(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and start1.y - near1[i].y == 1 and near1[i].z - start1.z == 1): #最下层左下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbld(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and start2.y - near2[j].y == 1 and near2[j].z - start2.z == 1): #最下层左下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictbld(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and start3.y - near3[k].y == 1 and near3[k].z - start3.z == 1): #最下层左下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictbld(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and start4.y - near4[l].y == 1 and near4[l].z - start4.z == 1): #最下层左下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictbld(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatebld(start1, map)
                                                                    path2s = mpc2.updatebld(start2, map)
                                                                    path3s = mpc3.updatebld(start3, map)
                                                                    path4s = mpc4.updatebld(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and start1.y - near1[i].y == 1 and start1.z - near1[i].z == 1): #最下层左上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictblu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and start2.y - near2[j].y == 1 and start2.z - near2[j].z == 1): #最下层左上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictblu(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and start3.y - near3[k].y == 1 and start3.z - near3[k].z == 1): #最下层左上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictblu(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and start4.y - near4[l].y == 1 and start4.z - near4[l].z == 1): #最下层左上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictblu(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updateblu(start1, map)
                                                                    path2s = mpc2.updateblu(start2, map)
                                                                    path3s = mpc3.updateblu(start3, map)
                                                                    path4s = mpc4.updateblu(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and start1.y - near1[i].y == 1 and near1[i].z == start1.z): #最下层左
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictbl(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and start2.y - near2[j].y == 1 and near2[j].z == start2.z): #最下层左
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictbl(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and start3.y - near3[k].y == 1 and near3[k].z == start3.z): #最下层左
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictbl(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and start4.y - near4[l].y == 1 and near4[l].z == start4.z): #最下层左
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictbl(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatebl(start1, map)
                                                                    path2s = mpc2.updatebl(start2, map)
                                                                    path3s = mpc3.updatebl(start3, map)
                                                                    path4s = mpc4.updatebl(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
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
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and start2.y == near2[j].y and near2[j].z == start2.z):  # 中间层右
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictmr(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and start3.y == near3[k].y and near3[k].z == start3.z):  # 中间层右
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictmr(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and start4.y == near4[l].y and near4[l].z == start4.z):  # 中间层右
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictmr(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatemr(start1, map)
                                                                    path2s = mpc2.updatemr(start2, map)
                                                                    path3s = mpc3.updatemr(start3, map)
                                                                    path4s = mpc4.updatemr(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x - start1.x == 1 and start1.y == near1[i].y and near1[i].z - start1.z == 1):#中间层右下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmrd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and start2.y == near2[j].y and near2[j].z - start2.z == 1):#中间层右下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictmrd(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and start3.y == near3[k].y and near3[k].z - start3.z == 1):#中间层右下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictmrd(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and start4.y == near4[l].y and near4[l].z - start4.z == 1):#中间层右下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictmrd(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatemrd(start1, map)
                                                                    path2s = mpc2.updatemrd(start2, map)
                                                                    path3s = mpc3.updatemrd(start3, map)
                                                                    path4s = mpc4.updatemrd(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x - start1.x == 1 and start1.y == near1[i].y and start1.z - near1[i].z == 1): #中间层右上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmru(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and start2.y == near2[j].y and start2.z - near2[j].z == 1): #中间层右上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictmru(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and start3.y == near3[k].y and start3.z - near3[k].z == 1): #中间层右上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictmru(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and start4.y == near4[l].y and start4.z - near4[l].z == 1): #中间层右上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictmru(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatemru(start1, map)
                                                                    path2s = mpc2.updatemru(start2, map)
                                                                    path3s = mpc3.updatemru(start3, map)
                                                                    path4s = mpc4.updatemru(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x == start1.x and start1.y == near1[i].y and near1[i].z - start1.z == 1):#中间层下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x == start2.x and start2.y == near2[j].y and near2[j].z - start2.z == 1):#中间层下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictmd(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x == start3.x and start3.y == near3[k].y and near3[k].z - start3.z == 1):#中间层下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictmd(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x == start4.x and start4.y == near4[l].y and near4[l].z - start4.z == 1):#中间层下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictmd(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatemd(start1, map)
                                                                    path2s = mpc2.updatemd(start2, map)
                                                                    path3s = mpc3.updatemd(start3, map)
                                                                    path4s = mpc4.updatemd(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x == start1.x and start1.y == near1[i].y and start1.z - near1[i].z == 1): #中间层上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x == start2.x and start2.y == near2[j].y and start2.z - near2[j].z == 1): #中间层上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictmu(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x == start3.x and start3.y == near3[k].y and start3.z - near3[k].z == 1): #中间层上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictmu(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x == start4.x and start4.y == near4[l].y and start4.z - near4[l].z == 1): #中间层上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictmu(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatemu(start1, map)
                                                                    path2s = mpc2.updatemu(start2, map)
                                                                    path3s = mpc3.updatemu(start3, map)
                                                                    path4s = mpc4.updatemu(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and start1.y == near1[i].y and near1[i].z - start1.z == 1): #中间层左下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmld(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and start2.y == near2[j].y and near2[j].z - start2.z == 1): #中间层左下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictmld(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and start3.y == near3[k].y and near3[k].z - start3.z == 1): #中间层左下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictmld(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and start4.y == near4[l].y and near4[l].z - start4.z == 1): #中间层左下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictmld(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatemld(start1, map)
                                                                    path2s = mpc2.updatemld(start2, map)
                                                                    path3s = mpc3.updatemld(start3, map)
                                                                    path4s = mpc4.updatemld(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and start1.y == near1[i].y and start1.z - near1[i].z == 1): #中间层左上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictmlu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and start2.y == near2[j].y and start2.z - near2[j].z == 1): #中间层左上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictmlu(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and start3.y == near3[k].y and start3.z - near3[k].z == 1): #中间层左上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictmlu(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and start4.y == near4[l].y and start4.z - near4[l].z == 1): #中间层左上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictmlu(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatemlu(start1, map)
                                                                    path2s = mpc2.updatemlu(start2, map)
                                                                    path3s = mpc3.updatemlu(start3, map)
                                                                    path4s = mpc4.updatemlu(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and start1.y == near1[i].y and near1[i].z == start1.z): #中间层左
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictml(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and start2.y == near2[j].y and near2[j].z == start2.z): #中间层左
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictml(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and start3.y == near3[k].y and near3[k].z == start3.z): #中间层左
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictml(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and start4.y == near4[l].y and near4[l].z == start4.z): #中间层左
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictml(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updateml(start1, map)
                                                                    path2s = mpc2.updateml(start2, map)
                                                                    path3s = mpc3.updateml(start3, map)
                                                                    path4s = mpc4.updateml(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
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
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x == start2.x and near2[j].y - start2.y == 1 and near2[j].z == start2.z):  # 最上层中间节点
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttm(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x == start3.x and near3[k].y - start3.y == 1 and near3[k].z == start3.z):  # 最上层中间节点
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttm(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x == start4.x and near4[l].y - start4.y == 1 and near4[l].z == start4.z):  # 最上层中间节点
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttm(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetm(start1, map)
                                                                    path2s = mpc2.updatetm(start2, map)
                                                                    path3s = mpc3.updatetm(start3, map)
                                                                    path4s = mpc4.updatetm(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x - start1.x == 1 and near1[i].y - start1.y == 1 and near1[i].z == start1.z):  # 最上层右
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttr(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and near2[j].y - start2.y == 1 and near2[j].z == start2.z):  # 最上层右
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttr(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and near3[k].y - start3.y == 1 and near3[k].z == start3.z):  # 最上层右
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttr(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and near4[l].y - start4.y == 1 and near4[l].z == start4.z):  # 最上层右
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttr(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetr(start1, map)
                                                                    path2s = mpc2.updatetr(start2, map)
                                                                    path3s = mpc3.updatetr(start3, map)
                                                                    path4s = mpc4.updatetr(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x - start1.x == 1 and near1[i].y - start1.y == 1 and near1[i].z - start1.z == 1):#最上层右下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttrd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and near2[j].y - start2.y == 1 and near2[j].z - start2.z == 1):#最上层右下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttrd(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and near3[k].y - start3.y == 1 and near3[k].z - start3.z == 1):#最上层右下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttrd(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and near4[l].y - start4.y == 1 and near4[l].z - start4.z == 1):#最上层右下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttrd(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetrd(start1, map)
                                                                    path2s = mpc2.updatetrd(start2, map)
                                                                    path3s = mpc3.updatetrd(start3, map)
                                                                    path4s = mpc4.updatetrd(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x - start1.x == 1 and near1[i].y - start1.y == 1 and start1.z - near1[i].z == 1): #最上层右上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttru(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x - start2.x == 1 and near2[j].y - start2.y == 1 and start2.z - near2[j].z == 1): #最上层右上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttru(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x - start3.x == 1 and near3[k].y - start3.y == 1 and start3.z - near3[k].z == 1): #最上层右上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttru(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x - start4.x == 1 and near4[l].y - start4.y == 1 and start4.z - near4[l].z == 1): #最上层右上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttru(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetru(start1, map)
                                                                    path2s = mpc2.updatetru(start2, map)
                                                                    path3s = mpc3.updatetru(start3, map)
                                                                    path4s = mpc4.updatetru(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x == start1.x and near1[i].y - start1.y == 1 and near1[i].z - start1.z == 1):#最上层下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x == start2.x and near2[j].y - start2.y == 1 and near2[j].z - start2.z == 1):#最上层下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttd(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x == start3.x and near3[k].y - start3.y == 1 and near3[k].z - start3.z == 1):#最上层下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttd(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x == start4.x and near4[l].y - start4.y == 1 and near4[l].z - start4.z == 1):#最上层下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttd(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetd(start1, map)
                                                                    path2s = mpc2.updatetd(start2, map)
                                                                    path3s = mpc3.updatetd(start3, map)
                                                                    path4s = mpc4.updatetd(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (near1[i].x == start1.x and near1[i].y - start1.y == 1 and start1.z - near1[i].z == 1): #最上层上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (near2[j].x == start2.x and near2[j].y - start2.y == 1 and start2.z - near2[j].z == 1): #最上层上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttu(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (near3[k].x == start3.x and near3[k].y - start3.y == 1 and start3.z - near3[k].z == 1): #最上层上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttu(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (near4[l].x == start4.x and near4[l].y - start4.y == 1 and start4.z - near4[l].z == 1): #最上层上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttu(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetu(start1, map)
                                                                    path2s = mpc2.updatetu(start2, map)
                                                                    path3s = mpc3.updatetu(start3, map)
                                                                    path4s = mpc4.updatetu(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and near1[i].y - start1.y == 1 and near1[i].z - start1.z == 1): #最上层左下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttld(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and near2[j].y - start2.y == 1 and near2[j].z - start2.z == 1): #最上层左下
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttld(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and near3[k].y - start3.y == 1 and near3[k].z - start3.z == 1): #最上层左下
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttld(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and near4[l].y - start4.y == 1 and near4[l].z - start4.z == 1): #最上层左下
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttld(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetld(start1, map)
                                                                    path2s = mpc2.updatetld(start2, map)
                                                                    path3s = mpc3.updatetld(start3, map)
                                                                    path4s = mpc4.updatetld(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and near1[i].y - start1.y == 1 and start1.z - near1[i].z == 1): #最上层左上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttlu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and near2[j].y - start2.y == 1 and start2.z - near2[j].z == 1): #最上层左上
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttlu(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and near3[k].y - start3.y == 1 and start3.z - near3[k].z == 1): #最上层左上
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttlu(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and near4[l].y - start4.y == 1 and start4.z - near4[l].z == 1): #最上层左上
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttlu(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetlu(start1, map)
                                                                    path2s = mpc2.updatetlu(start2, map)
                                                                    path3s = mpc3.updatetlu(start3, map)
                                                                    path4s = mpc4.updatetlu(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
            elif (start1.x - near1[i].x == 1 and near1[i].y - start1.y == 1 and near1[i].z == start1.z): #最上层左
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predicttl(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        ctlnum1 = 0
                        if (near2[j].x, near2[j].y, near2[j].z) in close_list2:
                            continue
                        elif (start2.x - near2[j].x == 1 and near2[j].y - start2.y == 1 and near2[j].z == start2.z): #最上层左
                            if (near1[i].x - near2[j].x == 2 and near1[i].y == near2[j].y and near1[i].z == near2[j].z): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predicttl(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        ctlnum2 = 0
                                        if (near3[k].x, near3[k].y, near3[k].z) in close_list3:
                                            continue
                                        elif (start3.x - near3[k].x == 1 and near3[k].y - start3.y == 1 and near3[k].z == start3.z): #最上层左
                                            if (near1[i].x - near3[k].x == 2 and near1[i].y == near3[k].y and near3[k].z - near1[i].z == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predicttl(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        ctlnum3 = 0
                                                        if (near4[l].x, near4[l].y, near4[l].z) in close_list4:
                                                            continue
                                                        elif (start4.x - near4[l].x == 1 and near4[l].y - start4.y == 1 and near4[l].z == start4.z): #最上层左
                                                            if (near1[i].x == near4[l].x and near1[i].y == near4[l].y and near4[l].z - near1[i].z == 2 ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predicttl(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].x, near1[i].y, near1[i].z)] = near1[i] 
                                                                    close_list2[(near2[j].x, near2[j].y, near2[j].z)] = near2[j]
                                                                    close_list3[(near3[k].x, near3[k].y, near3[k].z)] = near3[k]
                                                                    close_list4[(near4[l].x, near4[l].y, near4[l].z)] = near4[l]
                                                                    path1s = mpc1.updatetl(start1, map)
                                                                    path2s = mpc2.updatetl(start2, map)
                                                                    path3s = mpc3.updatetl(start3, map)
                                                                    path4s = mpc4.updatetl(start4, map)
                                                                    ctlnum3 = 1
                                                                    break
                                                            else:
                                                                continue
                                                    if (ctlnum3 == 1):
                                                        ctlnum3 = 0
                                                        break
                                                    else:
                                                        continue
                                    if (ctlnum2 == 1):
                                        ctlnum2 = 0
                                        break
                                    else:
                                        continue
                    if (ctlnum1 == 1):
                        ctlnum1 = 0
                        break
                    else:
                        continue
        cartoon.run(path1s,path2s,path3s,path4s)
        print(close_list1)
        print(close_list2)
        print(close_list3)
        print(close_list4)
    return (path1s,path2s,path3s,path4s)

if __name__=='__main__':
    k1,k2,k3,k4 = total()
    print(k1)
    print(k2)
    print(k3)
    print(k4)









