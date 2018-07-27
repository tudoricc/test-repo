input_word = raw_input("Enter your words with spaces in between: ")

# Are  we talking only alphanumerical character but do we also have "special" characters
#Write a method to replace all spaces in a string with '%20'
def replace_characters(where_to_replace,what_to_replace):
    modified_string = ""
    for character in where_to_replace:
        if character == what_to_replace:
            modified_string += "\%20"
        else:
            modified_string += character
    print "Function result: " + modified_string




modified_word = input_word.replace(" ","\%20")
#print modified_word
replace_characters(input_word," ")
