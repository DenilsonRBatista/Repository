print('Numero de posições')
n = int(input())
arr = sorted(map(int, input().split()))
arr_dup = sorted(list(set(arr)), reverse=True)
print(arr_dup[1])
