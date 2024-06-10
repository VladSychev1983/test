def vote(votes):
    result_dic = {}
    unique_list = sorted(list(set(votes)))
    for num in unique_list:
        count_num = votes.count(num)
        result_dic[num] = count_num
    result_dic_sorted = sorted(result_dic.items(), key=lambda x:x[1])
    return result_dic_sorted[-1][0]

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))
    
#vote([1,1,1,2,3])
#vote([1,2,3,2,2])
#vote([10,10,2,3,5,7]
