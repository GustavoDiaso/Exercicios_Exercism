"""
band values:

Black: 0
Brown: 1
Red: 2
Orange: 3
Yellow: 4
Green: 5
Blue: 6
Violet: 7
Grey: 8
White: 9

tolerance values:

Grey - 0.05%
Violet - 0.1%
Blue - 0.25%
Green - 0.5%
Brown - 1%
Red - 2%
Gold - 5%
Silver - 10%

"""

def resistor_information(*bands: str) -> str:

    def ohmns_in_resistor(bands_list: list) -> str:
        """returns the amount of ohmns in the resistor according to the given bands in the following pattern:
        (amount of ohmns) + suffix + ohmns"""

        band_values = {
            "black": 0,
            "brown": 1,
            "red": 2,
            "orange": 3,
            "yellow": 4,
            "green": 5,
            "blue": 6,
            "violet": 7,
            "grey": 8,
            "white": 9
        }

        ohmns_ =  ''

        if len(bands_list) < 3:
            for band_color in bands_list:
                ohmns_ += f'{band_values[band_color]}'

            ohmns_ = int(ohmns_)

        if len(bands_list) == 3:

            for index in range(0,2):
                ohmns_ += f'{band_values[bands_list[index]]}'

            ohmns_ = int(ohmns_)
            multiplier_ = band_values[bands_list[-1]]
            ohmns_ = ohmns_ * 10 ** multiplier_

        elif len(bands_list) >= 4:

            for index in range(0, len(bands_list) - 2):
                ohmns_ += f'{band_values[bands_list[index]]}'

            ohmns_ = int(ohmns_)
            multiplier_ = band_values[bands_list[-2]]
            ohmns_ = ohmns_ * 10 ** multiplier_


        suffix = ''

        if ohmns_ in range(10 ** 3, 10 ** 6):
            suffix = 'kilo'
            ohmns_ = ohmns_ / 10 ** 3
        elif ohmns_ >= 10 ** 6:
            suffix = 'mega'
            ohmns_ = ohmns_ / 10 ** 6


        return f'{ohmns_} {suffix}ohmns'




    if len(bands) in range(1, 6):

        bands = [band.lower() for band in bands]
        ohmns = ohmns_in_resistor(bands)

        if len(bands) >= 4:
            tolerance_percentage_values = {
                "grey": 0.05,
                "violet": 0.1,
                "blue": 0.25,
                "green": 0.5,
                "brown": 1,
                "red": 2,
                "gold": 5,
                "silver": 10
            }

            tolerance = tolerance_percentage_values[bands[-1]]
            return f'{ohmns} ±{tolerance}%'

        else:
            return ohmns







print(resistor_information("orange", "BLUE"))