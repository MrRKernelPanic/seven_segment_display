![SevenSegDisplay](https://cdn.pixabay.com/photo/2019/10/01/09/18/tm1637-4517661_960_720.png)
# Seven Segment Display
An implementation of a seven segment display representation using ASCII characters to display digits.
This attempt was created using TDD.

## Requirements.
The system requires an input of a one or more digit positive integer.

## Approach
The system was initially designed to handle a single digit, this digit was represented by ```3 lines of ASCII chars```
These consist of ```underscores, hyphens and vertical slashes (pipes)```.  Using 3 lines provides and aesthetically pleasing
result where only the very tops of numbers (2,5,6,7,8,9,0) are represented in the top line using underscores.  The remaineder
of lines are used to represent the rest of the digits.  Each digit consists of 3 ascii characters their representations stored in a dictionary using tuples, 
Each line is aligned, spaces are used to pad appropriately.  The information for each digit is stored with a dictionay in the class initialiser.

TDD allowed the generation of a test to create a single digit. A fixture was used to run tests from 0-9 for each digit.
A test was then created to handle multiple digit numbers.  Each digit is addressed in turn and each line (top, middle or bottom) 
are then concatenated togeather to form a final string that is returned with appropriate newlines to format (/n)

As an extension the functionality was added to scale the width and height of digits diplayed.  This was done by first altering the width by the 'width' factor and then padded vertically using the 'height' factor.

## Dependencies
The system was created and run and tested on Python 3.7+ using Pytest which can easily be installed using ```apt install python3-pytest``` or via pip using ```pip install -U pytest```

## Getting Started
- Clone this repo
- Navigate to the directory

## Usage
- ```import seven_segment_display```
- ```from seven_segment_display import SevenSegmentDisplay```

A single digit can be tested by callig the function ```display_numbers(x)``` where ```x``` is the digit or number you want to display.

Multiple digits can be tested using the function ```display_scaled_number(x, w, h)``` where ```x``` is the integer to display, ```w and h``` are ```width``` and ```height```(optional).

## Testing
Two tests were originally created to test single digit characters.
A Fixture was then used to run the same test with different input values, one for each digit.
Finally a test was constructed to test multiple digits

The system does not currently handle negative integers, however this feature could be implemented, also the handling of decimal values.

## Reflections
This was an interesting lesson that allowed me to use a fixture to cycle through a series of similar tests (with just the input variable changed to a known value.)
The program also gave me a reminder of string handling, string manipuation and using additonal special chars such as ```/n``` newlines.
