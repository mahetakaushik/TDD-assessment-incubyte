# String Calculator

A simple String Calculator that processes a string of numbers and returns their sum. Supports custom delimiters and handles negative numbers with exceptions.

## Features

* Add numbers from a string (comma, newline, or custom delimiters).
* Throw exceptions for negative numbers.

## Example Usage

```python
add("")           # Returns 0
add("1")          # Returns 1
add("1,2,3")      # Returns 6
add("1\n2,3")     # Returns 6
add("//;\n1;2")   # Returns 3
add("1,-1")       # Throws exception: "negative numbers not allowed -1"
```
