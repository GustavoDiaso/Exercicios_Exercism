def all_your_base(number: int, input_base: int, output_base: int):
    if input_base >= 2 and output_base >= 2:
        number = str(number)

        for char in number:
            if int(char) < 0 or int(char) > input_base:
                raise ValueError("Input and output bases must be higher or equal to 2")

        number_in_base10 = 0
        reversed_number = number[::-1]

        for i in range(0, len(reversed_number)):
            number_in_base10 += int(reversed_number[i]) * (input_base**i)

        rest = ""

        while number_in_base10 // output_base != 0:
            rest += f"{number_in_base10 % output_base}"
            number_in_base10 = number_in_base10 // output_base

        rest += f"{number_in_base10 % output_base}"

        number_to_output_base = rest[::-1]

        return number_to_output_base

    else:
        raise ValueError("Input and output bases must be higher or equal to 2")


all_your_base(10, 10, 2)
