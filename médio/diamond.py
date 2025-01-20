def diamond(main_letter: str) -> None:
    main_letter = main_letter.strip().upper()
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if type(main_letter) is not str:
        raise ValueError("This function only accepts strings")

    if len(main_letter) == 1:
        if main_letter not in letters:
            raise ValueError(f'Invalid characters passed to funtion: {main_letter}')
    else:
        invalid_chars = ''
        for char_ in main_letter:
            if char_ not in letters:
                invalid_chars += char_

        if len(invalid_chars) > 0:
            raise ValueError(f'Invalid characters passed to funtion: {invalid_chars}')
        else:
            raise ValueError('This function doesn\'t except more than 1 letter')


    if main_letter == 'A':
        print(main_letter)
        return None


    list_rows = []

    for letter in letters[:letters.index(main_letter)+1]:
        row = ' ' * (letters.index(main_letter) - letters.index(letter))
        row += letter
        if letters.index(letter) != 0:
            row += ' ' * (1 + (letters.index(letter) - 1) * 2)
            row += letter

        list_rows.append(row)


    for row in list_rows[(len(list_rows) - 2)::-1]:
        list_rows.append(row)

    print(*list_rows, sep='\n')
    return None


diamond('a')