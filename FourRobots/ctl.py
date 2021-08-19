#四机器人 CTL 约束代码，可扩展至更多机器人

import mpc1,mpc2,mpc3,mpc4
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
        near1 = mpc1.addAdjacentIntoOpen(start1)
        mpc1.sel_sort(near1)
        near2 = mpc2.addAdjacentIntoOpen(start2)
        mpc2.sel_sort(near2)
        near3 = mpc3.addAdjacentIntoOpen(start3)
        mpc3.sel_sort(near3)
        near4 = mpc4.addAdjacentIntoOpen(start4)
        mpc4.sel_sort(near4)
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
                    for j in range(len(near2) - 1, -1, -1):
                        if (near2[j].row, near2[j].col) in close_list2:
                            continue
                        elif (near2[j].row == start2.row and near2[j].col - start2.col == 1): # 右
                            if (near1[i].row == near2[j].row and near1[i].col - near2[j].col == 2): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictr(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        if (near3[k].row, near3[k].col) in close_list3:
                                            continue
                                        elif (near3[k].row == start3.row and near3[k].col - start3.col == 1): # 右
                                            if (near3[k].row - near1[i].row == 2 and near1[i].col - near3[k].col == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictr(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        if (near4[l].row, near4[l].col) in close_list4:
                                                            continue
                                                        elif (near4[l].row == start4.row and near4[l].col - start4.col == 1): # 右
                                                            if (near4[l].row - near1[i].row == 2 and near1[i].col == near4[l].col ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictr(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                                                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    path1s = mpc1.updater(start1, map)
                                                                    path2s = mpc2.updater(start2, map)
                                                                    path3s = mpc3.updater(start3, map)
                                                                    path4s = mpc4.updater(start4, map)
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
            elif (near1[i].row - start1.row == 1 and near1[i].col - start1.col == 1):  #右下 
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictrd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        if (near2[j].row, near2[j].col) in close_list2:
                            continue
                        elif (near2[j].row - start2.row == 1 and near2[j].col - start2.col == 1): # 右下
                            if (near1[i].row == near2[j].row and near1[i].col - near2[j].col == 2): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictrd(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        if (near3[k].row, near3[k].col) in close_list3:
                                            continue
                                        elif (near3[k].row - start3.row == 1 and near3[k].col - start3.col == 1): # 右下
                                            if (near3[k].row - near1[i].row == 2 and near1[i].col - near3[k].col == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictrd(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        if (near4[l].row, near4[l].col) in close_list4:
                                                            continue
                                                        elif (near4[l].row - start4.row == 1 and near4[l].col - start4.col == 1): # 右下
                                                            if (near4[l].row - near1[i].row == 2 and near1[i].col == near4[l].col ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictrd(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                                                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    path1s = mpc1.updaterd(start1, map)
                                                                    path2s = mpc2.updaterd(start2, map)
                                                                    path3s = mpc3.updaterd(start3, map)
                                                                    path4s = mpc4.updaterd(start4, map)
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
            elif (start1.row - near1[i].row == 1 and near1[i].col - start1.col == 1):  # 右上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictru(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        if (near2[j].row, near2[j].col) in close_list2:
                            continue
                        elif (start2.row - near2[j].row == 1 and near2[j].col - start2.col == 1): # 右上
                            if (near1[i].row == near2[j].row and near1[i].col - near2[j].col == 2): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictru(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        if (near3[k].row, near3[k].col) in close_list3:
                                            continue
                                        elif (start3.row - near3[k].row == 1 and near3[k].col - start3.col == 1): # 右上
                                            if (near3[k].row - near1[i].row == 2 and near1[i].col - near3[k].col == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictru(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        if (near4[l].row, near4[l].col) in close_list4:
                                                            continue
                                                        elif (start4.row - near4[l].row == 1 and near4[l].col - start4.col == 1): # 右上
                                                            if (near4[l].row - near1[i].row == 2 and near1[i].col == near4[l].col ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictru(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                                                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    path1s = mpc1.updateru(start1, map)
                                                                    path2s = mpc2.updateru(start2, map)
                                                                    path3s = mpc3.updateru(start3, map)
                                                                    path4s = mpc4.updateru(start4, map)
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
            elif (near1[i].row - start1.row == 1 and near1[i].col == start1.col):  # 下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictd(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        if (near2[j].row, near2[j].col) in close_list2:
                            continue
                        elif (near2[j].row - start2.row == 1 and near2[j].col == start2.col): # 下
                            if (near1[i].row == near2[j].row and near1[i].col - near2[j].col == 2): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictd(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        if (near3[k].row, near3[k].col) in close_list3:
                                            continue
                                        elif (near3[k].row - start3.row == 1 and near3[k].col == start3.col): # 下
                                            if (near3[k].row - near1[i].row == 2 and near1[i].col - near3[k].col == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictd(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        if (near4[l].row, near4[l].col) in close_list4:
                                                            continue
                                                        elif (near4[l].row - start4.row == 1 and near4[l].col == start4.col): # 下
                                                            if (near4[l].row - near1[i].row == 2 and near1[i].col == near4[l].col ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictd(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                                                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    path1s = mpc1.updated(start1, map)
                                                                    path2s = mpc2.updated(start2, map)
                                                                    path3s = mpc3.updated(start3, map)
                                                                    path4s = mpc4.updated(start4, map)
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
            elif (start1.row - near1[i].row == 1 and near1[i].col == start1.col):  # 上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        if (near2[j].row, near2[j].col) in close_list2:
                            continue
                        elif (start2.row - near2[j].row == 1 and near2[j].col == start2.col): # 上
                            if (near1[i].row == near2[j].row and near1[i].col - near2[j].col == 2): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictu(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        if (near3[k].row, near3[k].col) in close_list3:
                                            continue
                                        elif (start3.row - near3[k].row == 1 and near3[k].col == start3.col): # 上
                                            if (near3[k].row - near1[i].row == 2 and near1[i].col - near3[k].col == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictu(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        if (near4[l].row, near4[l].col) in close_list4:
                                                            continue
                                                        elif (start4.row - near4[l].row == 1 and near4[l].col == start4.col): # 上
                                                            if (near4[l].row - near1[i].row == 2 and near1[i].col == near4[l].col ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictu(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                                                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    path1s = mpc1.updateu(start1, map)
                                                                    path2s = mpc2.updateu(start2, map)
                                                                    path3s = mpc3.updateu(start3, map)
                                                                    path4s = mpc4.updateu(start4, map)
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
            elif (near1[i].row - start1.row == 1 and start1.col - near1[i].col == 1):  # 左下
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictld(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        if (near2[j].row, near2[j].col) in close_list2:
                            continue
                        elif (near2[j].row - start2.row == 1 and start2.col - near2[j].col == 1): # 左下
                            if (near1[i].row == near2[j].row and near1[i].col - near2[j].col == 2): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictld(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        if (near3[k].row, near3[k].col) in close_list3:
                                            continue
                                        elif (near3[k].row - start3.row == 1 and start3.col - near3[k].col == 1): # 左下
                                            if (near3[k].row - near1[i].row == 2 and near1[i].col - near3[k].col == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictld(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        if (near4[l].row, near4[l].col) in close_list4:
                                                            continue
                                                        elif (near4[l].row - start4.row == 1 and start4.col - near4[l].col == 1): # 左下
                                                            if (near4[l].row - near1[i].row == 2 and near1[i].col == near4[l].col ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictld(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                                                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    path1s = mpc1.updateld(start1, map)
                                                                    path2s = mpc2.updateld(start2, map)
                                                                    path3s = mpc3.updateld(start3, map)
                                                                    path4s = mpc4.updateld(start4, map)
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
            elif (start1.row - near1[i].row == 1 and start1.col - near1[i].col == 1):  # 左上
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictlu(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        if (near2[j].row, near2[j].col) in close_list2:
                            continue
                        elif (start2.row - near2[j].row == 1 and start2.col - near2[j].col == 1): # 左上
                            if (near1[i].row == near2[j].row and near1[i].col - near2[j].col == 2): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictlu(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        if (near3[k].row, near3[k].col) in close_list3:
                                            continue
                                        elif (start3.row - near3[k].row == 1 and start3.col - near3[k].col == 1): # 左上
                                            if (near3[k].row - near1[i].row == 2 and near1[i].col - near3[k].col == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictlu(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        if (near4[l].row, near4[l].col) in close_list4:
                                                            continue
                                                        elif (start4.row - near4[l].row == 1 and start4.col - near4[l].col == 1): # 左上
                                                            if (near4[l].row - near1[i].row == 2 and near1[i].col == near4[l].col ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictlu(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                                                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    path1s = mpc1.updatelu(start1, map)
                                                                    path2s = mpc2.updatelu(start2, map)
                                                                    path3s = mpc3.updatelu(start3, map)
                                                                    path4s = mpc4.updatelu(start4, map)
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
            elif (start1.row == near1[i].row and start1.col - near1[i].col == 1):  # 左
                is_end1, block_flag, avoid_diag_block_flag = mpc1.predictl(start1,map)  # 将地图作为参数，是为了实时更新地图情况
                
                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                if (avoid_diag_block_flag == 1):
                    continue
                if (block_flag == 1):
                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                    continue
                else:
                    for j in range(len(near2) - 1, -1, -1):
                        if (near2[j].row, near2[j].col) in close_list2:
                            continue
                        elif (start2.row == near2[j].row and start2.col - near2[j].col == 1): # 左
                            if (near1[i].row == near2[j].row and near1[i].col - near2[j].col == 2): # 满足 CTL
                                is_end2, block_flag, avoid_diag_block_flag = mpc2.predictl(start2, map)
                                
                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                if (avoid_diag_block_flag == 1):
                                    ctlnum1 = 0
                                    continue
                                if (block_flag == 1):
                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                    ctlnum1 = 0
                                    continue
                                else:
                                    ctlnum1 = 1
                                    for k in range(len(near3) - 1, -1, -1):
                                        if (near3[k].row, near3[k].col) in close_list3:
                                            continue
                                        elif (start3.row == near3[k].row and start3.col - near3[k].col == 1): # 左
                                            if (near3[k].row - near1[i].row == 2 and near1[i].col - near3[k].col == 2): # 满足 CTL
                                                is_end3, block_flag, avoid_diag_block_flag = mpc3.predictl(start3, map)
                                                
                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                if (avoid_diag_block_flag == 1):
                                                    ctlnum2 = 0
                                                    continue
                                                if (block_flag == 1):
                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                    ctlnum2 = 0
                                                    continue
                                                else:
                                                    ctlnum2 = 1
                                                    for l in range(len(near4) - 1, -1, -1):
                                                        if (near4[l].row, near4[l].col) in close_list4:
                                                            continue
                                                        elif (start4.row == near4[l].row and start4.col - near4[l].col == 1): # 左
                                                            if (near4[l].row - near1[i].row == 2 and near1[i].col == near4[l].col ): # 满足 CTL
                                                                is_end4, block_flag, avoid_diag_block_flag = mpc4.predictl(start4, map)
                                                                
                                                                # block_flag 等于 1 代表下一个状态或下下个状态有障碍物，continue 转换方向
                                                                if (avoid_diag_block_flag == 1):
                                                                    ctlnum3 = 0
                                                                    continue
                                                                if (block_flag == 1):
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    ctlnum3 = 0
                                                                    continue
                                                                else:
                                                                    close_list1[(near1[i].row, near1[i].col)] = near1[i]
                                                                    close_list2[(near2[j].row, near2[j].col)] = near2[j]
                                                                    close_list3[(near3[k].row, near3[k].col)] = near3[k]
                                                                    close_list4[(near4[l].row, near4[l].col)] = near4[l]
                                                                    path1s = mpc1.updatel(start1, map)
                                                                    path2s = mpc2.updatel(start2, map)
                                                                    path3s = mpc3.updatel(start3, map)
                                                                    path4s = mpc4.updatel(start4, map)
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
        print(close_list1)
        print(close_list2)
        print(close_list3)
        print(close_list4)
    return (path1s,path2s,path3s,path4s)
    print (path1s)
    print (path2s)
    print (path3s)
    print (path4s)











