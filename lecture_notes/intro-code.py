import words

### Print from an imported object

# print(words.ADJECTIVES)
# for element in words.ADJECTIVES:
#     print (element)
#     for letter in element:
#         print(letter)

### Print string som er Bxxxx Axxxx, fra adjective og nouns 

# a = words.NOUNS[5].title()
# b = words.ADJECTIVES[5].title()
# print(a, b)
# print(a + b) 

# eller 
# print ((words.ADJECTIVES[5].title() + " " + words.NOUNS[5].title()))

### Read a file

with open('data/books/the_sign_of_the_four.txt') as fp:
    all_txt = fp.read()

# print(all_txt)

all_txt = all_txt.replace("\n", " ")
print(all_txt)

for word in all_txt.split():
