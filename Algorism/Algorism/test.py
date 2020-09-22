str1 = "1000000000"
data = list(map(int,str1))

print(data)

#
ck = True
str2 = ""
while ck:
    for i in range(len(str1)):

        if i == 1 and data[i] == 0:
            data[0] -= 1
        if data[i] == 0:
            data[i] = 9

    ck = False
    break

res = ""
for i in range(len(data)):
    if i == 0 and data[0] == 0:
        continue
    res += str(data[i])

resInt = 1
for i in data:
    resInt *= i

result = ""
for i in range(len(data)):
    if i == 0 and data[0] == 0:
        continue
    if i == 0:
        result += str(data[i])
    elif i == 1 and 1 < len(str1):
        result += str(data[i]-1)
    else:
        result += "9"

resInt2 = 1
for i in result:
    resInt2 *= int(i)
print(resInt2)
print(result)
print(resInt)
print(res)
print(data)

if resInt > resInt2:
    print(resInt)
else:
    print(resInt2)



