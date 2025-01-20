from num2binary import num2binary

def secret_handshake(num: int) -> list[str]:
    binary_num:str = num2binary(num)

    actions_based_on_number_place = {
        0: 'wink',
        1: 'double blink',
        2: 'close your eyes',
        3: 'jump'
    }

    secret_hanshake_list = []

    if len(binary_num) >= 5:
        last_five_digits = binary_num[-5:]

        digit_position = 0
        for digit in last_five_digits[::-1]:
            if digit_position == 4:
                break

            if digit == '1':
                secret_hanshake_list.append(actions_based_on_number_place[digit_position])

            digit_position+=1

        if last_five_digits[0] == '1':
            secret_hanshake_list = secret_hanshake_list[::-1]

    else:
        last_five_digits = binary_num

        digit_position = 0
        for digit in last_five_digits[::-1]:
            if digit == '1':
                secret_hanshake_list.append(actions_based_on_number_place[digit_position])

            digit_position += 1


    return secret_hanshake_list

print(secret_handshake(2))
