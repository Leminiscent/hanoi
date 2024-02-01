# Define the number of disks in the Tower of Hanoi problem
NUMBER_OF_DISKS = 5
# Initialize the source peg A with disks in descending order
A = list(range(NUMBER_OF_DISKS, 0, -1))
# Initialize empty lists for auxiliary peg B and target peg C
B = []
C = []


def move(n, source, auxiliary, target):
    """
    Recursively move n disks from the source peg to the target peg using an auxiliary peg.

    Parameters:
    n (int): The number of disks to move.
    source (list): The source peg as a list of disks.
    auxiliary (list): The auxiliary peg as a list of disks.
    target (list): The target peg as a list of disks.
    """
    if n <= 0:
        # Base case: no disks to move
        return
    # Recursive case: move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)

    # Move the nth disk from source to target
    target.append(source.pop())

    # Display our progress
    print(A, B, C, "\n")

    # Move the n - 1 disks from auxiliary to target
    move(n - 1, auxiliary, source, target)


# Initiate the call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)