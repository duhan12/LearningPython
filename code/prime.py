number=[]
for k in range(2,1001):
    number.append(k)
primenumber=number[:]
number_=[]

for i in primenumber:
    for j in range(2,i):
        if i%j==0:
            number_.append(i)

for l in number_:
    if l in primenumber:
        primenumber.remove(l)
print primenumber