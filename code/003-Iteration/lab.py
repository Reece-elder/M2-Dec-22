# Count Vowels Task

word = input("Please enter a word to count vowels: ")
print(word)

vowels_count = 0
vowels = ["a", "e", "i", "o", "u"]

count = 0
# print(len(word)) Length of the word.. 5

# While Loop
# while count < len(word):
#     if word[count] in vowels:
#         vowels_count += 1
#     count += 1

# For Loop
for char in word:
    if char in vowels:
        vowels_count += 1

print(f"Number of vowels in {word} is {vowels_count}")

# While word_finished is false