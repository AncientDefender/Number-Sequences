# Number Sequences Repository

Welcome to the Number Sequences repository! This project explores various intriguing number sequences, starting with Armstrong numbers and then Happy numbers. Whether you're a math enthusiast or just curious about numbers, you'll find a range of interesting sequences and their properties here.

## Table of Contents

1. [Introduction](#introduction)
2. [Armstrong Numbers](#armstrong-numbers)
3. [Happy Numbers](#happy-numbers)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

Number sequences have fascinated mathematicians for centuries, providing insights into number theory and often revealing surprising properties. This repository aims to catalogue and analyze a variety of number sequences, starting with the classic Armstrong numbers and then followed up with the colourful Happy numbers.

## Armstrong Numbers

### What are Armstrong Numbers?

An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, in a 3-digit number, an Armstrong number is one where:

abc = a<sup>3</sup> + b<sup>3</sup> + c<sup>3</sup>

where \(a\), \(b\), and \(c\) are the digits of the number. 

### Examples

- **153**:  1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup> = 153

- **9474**: 9<sup>4</sup> + 4<sup>4</sup> + 74</sup> + 4<sup>4</sup> = 9474

### Properties

- Armstrong numbers are a special case of numbers that can be expressed as the sum of their digits raised to some power.
- The number of Armstrong numbers in a given digit range is relatively small compared to the total number of numbers in that range.
- There are 89 known Armstrong numbers in base-10

### How to Find Armstrong Numbers

To find Armstrong numbers within a specific range, you can use the following algorithm:

1. Iterate over each number in the desired range.
2. For each number, calculate the sum of its digits each raised to the power of the number of digits.
3. Check if this sum equals the original number.

### Python Program

The repository includes a Python program designed to find Armstrong numbers efficiently. The program is optimized to handle numbers with up to 8 digits comfortably. For larger numbers, such as those with 10 digits, the computation time can be extensive.
This update includes details on the number of Armstrong numbers and notes on computational efficiency for finding these numbers. If you need any more adjustments or additional information, just let me know!

## Happy Numbers

### What are Happy Numbers?

A happy number is a number that, when you replace it with the sum of the squares of its digits and repeat the process, eventually results in the number 1. If the number falls into a loop that does not include 1, it is not a happy number.

### Examples

- **19** is a happy number because:
  - 1<sup>2</sup> + 9<sup>2</sup> = 82
  - 8<sup>2</sup> + 2<sup>2</sup> = 68
  - 6<sup>2</sup> + 8<sup>2</sup> = 100
  - 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
- Since it reaches 1, **19** is happy.

- **70** is a happy number because:
  - 7<sup>2</sup> + 0<sup>2</sup> = 49
  - 4<sup>2</sup> + 9<sup>2</sup> = 97
  - 9<sup>2</sup> + 7<sup>2</sup> = 130
  - 1<sup>2</sup> + 3<sup>2</sup> + 0<sup>2</sup> = 10
  - 1<sup>2</sup> + 0<sup>2</sup> = 1
- Since it reaches 1, **70** is happy.

### Properties

- Non-happy numbers fall into a repeating cycle. A common cycle for non-happy numbers is: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4.
- Every positive integer is either a happy number or not. While there are infinitely many happy numbers, they become less frequent as numbers get larger.
- In base-10, happy numbers follow a specific pattern, but this pattern may vary in other bases.

### How to Find Happy Numbers

To determine if a number is happy:

1. Calculate the sum of the squares of its digits.
2. If the result is 1, the number is happy but, if the result repeats (i.e., you encounter the same number again), it is not happy.
3. Continue the process with the new number until you reach 1 or detect a cycle.

### Python Program
The repository includes a Python program designed to find Happy numbers efficiently. The program will initially find happy numbers from 1 up to 1 million (~30 seconds). Afterwards, there is freedom to input any number and verify whether the number is happy or sad.
You can manually increase the uppper limit for the program by adjusting the two parameters on lines 403 and 404. To change the lower limit, go to line 268 and replace  i  *  chunk_size  +  1 with  i  *  chunk_size  +  **limit** where **limit** is your value. 
This update includes details on the number of Happy numbers and notes on computational efficiency for finding these numbers. If you need any more adjustments or additional information, just let me know!

## Contributing

Contributions are welcome! If you have improvements to the existing content or enhancements to the Python program, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Created by KWThunderRaft  
Date: July 25, 2024
