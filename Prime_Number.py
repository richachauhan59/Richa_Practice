num = int(input())

if num > 1:
    for i in range(2, num//2):
        if num % i == 0:
            print("number is not prime")
            break
    else:
        print("Prime")
else:
    print("number is not prime")
