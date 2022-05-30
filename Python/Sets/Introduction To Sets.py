def average(array):
    se = set(array)
    k = len(se)
    total = sum(se)
    avg = total/k
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)