num = input()
temp = 0
for i in range(0, len(num)):
    # print("i", i)
    c = int(num[i]) * int(num[i]) * int(num[i])
    # print("C", c)
    temp += c
#     print("Temp", temp)
# print(type(temp), type(num))
if temp == int(num):
    print("armstrong")

else:
    print("not armstrong")


