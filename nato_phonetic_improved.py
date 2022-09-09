import pandas


def get_nato_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters from the alphabet please.")
        get_nato_phonetic()
    else:
        print(output_list)


data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

get_nato_phonetic()
