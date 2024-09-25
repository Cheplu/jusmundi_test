import time
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FrenchNumberConverter:
    """
    A class to convert numbers into their French word representations.

    Supports numbers from 0 to 999,999.
    """

    # Constants for units, tens, hundreds, and special cases
    UNITS = {
        0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre",
        5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf",
        10: "dix", 11: "onze", 12: "douze", 13: "treize", 14: "quatorze",
        15: "quinze", 16: "seize"
    }

    TENS = {
        10: "dix", 20: "vingt", 30: "trente", 40: "quarante", 
        50: "cinquante", 60: "soixante", 70: "soixante-dix",
        80: "quatre-vingts", 90: "quatre-vingt-dix"
    }

    HUNDREDS = {
        100: "cent"
    }

    SPECIAL_CASES = {
        71: "soixante-et-onze",
        81: "quatre-vingt-un",
        91: "quatre-vingt-onze",
        72: "soixante-douze", 73: "soixante-treize", 74: "soixante-quatorze",
        75: "soixante-quinze", 76: "soixante-seize", 77: "soixante-dix-sept",
        78: "soixante-dix-huit", 79: "soixante-dix-neuf",
        82: "quatre-vingt-deux", 83: "quatre-vingt-trois",
        84: "quatre-vingt-quatre", 85: "quatre-vingt-cinq", 
        86: "quatre-vingt-six", 87: "quatre-vingt-sept", 
        88: "quatre-vingt-huit", 89: "quatre-vingt-neuf",
        92: "quatre-vingt-douze", 93: "quatre-vingt-treize",
        94: "quatre-vingt-quatorze", 95: "quatre-vingt-quinze",
        96: "quatre-vingt-seize", 97: "quatre-vingt-dix-sept",
        98: "quatre-vingt-dix-huit", 99: "quatre-vingt-dix-neuf"
    }

    def convert(self, number):
        """
        Converts a number into its French word representation.

        Args:
            number (int): The number to convert. Must be between 0 and 999,999.

        Returns:
            str: The French word representation of the number.

        Raises:
            ValueError: If the number is out of the supported range.
        """
        logging.debug(f"Attempting to convert number: {number}")

        if not isinstance(number, int):
            logging.error(f"Invalid input type: {type(number)}. Expected int.")
            raise TypeError("Input must be an integer")
        
        if number < 0 or number >= 1000000:
            logging.error(f"Number out of supported range: {number}")
            raise ValueError("Number out of supported range")

        if number < 17:
            logging.info(f"Converted {number} to {self.UNITS[number]}")
            return self.UNITS[number]
        elif number in self.SPECIAL_CASES:
            logging.info(f"Special case conversion for {number}: {self.SPECIAL_CASES[number]}")
            return self.SPECIAL_CASES[number]
        elif number < 100:
            return self.convert_tens(number)
        elif number < 1000:
            return self.convert_hundreds(number)
        else:
            return self.convert_thousands(number)

    def convert_tens(self, number):
        """
        Converts numbers from 20 to 99 into their French word representation.

        Args:
            number (int): The number to convert, must be between 20 and 99.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Converting tens for number: {number}")

        tens = number // 10 * 10
        remainder = number % 10

        if remainder == 0:
            logging.info(f"Converted {number} to {self.TENS[tens]}")
            return self.TENS[tens]
        elif number in self.SPECIAL_CASES:
            logging.info(f"Special case conversion for {number}: {self.SPECIAL_CASES[number]}")
            return self.SPECIAL_CASES[number]
        elif remainder == 1 and tens in [20, 30, 40, 50, 60]:  
            result = f"{self.TENS[tens]}-et-un"
            logging.info(f"Converted {number} to {result}")
            return result
        else:
            result = f"{self.TENS[tens]}-{self.UNITS[remainder]}"
            logging.info(f"Converted {number} to {result}")
            return result

    def convert_hundreds(self, number):
        """
        Converts numbers from 100 to 999 into their French word representation.

        Args:
            number (int): The number to convert, must be between 100 and 999.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Converting hundreds for number: {number}")

        hundreds = number // 100
        remainder = number % 100

        if hundreds == 1:
            result = f"cent-{self.convert(remainder)}" if remainder > 0 else "cent"
            logging.info(f"Converted {number} to {result}")
            return result
        else:
            result = f"{self.UNITS[hundreds]}-cents-{self.convert(remainder)}" if remainder > 0 else f"{self.UNITS[hundreds]}-cents"
            logging.info(f"Converted {number} to {result}")
            return result

    def convert_thousands(self, number):
        """
        Converts numbers from 1000 to 999,999 into their French word representation.

        Args:
            number (int): The number to convert, must be between 1000 and 999,999.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Converting thousands for number: {number}")

        thousands = number // 1000
        remainder = number % 1000

        if thousands == 1:
            result = f"mille-{self.convert(remainder)}" if remainder > 0 else "mille"
            logging.info(f"Converted {number} to {result}")
            return result
        else:
            result = f"{self.convert(thousands)}-mille-{self.convert(remainder)}" if remainder > 0 else f"{self.convert(thousands)}-mille"
            logging.info(f"Converted {number} to {result}")
            return result
