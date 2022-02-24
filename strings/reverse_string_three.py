def reverse_words_in_array(array_of_words):
    for i in range(len(array_of_words)):
        
        charArray = list(array_of_words[i])
        n = len(charArray)
        print(charArray)
        temp = charArray[n - 1]
        for j in range(n):
            
            charArray[n - 1] = charArray[j]
            charArray[j] = temp
            n -= 1

        print("----",charArray)

result = reverse_words_in_array(["python","javascript","angular"])

# print result
print(result)
            