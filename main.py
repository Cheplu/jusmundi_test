import logging
from french_number_converter_comparaison_method import FrenchNumberConverterComparaison, compare_conversion_methods
from french_number_converter import FrenchNumberConverter
import time
import random
import matplotlib.pyplot as plt

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the main function.")

    # Test the FrenchNumberConverter class
    numbers = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 
               200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 
               11111, 12345, 123456, 654321, 999999]

    converter = FrenchNumberConverter()

    # Measure the start time
    start_time = time.time()

    # Process all numbers
    for number in numbers:
        logging.debug(f"Converting number: {number}")
        result = converter.convert(number)
        logging.info(f"{number}: {result}")

    # Measure the end time
    end_time = time.time()

    # Calculate and log total elapsed time
    elapsed_time = end_time - start_time
    logging.info(f"Total time taken for FrenchNumberConverter: {elapsed_time} seconds")

    logging.info("Next Steps: Consider optimizing for larger datasets.")

    # Test the FrenchNumberConverterComparaison class
    logging.info("Starting the comparison between basic and optimized conversion methods.")
    
    converter_comparaison = FrenchNumberConverterComparaison()
    total_basic_time = 0
    total_optimized_time = 0

    basic_list = []
    optimized_list = []

    # Perform 100 comparisons with 48 random numbers each time
    for i in range(100):
        logging.debug(f"Iteration {i+1}: Generating random numbers.")
        
        # Generate 48 random numbers between 0 and 999999
        numbers = [random.randint(0, 999999) for _ in range(48)]

        # Compare conversion methods and measure time
        logging.debug("Comparing conversion methods.")
        time_basic, time_optimized = compare_conversion_methods(converter_comparaison, numbers)

        # Accumulate the total time for both methods
        total_basic_time += time_basic
        total_optimized_time += time_optimized

        basic_list.append(time_basic)
        optimized_list.append(time_optimized)

        logging.debug(f"Time for basic method: {time_basic:.6f} seconds, optimized method: {time_optimized:.6f} seconds.")

    # Create the plot
    logging.info("Creating comparison plot.")
    x1 = list(range(1, 101))

    # Create the plot with improved readability
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.plot(x1, basic_list, label='Basic Calculation', linestyle='-', marker='o', color='blue')
    plt.plot(x1, optimized_list, label='Optimized Calculation', linestyle='--', marker='s', color='red')

    # Add a title and labels to the x and y axes
    plt.title('Comparison of Basic and Optimized Calculation Methods')
    plt.xlabel('Iteration Number')
    plt.ylabel('Values')

    # Add a legend
    plt.legend(loc='upper right', fontsize=12)

    # Add grid lines for better readability
    plt.grid(True, linestyle='--', alpha=0.5)

    # Save plot
    plot_filename = 'Comparison_plot.png'
    plt.savefig(plot_filename)
    logging.info(f"Comparison plot saved as {plot_filename}.")

    # Display total time taken by both methods after 100 comparisons
    logging.info(f"Total time taken by Basic Conversion after 100 comparisons: {total_basic_time:.6f} seconds")
    logging.info(f"Total time taken by Optimized Conversion after 100 comparisons: {total_optimized_time:.6f} seconds")
    
    # Display gain
    difference = total_basic_time - total_optimized_time
    percentage_difference = (difference / total_optimized_time) * 100
    logging.info(f"The percentage difference between {total_basic_time:.6f} and {total_optimized_time:.6f} is: {percentage_difference:.3f}%")

if __name__ == "__main__":
    main()
