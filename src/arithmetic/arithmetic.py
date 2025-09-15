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
    return a + b
    # raise NotImplementedError


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
        raise ValueError
    else:
        if n == 0:
            return 1
        else:
            fact = 1
            for i in range(1, n + 1):
                fact = fact * i
            return fact


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
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
