num_list = []
nums = list(range(0, 101))
for num in nums:
    if num % 5 == 0 and num % 7 ==0:
        num_list.append(num)
print(num_list)
