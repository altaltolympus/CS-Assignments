#Question 16(b)
#Luke Ó Foghlú | Coláiste Chilliain


from random import *

def random_item(list):
    return list[randint(0, len(list)-1)]


one_syllable = ["dusk", "rain", "cloud", "stars", "mist", "wind", "flame", "stone", "sky"]
two_syllable = ["river", "mountain", "blossom", "autumn", "sunlight", "evening", "winter"]
three_syllable = ["butterfly", "harmony", "whispering", "melody", "reflection"]
four_syllable = ["tranquility", "ephemeral", "illuminate"]
five_syllable = ["a distant thunder", "beneath silent trees","whispers in the grass","moonlight on still waves"]

phrases = [one_syllable, two_syllable, three_syllable, four_syllable, five_syllable]

def haiku_line(length):
    line = ""
    length_distribution = []
    while sum(length_distribution) < length:
        length_distribution.append(randint(1, min(length - sum(length_distribution), 5)))
    for phrase_length in length_distribution:
        phrase_length -= 1
        line += f" {random_item(phrases[phrase_length])}"
    return line
        
def generate_haiku():
    print(f"\n{haiku_line(5)}\n{haiku_line(7)}\n{haiku_line(5)}")
    repeat = input('another? (y/n)\n > ')
    if repeat == "y":
        generate_haiku()

generate_haiku()