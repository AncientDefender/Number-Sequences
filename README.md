# Number Sequences Repository

Welcome to the Number Sequences repository! This project explores various intriguing number sequences, starting with Armstrong numbers. Whether you're a math enthusiast or just curious about numbers, you'll find a range of interesting sequences and their properties here.

## Table of Contents

1. [Introduction](#introduction)
2. [Armstrong Numbers](#armstrong-numbers)
3. [Python Program](#python-program)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

Number sequences have fascinated mathematicians for centuries, providing insights into number theory and often revealing surprising properties. This repository aims to catalog and analyze a variety of number sequences, starting with the classic Armstrong numbers.

## Armstrong Numbers

### What are Armstrong Numbers?

An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, in a 3-digit number, an Armstrong number is one where:

\[ abc = a^3 + b^3 + c^3 \]

where \(a\), \(b\), and \(c\) are the digits of the number. 

### Examples

- **153**: \(1^3 + 5^3 + 3^3 = 153\)
- **9474**: \(9^4 + 4^4 + 7^4 + 4^4 = 9474\)

### Properties

- Armstrong numbers are a special case of numbers that can be expressed as the sum of their digits raised to some power.
- The number of Armstrong numbers in a given digit range is relatively small compared to the total number of numbers in that range.
- **Count of Armstrong Numbers**: There are 89 known Armstrong numbers.

### How to Find Armstrong Numbers

To find Armstrong numbers within a specific range, you can use the following algorithm:

1. Iterate over each number in the desired range.
2. For each number, calculate the sum of its digits each raised to the power of the number of digits.
3. Check if this sum equals the original number.

## Python Program

The repository includes a Python program designed to find Armstrong numbers efficiently. The program is optimized to handle numbers with up to 8 digits comfortably. For larger numbers, such as those with 10 digits, the computation time can be extensive.
This update includes details on the number of Armstrong numbers and notes on computational efficiency for finding these numbers. If you need any more adjustments or additional information, just let me know!

## Contributing

Contributions are welcome! If you have improvements to the existing content or enhancements to the Python program, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
