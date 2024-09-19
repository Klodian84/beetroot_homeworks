# Function to count word occurrences
def count_words(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:

        word = word.lower()

        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1

    return word_count


sentence = input("Enter a sentence: ")

word_occurrences = count_words(sentence)

print(word_occurrences)
