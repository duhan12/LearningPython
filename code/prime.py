primenumber = list(range(2,1001))
number_=[]

for i in range(2,1001):
    for j in range(2,i):
        if i%j==0:
            number_.append(i)
            break

for l in number_:
    if l in primenumber:
        primenumber.remove(l)
print(primenumber)
