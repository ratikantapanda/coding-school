def two_number_sum(array, target_sum):
    nums_dict={}
    for idx,num in enumerate(array):
        num_req=target_sum -num
        if num_req in nums_dict:
            num_req_idx=nums_dict[num_req]
            return [(num,idx),(num_req,num_req_idx)]
        else:
            nums_dict[num]=idx
    return None

def two_number_sum_2(array, target_sum):
    array.sort()
    left=0
    right=len(array) -1
    while left < right:
        sum=array[left] + array[right]
        if sum == target_sum:
            return [(array[left],left),(array[right],right)]
        elif sum  < target_sum:
            left += 1
        else:
            right -= 1
    return None
