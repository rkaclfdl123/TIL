num = list(map(int, input().split()))
# num = [4,4]
x, y, direction = input().split()
x = int(x)
y = int(y)
direction = int(direction)
# x,y,direction =1,1,0
A = []
for i in range(num[0]):
    A.append(list(map(int, input().split())))

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
count = 1
turntime = 0


def turnleft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


A[x][y] = 1
while (True):
    turnleft()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if A[ny][nx] == 1:
        turntime += 1


    elif (A[nx][ny] == 0):
        x = nx
        y = ny
        count += 1
    else:
        print("error")
    if turntime == 4:
        if (A[nx][ny] == 0):
            x = nx
            y = ny
        else:
            break

        turntime = 0

print(count)