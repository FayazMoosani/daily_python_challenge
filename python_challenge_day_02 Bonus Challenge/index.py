# Day_02_Python_Daily_Challenge_Bonus_Challenge

user_input = input ("Enter Your Sentence: ")
words = user_input.split()
words_count = len(words)
print(f"{user_input.upper()} Number of words:", words_count ,"\n")

words = user_input.split()
reverse_text = words.reverse()
reverse_text = ' '.join(words)
print(f"Reverse Text is : {reverse_text}","\n")