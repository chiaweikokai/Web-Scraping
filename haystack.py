import re

text = open("regex_sum_297309.txt")

sum = 0
for line in text:
    line = line.rstrip()
    num_list = re.findall('[0-9]+', line)
    if len(num_list) > 0:
        for num in num_list:
            sum += int(num)

print(sum)

