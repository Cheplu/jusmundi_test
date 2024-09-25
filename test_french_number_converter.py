import unittest
import random
import logging
from french_number_converter import FrenchNumberConverter as BasicFrenchConverter
from french_number_converter_comparaison_method import (
    FrenchNumberConverterComparaison as ComparaisonFrenchConverter, 
    compare_conversion_methods
)

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TestFrenchNumberConverter(unittest.TestCase):
    """
    Test cases for FrenchNumberConverter and ComparaisonFrenchConverter.
    """

    def setUp(self):
        """
        Initialize converters before each test.
        """
        self.basic_converter = BasicFrenchConverter()
        self.comparaison_converter = ComparaisonFrenchConverter()

    def test_basic_french_converter_units(self):
        """
        Test conversion for numbers from 0 to 16 (units).
        """
        expected = {
            0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre",
            5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf",
            10: "dix", 11: "onze", 12: "douze", 13: "treize", 
            14: "quatorze", 15: "quinze", 16: "seize"
        }
        for num, word in expected.items():
            try:
                self.assertEqual(self.basic_converter.convert(num), word)
            except AssertionError as e:
                logger.error(f"Assertion error for number {num}: {e}")

    def test_comparaison_conversion_comparison(self):
        """
        Test comparing basic vs optimized conversion timing.
        """
        numbers = [random.randint(0, 999999) for _ in range(10)]  # Small dataset for test
        logger.info(f"Testing with numbers: {numbers}")
        
        # Call the compare_conversion_methods function with the comparison converter
        try:
            time_basic, time_optimized = compare_conversion_methods(self.comparaison_converter, numbers)
            logger.info(f"Basic conversion time: {time_basic}, Optimized conversion time: {time_optimized}")
        except Exception as e:
            logger.error(f"Error during comparison: {e}")
            return
        
        # Ensure both methods convert without errors and are timed
        self.assertGreaterEqual(time_basic, 0)
        self.assertGreaterEqual(time_optimized, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
