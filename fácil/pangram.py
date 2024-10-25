def is_pangram(phrase: str):

    phrase = phrase.lower()

    alfabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    for letter in phrase:
        if letter in alfabet:
            letter_index = alfabet.index(letter)
            del alfabet[letter_index]

    if len(alfabet) == 0:
        return True
    else:
        return False


print(is_pangram("abcdefghi jklmno p qrstuvwxyz"))
