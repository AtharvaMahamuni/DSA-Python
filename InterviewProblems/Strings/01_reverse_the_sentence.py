
def reverse_the_sentence(sentence):

    words = sentence.split(" ")

    sentence = " ".join(reversed(words))

    return sentence

print(reverse_the_sentence("Hello I am Atharva"))