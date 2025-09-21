"""arithmetic functions."""

from __future__ import annotations


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers.

    Args:
        a: first integer
        b: second integer

    Returns:
        Sum of a and b.
    """
    total = a + b
    return total


def factorial(n: int) -> int:
    """Compute the factorial of n.

    Args:
        n: non-negative integer

    Returns:
        n! as int

    Raises:
        ValueError: if n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


def is_prime(n: int) -> bool:
    """Check whether n is a prime number.

    A prime number is an integer greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        n: integer to test

    Returns:
        True if n is prime; otherwise False.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
