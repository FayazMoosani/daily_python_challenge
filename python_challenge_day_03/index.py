def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  # Check from 2 to square root of num
        if num % i == 0:
            return False
    return True

#Get user input
user_input = int(input("Enter a number to check if it's prime: "))

#Check if the number is prime
if is_prime(user_input):
    print(f"Yes, {user_input} is a prime number.")
else:
    print(f"No, {user_input} is not a prime number.")
