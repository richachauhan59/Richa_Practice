num = input()

for i in range(0, len(num) // 2):
    print(num[i], num[-i-1])
    if num[i] != num[-i - 1]:
        print("Not a Palindrome")
        break
else:
    print("Palindrome")
