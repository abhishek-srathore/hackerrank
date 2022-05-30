if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

s = student_marks.get(query_name)
avg = (s[0]+s[1]+s[2])/3+0.0001
print(format(avg , '.2f'))
