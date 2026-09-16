# Mini Excel — Spreadsheet Function Simulator

A simple Python program that reads a text file containing a matrix of numbers
and a list of commands, then executes spreadsheet-like functions (`sum`, `min`, `max`)
on cell ranges.

## Features
- Reads a matrix of numbers from a text file
- Parses cell references such as `A1`, `B3`, and ranges like `A1:B3`
- Converts column letters to zero-based indices
- Supports `sum`, `min`, and `max` functions on any cell range
- Handles reversed ranges (e.g. `B3:A1`)

## How It Works
1. The first line of the input file specifies the number of rows and columns.
2. The next lines contain the matrix of numbers.
3. The remaining lines contain commands in the form `function(start:end)`.
4. The program prints each command followed by its result.

## Example

**Input file (`MyExcel.txt`):**
