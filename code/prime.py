number=[]
for k in range(2,1001):
    number.append(k)

primenumber=number[2:]    

for i in primenumber:
    for j in range(2,i):
        if i%j==0:
            primenumber.remove(i)
            
print primenumber