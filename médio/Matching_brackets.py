"""
Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all
pairs are matched and nested correctly. Any other characters should be ignored. For example, "{what is (42)}?" is
balanced and "[text}" is not.
"""
def bracketeer(word:str) -> bool:

    def relative_closing_char(char_:str) -> str:
        match char_:
            case '[':
                return ']'
            case '{':
                return '}'
            case '(':
                return ')'

    opening_characters = '[{('
    closing_characters = '}])'

    searching_for_sequence = ''
    for char in word:
        # if an opening character is found
        if char in opening_characters:
            # we are going to look for its relative closing character
            searching_for_sequence += relative_closing_char(char)

        # if a closing character is found
        if char in closing_characters:
            # and this character is not what we are currently looking for
            if char != searching_for_sequence[-1]:
                # then the nesting string passed is not balanced
                return False
            # and this character IS what we are currently looking for
            else:
                # then remove this character from the searching_for_sequence
                searching_for_sequence = searching_for_sequence[:-1]


    return True

print(bracketeer('{what is [(42)]}'))