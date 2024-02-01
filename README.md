# Hanoi

This Python script solves the Tower of Hanoi puzzle for a specified number of disks using a recursive algorithm. The Tower of Hanoi is a classic problem that involves moving a stack of disks from one peg to another, following specific rules.

## How It Works

The script defines a function `move()` that uses recursion to move `n` disks from a source peg to a target peg, with the help of an auxiliary peg. The disks are represented by integers in descending order, where the largest disk is represented by the largest number.

### Parameters

- `n (int)`: The number of disks to move.
- `source (list)`: The source peg as a list of disks.
- `auxiliary (list)`: The auxiliary peg as a list of disks.
- `target (list)`: The target peg as a list of disks.

### Process

1. **Initialization**: The script initializes three pegs (A, B, C) with `NUMBER_OF_DISKS` on peg A in descending order and pegs B and C empty.
2. **Recursive Movement**:
   - Moves `n-1` disks from the source peg to the auxiliary peg, using the target peg as a temporary holding area.
   - Moves the nth disk from the source peg to the target peg.
   - Moves the `n-1` disks from the auxiliary peg to the target peg, using the source peg as a temporary holding area.
3. **Progress Display**: After each move, the current state of the pegs is printed to the console.

### Usage

To use the script, simply set the `NUMBER_OF_DISKS` variable to the desired number of disks and run the script. The moves required to solve the puzzle will be printed to the console, along with the state of the pegs after each move.

## Example Output

For `NUMBER_OF_DISKS = 5`, the output will display the sequence of moves and the intermediate states of pegs A, B, and C until all disks are moved from peg A to peg C in accordance with the rules of the Tower of Hanoi puzzle.

## Rules of the Game

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3. No disk may be placed on top of a smaller disk.

## Requirements

- Python 3.x

This script is a straightforward implementation of the Tower of Hanoi puzzle solver and serves as an educational tool to demonstrate recursion in algorithms.
