
# A Python function that tests whether a given string is the same when reversed or not.

a = str(input("Enter a word or words you need to be reversed:"))

# Construct the list of words
words = a.split(' ')

# Construct the list of reversed words
reversed_words = [word[::-1] for word in words]

if set(words) & set(reversed_words):

# Get an intersection of these lists converted to sets

    print(set(words) & set(reversed_words))
    print("The above word/words can be reversed.")
else:

# Where there is no intersection on the lists

    print("The above word/words cannot be reversed OR the set is Empty.")