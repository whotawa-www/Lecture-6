# TODO: Вставить сюда код задачи 2.
n = int(input())
total_sum = 0

for _ in range(n):
	number = int(input())
	if number % 6 == 0 and number % 10 == 4:
		total_sum += number
print(total_sum)
