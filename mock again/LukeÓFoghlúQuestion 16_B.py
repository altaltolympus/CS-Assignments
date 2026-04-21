#Question 16(b)
#Luke Ó Foghlú | Coláiste Chilliain


from random import *

def random_item(list):
    return list[randint(0, len(list))]


one_syllable = ["dusk", "rain", "cloud", "stars", "mist", "wind", "flame", "stone", "sky"]
two_syllable = ["river", "mountain", "blossom", "autumn", "sunlight", "evening", "winter"]
three_syllable = ["butterfly", "harmony", "whispering", "melody", "reflection"]
four_syllable = ["tranquility", "ephemeral", "illuminate"]
five_syllable = ["a distant thunder", "beneath silent trees","whispers in the grass","moonlight on still waves"]

phrases = [one_syllable, two_syllable, three_syllable, four_syllable, five_syllable]

def haiku_line(length):
    start_syllables = randint(0,4)
    print(f"start_syllables: {start_syllables}")
    end_syllables = length - start_syllables
    
    print(f"end_syllables: {end_syllables}")
    
    start_phrases = phrases[start_syllables]
    print(f"start_phrases: {start_phrases}")
    line = random_item(start_phrases)
    print(f"line: {line}")
    if end_syllables > -1:
        end_phrases = phrases[end_syllables]
        print(f"end_phrases: {end_phrases}")
        line += f" {random_item(end_phrases)}"
        print(f"completed line: {line}")
    return line
        
def generate_haiku():
    print(f"{haiku_line(5)}\n{haiku_line(7)}\n{haiku_line(5)}")
    repeat = input('another? (y/n)\n > ')
    if repeat == "y":
        generate_haiku()

generate_haiku()