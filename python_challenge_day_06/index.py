# Day_06

try:
    print("Palindrome mini project \n")
    num_int = int(input("Enter Integer Number : "))
    binary_num = bin(num_int)[2:]

    print(f"Binary Representation: {binary_num}")
    # Check if the binary representation is a palindrome
    print("Palindrome ✅ " if binary_num == binary_num[::-1] else "Not a palindrome ❌")
except ValueError:
    # Handle the case where the input is not an integer
    print("Invalid Input! Please Enter Integer Number ❌.")