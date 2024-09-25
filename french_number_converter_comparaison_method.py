import time
import random
import logging
import matplotlib.pyplot as plt

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FrenchNumberConverterComparaison:
    """
    A class for comparing two methods of converting numbers to their French word representation:
    basic and optimized methods.
    """

    # Constants for units and tens
    UNITS = {
        0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 
        7: "sept", 8: "huit", 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 
        13: "treize", 14: "quatorze", 15: "quinze", 16: "seize", 17: "dix-sept", 
        18: "dix-huit", 19: "dix-neuf"
    }
    
    TENS = {
        10: "dix", 20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 
        60: "soixante", 70: "soixante-dix", 80: "quatre-vingts", 90: "quatre-vingt-dix"
    }

    def convert_units(self, number):
        """
        Converts a number less than 20 to its French word representation.

        Args:
            number (int): A number between 0 and 19.

        Returns:
            str: The French word for the given number.
        """
        logging.debug(f"Converting units: {number}")
        return self.UNITS[number]

    def convert_tens_basic(self, number):
        """
        Basic method to convert numbers from 10 to 99 into French.

        Args:
            number (int): A number between 10 and 99.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Basic conversion for tens: {number}")
        if number < 17:
            return self.UNITS[number]
        elif number < 20:
            return f"dix-{self.UNITS[number - 10]}"
        elif number < 70:
            tens = (number // 10) * 10
            remainder = number % 10
            if remainder == 1 and tens != 80:
                return f"{self.TENS[tens]}-et-un"
            return f"{self.TENS[tens]}-{self.UNITS[remainder]}" if remainder > 0 else self.TENS[tens]
        elif number < 80:
            remainder = number - 60
            return f"soixante-{self.convert_tens_basic(remainder)}"
        elif number < 100:
            remainder = number - 80
            if remainder == 0:
                return self.TENS[80]
            elif remainder <= 19:
                return f"quatre-vingt-{self.UNITS[remainder]}"

    def convert_tens_optimized(self, number):
        """
        Optimized method to convert numbers from 10 to 99 into French.

        Args:
            number (int): A number between 10 and 99.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Optimized conversion for tens: {number}")
        if number < 17:
            return self.UNITS[number]
        elif number < 20:
            return f"dix-{self.UNITS[number - 10]}"
        elif number < 70:
            tens = (number // 10) * 10
            remainder = number % 10
            if remainder == 1 and tens != 80:
                return f"{self.TENS[tens]}-et-un"
            return f"{self.TENS[tens]}-{self.UNITS[remainder]}" if remainder > 0 else self.TENS[tens]
        elif number < 80:
            remainder = number - 60
            return f"soixante-{self.convert_tens_optimized(remainder)}"
        elif number < 100:
            remainder = number - 80
            if remainder == 0:
                return self.TENS[80]
            elif remainder <= 19:
                return f"quatre-vingt-{self.UNITS[remainder]}"

    def convert_hundreds(self, number):
        """
        Converts numbers from 100 to 999 into French.

        Args:
            number (int): A number between 100 and 999.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Converting hundreds: {number}")
        hundreds = number // 100
        remainder = number % 100
        if hundreds == 1:
            return f"cent-{self.convert_tens_basic(remainder)}" if remainder > 0 else "cent"
        else:
            return f"{self.UNITS[hundreds]}-cents-{self.convert_tens_basic(remainder)}" if remainder > 0 else f"{self.UNITS[hundreds]}-cents"

    def convert_thousands(self, number):
        """
        Converts numbers from 1000 to 999,999 into French.

        Args:
            number (int): A number between 1000 and 999,999.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Converting thousands: {number}")
        thousands = number // 1000
        remainder = number % 1000

        if thousands >= 1000:
            return f"{self.convert_thousands(thousands)}-mille-{self.convert_hundreds(remainder)}" if remainder > 0 else f"{self.convert_thousands(thousands)}-mille"
        
        if thousands == 1:
            return f"mille-{self.convert_hundreds(remainder)}" if remainder > 0 else "mille"
        else:
            return f"{self.convert_hundreds(thousands)}-mille-{self.convert_hundreds(remainder)}" if remainder > 0 else f"{self.convert_hundreds(thousands)}-mille"

    def convert_basic(self, number):
        """
        Basic method to convert numbers to French word representation.

        Args:
            number (int): A number between 0 and 999,999.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Basic conversion for number: {number}")
        if number < 100:
            return self.convert_tens_basic(number)
        elif number < 1000:
            return self.convert_hundreds(number)
        else:
            return self.convert_thousands(number)

    def convert_optimized(self, number):
        """
        Optimized method to convert numbers to French word representation.

        Args:
            number (int): A number between 0 and 999,999.

        Returns:
            str: The French word representation of the number.
        """
        logging.debug(f"Optimized conversion for number: {number}")
        if number < 100:
            return self.convert_tens_optimized(number)
        elif number < 1000:
            return self.convert_hundreds(number)
        else:
            return self.convert_thousands(number)


def compare_conversion_methods(converter, numbers):
    """
    Compare the time taken by the basic and optimized conversion methods.

    Args:
        converter (FrenchNumberConverterComparaison): The converter object.
        numbers (list): A list of numbers to be converted.

    Returns:
        tuple: Time taken by the basic and optimized methods.
    """
    #logging.info(f"Starting comparison of conversion methods for numbers: {numbers}")

    start_basic = time.perf_counter()
    basic_results = [converter.convert_basic(n) for n in numbers]
    end_basic = time.perf_counter()
    #logging.info(f"Basic conversion completed in {end_basic - start_basic:.6f} seconds")

    start_optimized = time.perf_counter()
    optimized_results = [converter.convert_optimized(n) for n in numbers]
    end_optimized = time.perf_counter()
    #logging.info(f"Optimized conversion completed in {end_optimized - start_optimized:.6f} seconds")

    time_basic = end_basic - start_basic
    time_optimized = end_optimized - start_optimized

    return time_basic, time_optimized
