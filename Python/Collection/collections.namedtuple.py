from collections import namedtuple
k = int(input())
det = namedtuple("det",input())
sm = 0
for i in range(k):
    p = input().split()
    st = det(p[0],p[1],p[2],p[3])
    sm += int(st.MARKS)
print(round(sm/k, 2))
    