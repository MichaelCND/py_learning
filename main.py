from unittest import result


print('work application with files')

#with open('D:/files_for_python/', 'r') as r:
    #print(r.read())

r = int(input())
arr = []
for i in range(r):
    arr.append([int(j) for j in input().split()])
result = ''.join(str(x) for x in arr)
with open('D:/files_for_python/readme.txt', 'a') as a:
    a.write(result)

