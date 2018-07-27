

#awbasdasdasdasd - longest non-repeating
#What od you understand when saying string? human printable characters/letters and numbers?
#Where do we read the string from?


input_string='abbac'
longest_substring=""

#Complexity max O(n^2)
for index_letter in range(0,len(input_string)):
    #For each letter try and create a no duplicate letters word
    print input_string[index_letter]
    temporrary_string=str(input_string[index_letter])
    for following_index_letter in range(index_letter+1,len(input_string)):
        if input_string[following_index_letter] not in temporrary_string:
            temporrary_string+=str(input_string[following_index_letter])
            if len(temporrary_string)>len(longest_substring):
                longest_substring = temporrary_string
        if input_string[following_index_letter] in temporrary_string:
            break




#sets
i = 0
j = 1
n = len(input_string)
while i < n and j < n and i < j:
    print i
    print j
    letter_set_substring=set()
    letter_set_substring.add(index_letter)
    i = i+1
    j = j + 1

print longest_substring
