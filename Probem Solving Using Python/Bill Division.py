def bonAppetit(bill, k, b):
    n = len(bill)
    sum = 0
    for i in range(n):
        if i != k:
            sum += bill[i]
    a_bill = sum//2
    if a_bill == b:
        print("Bon Appetit")
    else:
        print(b - a_bill)






if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
