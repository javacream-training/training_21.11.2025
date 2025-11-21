mytext = 'Das ist ein langer Text mit verschiedenen Wörtern'

charcount_total = len(mytext)
print(f'Total number of characters: {charcount_total}')

count_spaces = mytext.count(' ')
charcount_without_spaces = mytext.replace(' ', '')
charcount_without_spaces = len(charcount_without_spaces)
print(f'Total number of characters without spaces: {charcount_without_spaces}')
print(f'Total number of characters without spaces: {charcount_total - count_spaces}')

count_a = mytext.count('a')
print(f'Total count of character "a": {count_a}')

vowels = ['a','e','i','o','u']
count_vowels = 0
for vowel in vowels:
    count_vowels = count_vowels + mytext.count(vowel)
print(f'Total number of vowels: {count_vowels}')

count_words = count_spaces + 1
print(f'Total number of words: {count_words}')
count_words = mytext.split(' ')
count_words = len(count_words)
print(f'Total number of words: {count_words}')
