# Завдання 3
# Візьміть файл, в якому є багато англійських слів у рядках. Порахуйте частоту зустрічі кожного слова
# та видрукуйте відсортовано.

with open('exercise3.txt', 'r') as file:
    text_file = file.read()

# split string by spase and delete around punctuation marks like ;:,.!'"? and converse to lower case
text_file = text_file.split()
clear_words = []
for item in text_file:
    clear_word = item.strip(';:,.!"?').strip("'").lower()
    clear_words.append(clear_word)

# create dictionary {word: count} and iterate list of clear words
dictionary_words = dict()
for word in clear_words:
    current_count = dictionary_words.get(word) if dictionary_words.get(word) else 0
    dictionary_words.update({word: current_count + 1})

# sort the list for key [1] - our count in tuple (word, count)
sorted_words = list(dictionary_words.items())
sorted_words.sort(key=lambda x: x[1], reverse=True)

# print words on their count
for word, count in sorted_words:
    print(f'{word} - {count}')
