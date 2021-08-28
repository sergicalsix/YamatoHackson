def past_time_calc(c:dict,truck:list ) ->list:
    """
    in: 
        各経路でかかる時間:dict
        運転手の経路 :list
    out: 
        運転手の経路時間
    """
    ans = []
    
    #人数分のfor文
    for i in range(1,len(truck)+1 ):
        time_list = [] #一人一人の経過時間
        for j in range(len(truck[i]) - 1):
            key_ = (truck[i][j],truck[i][j+1])
            #key_ = '(' + str(truck[i][j]) + ','
            time_list.append(int(c[key_]))
        ans.extend([time_list])
    
    return ans 
    
