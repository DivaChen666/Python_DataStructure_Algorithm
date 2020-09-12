def finding_max_array(array):
    # global_max=float('-inf')
    max_ending_here=array[0]
    for i in range(1,len(array)):
        if max_ending_here<0:
            max_ending_here=array[i]
        else:
            max_ending_here = array[i]+max_ending_here
        # global_max=max(global_max,max_ending_here)
    return max_ending_here



array1=[2,5,-4,8,-11,1,6,12,17]
print(finding_max_array(array1))