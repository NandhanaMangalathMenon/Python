def is_perfect(num):
    # 1 is not a perfect number
    if num < 2:
        return False
    
    sum_of_divisors = 0
    
    # find all divisors except the number itself
    for i in range(1, num):
        if num % i == 0:   # if i divides num completely
            sum_of_divisors += i
    
    # check if sum of divisors equals the number
    if sum_of_divisors == num:
        return True
    else:
        return False



n = int(input("Enter a number: "))

if is_perfect(n):
    print(n, "is a Perfect number!")
else:
    print(n, "is not a Perfect number.")
