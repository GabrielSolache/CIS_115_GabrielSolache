def word_frequuency(sentence):
    #crate an empty dictionary to store word counta
    frequency = {}
    #split the sentence into words using split()
    words = sentence.split()
    #loop through each word in the words list
    for word in words:
        #if the word is already in the dictionary, increment its count
        #otherwise, add the word to the dictionary with a count of 1
        frequency[word] = frequency.get(word, 0) + 1
        #return the dictionary containing word frequencies
        return frequency
#ask the user to enter a sentence
sentence = input("Enter a sentence: ")
#call the function and print the result
print("word frequencies:")