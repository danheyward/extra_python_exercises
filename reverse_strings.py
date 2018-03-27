# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***
missy = 'Put my thing down, flip it and reverse it '

def reverse_string(string):
    string = string.split(' ')
    flip_array = []
    for word in range(len(string)):
        flip = string[word][::-1]
        flip_array.insert(len(flip_array), flip)
    new_sentence = ' '
    new_sentence = new_sentence.join(flip_array)
    print(new_sentence)

reverse_string(missy)
