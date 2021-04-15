# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def mean(n, arr):
    ans = sum(arr)/n
    return round(ans, 1)

def mode(n, arr):
    curr_mode = 0
    mode_freq = 0 # will always be beaten
    for elem in arr:
        freq = arr.count(elem)
        if freq > mode_freq:
            curr_mode = elem
            mode_freq = freq
        elif freq == mode_freq:
            curr_mode = min(curr_mode, elem)
    return curr_mode

def median(n, arr):
    arr.sort()
    if n%2 == 0: #even
        mid_idx1 = int(n/2-1)
        mid_idx2 = int(n/2)
        ans = round((arr[mid_idx1] + arr[mid_idx2])/2, 1)
    else:
        mid_idx = math.floor(n/2) #for 0 based indexing
        ans = arr[mid_idx]
    return ans

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(" ")))
    print(mean(n, arr))
    print(median(n, arr))
    print(mode(n, arr))
