def binary_search(l,target,low=None,high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high < low :
        return -1
    
    mid = (low + high) // 2

    if l[mid] == target:
        return mid
    elif target > l[mid]:
        return binary_search(l,target,mid+1,high)
    else:
        return binary_search(l,target,low,mid-1)

if __name__== '__main__':
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    target = 10
    print(binary_search(l,target))

# print(l[32])