input_word = raw_input("Enter your word: ")

#what characters we have?lower only or both lower and upper case
#Do we also have numbers and special characters?
reversed_word = ""

input_word_array = []
for character in input_word:
    input_word_array.append(character)


#Palindrome probleme
for character in range(len(input_word)-1,-1,-1):
    reversed_word += input_word_array[character]

print reversed_word



#Writing the FOR loop in another way:
reversed_word = ""
for character in input_word:
    reversed_word = "%s%s" % (character,reversed_word)

print reversed_word
