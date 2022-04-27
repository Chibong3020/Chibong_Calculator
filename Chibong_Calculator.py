import time

print("Chibong's Epik Calculator")
print(' ')
number_1 = int(input('Enter a number: '))
sign = input('What do you want to do with the numbers? (+, -, x, %): ')
number_2 = int(input('Enter a second number: '))

if sign == '+':
    sum = number_1 + number_2
    print(f'You sum is {sum}')
elif sign == '-':
    subracted_number = number_1 - number_2
    print(f" your answer is {subracted_number}")
elif sign.lower() == 'x':
    multiplied_number = number_1 * number_2
    print(f'Your answer is {multiplied_number}')
elif sign == '%':
    divided_number = number_1 / number_2
    print(f'Your answer is {divided_number}')
elif sign != '+' '-' 'x' '%':
   print("Enter a valid sign, don't make me cry ")
   
time.sleep(3)