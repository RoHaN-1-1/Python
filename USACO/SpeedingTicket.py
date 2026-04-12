N = 3
M = 3
inp = [[40,75],[50,35],[10,45],[40,76],[20,30],[40,40]]

limit = []
for i in range(N):
    length = inp[i][0]
    speed = inp[i][1]
    limit.extend([speed] * length)
bessie = []
for i in range(N,N+M):
    length = inp[i][0]
    speed = inp[i][1]
    bessie.extend([speed] * length)
max_over = 0
for i in range(100):
    over = bessie[i] - limit[i]
    if over > max_over:
        max_over = over
print(max_over)
