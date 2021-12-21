number = []
sums1 = 0
sums2 = 0

for i in range(1, 1001):
    if i % 2 != 0:
        number.append(i ** 3)

for idx in range(len(number)):
    num_sum = 0
    j = number[idx]
    while j:
        num_sum += j % 10
        j = j // 10
        if num_sum % 7 == 0:
            sums1 += number[idx]
        number[idx] += 17
        num_sum = 0
        j = number[idx]
        while j:
            num_sum += j % 10
            j = j // 10
        if num_sum % 7 == 0:
            sums2 += number[idx]
print(sums1)
print(sums2)



    
