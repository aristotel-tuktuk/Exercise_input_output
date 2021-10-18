#Задача «Следующее и предыдущее»
#Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
first_number = int(input())
next_number = str(first_number + 1)
previous_number = str(first_number - 1)
print('The next number for the number ' + str(first_number) + ' is ' + next_number + '.')
print('The previous number for the number ' + str(first_number) + ' is ' + previous_number + '.')

# Второй вариант решения
n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n + 1) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(n - 1) + '.')