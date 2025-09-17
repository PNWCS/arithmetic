"""Arithmetic functions."""

from __future__ import annotations


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers.

    Args:
        a: first integer
        b: second integer

    Returns:
        Sum of a and b.

    Raises:
        TypeError: if a or b is not an int
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("add_numbers requires integer arguments")
    return a + b


def factorial(n: int) -> int:
    """Compute the factorial of n.

    Args:
        n: non-negative integer

    Returns:
        n! as int

    Raises:
        ValueError: if n is negative
        TypeError: if n is not an int
    """
    if not isinstance(n, int):
        raise TypeError("factorial requires an integer argument")
    if n < 0:
        raise ValueError("n must be non-negative")

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

    Raises:
        TypeError: if n is not an int
    """
    if not isinstance(n, int):
        raise TypeError("is_prime requires an integer argument")

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
