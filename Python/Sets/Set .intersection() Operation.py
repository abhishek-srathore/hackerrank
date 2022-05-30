# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
l1 = input().split(" ")
n2 = int(input())
l2 = input().split(" ")

s1 = set(l1)
s2 = set(l2)
s3 = (s1&s2)
print(len(s3))
