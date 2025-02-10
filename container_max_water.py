#each element arr[i] represents height of vertical lines find the max amount of water stored between any two lines
def mostwater(arr):
    if not arr:
        return -1
    i = 0
    j = len(arr)-1
    area = 0
    while i<j:
        count = min(arr[i],arr[j])*(j-i)
        area = max(area, count)
        if arr[i]<arr[j]:
            i +=1
        else:
            j -= 1
    return area
arr = [8,6,2,4,1,9,3]
res = mostwater(arr)
print(res)