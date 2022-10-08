n = [0, 1, 0, 1, 0, 0, 0, 1]
p = [0, 0, 1, 1, 0, 0, 1, 1]
r = []

c = False
for i in range(7, -1, -1):
    a = n[i]
    b = p[i]
    unite = (a and not(b) and not(c)) or\
        (not(a) and b and not(c)) or\
        (not(a) and not(b) and c) or\
        (a and b and c) ### somme
    r = [int(unite)] + r
    c = (a and b) or (b and c) or (a and c) ### retenue
r = [int(c)] + r

print(r)


a = "01010001"
b = "00110011"

sum = bin(int(a, 2) + int(b, 2))

print(sum[2:])
print (sum)
