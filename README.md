# French Number Converter

This is a Python program that converts numbers from 0 to 999,999 into their French equivalents and a comparison of two methods : 

## French Number Converter
This is a Python program that converts numbers from 0 to 999,999 into their French equivalents.

### Features
- Converts numbers from 0 to 999,999 into French
- Handles special cases such as numbers ending in 1, 11, 111, etc.
- Uses a dictionary-based approach for efficient conversion

### Usage
Run the program using python french_number_converter.py
The program will output the French equivalent of the number of the data set asked in the kata

### Requirements
Python 3.9

### Notes
This program uses a dictionary-based approach to convert numbers into French. **This approach is efficient but may not be suitable for very large numbers.**
The program handles special cases such as numbers ending in 1, 11, 111, etc.


## French Number Converter with Performance Comparison
This is a Python program that convert numbers into their french equivalents with two differents methods.
The purpose is to see the gain.

### Features 
- The program take 100 times 45 numbers between 0 and 999999, we save the seconds for each number using the two methods and at this end show to gain or lost for the optimized method.
- The program make a plot with the 100 gain or lost.
- Warning : this is a random seed. Each time will be a random one.

### Usage
Run the program using python french_number_converter_comparaison_method.py
The program will output the seconds needed to do the two methods and show us the gain or the lost of the optimized method.
The program save a plot in your current directory.

### Requirements
- Python 3.9
- matplotlib

### Notes
This program uses a dictionary-based approach to convert numbers into French. This approach is efficient but may not be suitable for very large numbers.
The program compares the performance of two different conversion methods: basic and optimized.
The optimized method is faster but may be more complex to implement.


## Installation

1. Clone the repository:
```bash
git clone https://github.com/Cheplu/jusmundi_test.git
cd french_number_converter
```
2. install package : 
`pip install -r requirements.txt`

3. Usage : 
`python main.py`

4. Usage of test :
`python test_french_number_converter.py`


### use of llm
Here we have the prompt command i used on Llama 3.1 8B (i try it because it's the only one i have my local computer, and i wanted to make a comparaison with mistral, but time is missing for me)
#### at the begining
`create a dictionnary of the number bellow with Constants in UPPERCASE`
#### for the code(loop)
`create a converts numbers definition from 20 to 99 into their French word representation with the dictionnary below`
#### after creating the code
`On the code below, give me an optimize method to do the same result`
#### for the loop
`with the code below, give me a code able to a perform 100 comparisons with 48 random numbers each time taken between 0 and 999999`
#### for the both code
`to this code, add docstring`
#### on the pythons files
`add me some logging`
#### on the plot
`improve readability of this plot`


## Plot
The program made a plot and save it in your current directory.
the plot is a two line charts where each line is one of the two methods. It's a vizualisation of the 100 random try. When you see a peak, it's seems to be a random seed with only big numbers.