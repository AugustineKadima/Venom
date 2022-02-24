
'''
Given an array of words, write a function that reverses the words while maintining
their positions
input = ["python","javascript","angular"]
output = ["nohtyp","tpircsavaj","ralugna"]
'''
# LIST COMPREHENSION

# Pseudocode
# functiom
# loop through each element
# revearse each element in the array
# print revearsed array

def reverse_words_in_array(array_of_words):
    # Loop  through the outer array that contains all words
    for i in range(len(array_of_words)):

        # Convert each word into a character array
        charArray = list(array_of_words[i])
        # Find the length of each word within the array
        n = len(array_of_words[i])
        
        # Declare a variale to store the reversed word
        reverseword = ""

        # loop through the inner array to access each character and append the last letter to reverseword
        for j in range(n):
            reverseword += charArray[n - 1]
            n -= 1
        
        # Replace the word in the outer array with the reversed word
        array_of_words[i] = reverseword

    # Return array of words after all words have een reversed
    return array_of_words

# Call the function and store the output in a variable result
result = reverse_words_in_array(["python","javascript","angular"])

# print result
print(result)
            

