import sys

#Input
special_word_no_case = raw_input("Enter your word:")
special_word = special_word_no_case.lower()



#Approach 1: LOOP through the word and see if you can find each character again
print "---------------------------------"
print "Using arrays"
print "---------------------------------"

array_word = []
for letter in special_word:
    array_word.append(letter)

#Complexity O(n^2) -> Who the hell likes that
imperfect_characters = 0
for character in array_word:
    #count occurences of each character
    no_occurences_for_one_char = 0

    for word in array_word:
        if word == character:
            no_occurences_for_one_char += 1
    if no_occurences_for_one_char > 1:
        print "The character \"%s\" is not unique" % character
        no_occurences_for_one_char = 0
        imperfect_characters += 1
        array_word.pop(array_word.index(character))

if imperfect_characters == 0:
    print "All the letters are unique"


#Approach 2: Read each letter and put it into a hashmap/dictionary
print "---------------------------------"
print "Using a dictionary"
print "---------------------------------"

#Complexity: O(n)

character_dictionary = {}
count_correct = 0
for letter in special_word:
    if character_dictionary.has_key(letter):
        character_dictionary[letter] += 1
        count_correct -= 1
    else:
        character_dictionary[letter] = 1
        count_correct += 1

for key in character_dictionary.keys():

    if character_dictionary[key] > 1:
        print "The character \"%s\" is not unique" % key
if count_correct == len(character_dictionary):
    print "The word is perfect as are you"
