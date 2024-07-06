from fractions import Fraction

class FractionError(Exception):
    pass

def create_fraction(numerator, denominator):
    try:
        return Fraction(numerator, denominator)
    except ZeroDivisionError:
        raise FractionError("Denominator cannot be zero")
    except ValueError:
        raise FractionError("Invalid values for numerator or denominator")

def get_numerator(fraction):
    return fraction.numerator

def get_denominator(fraction):
    return fraction.denominator

def simplify_fraction(fraction):
    return fraction

def add_fractions(fraction1, fraction2):
    return fraction1 + fraction2

def subtract_fractions(fraction1, fraction2):
    return fraction1 - fraction2

def multiply_fractions(fraction1, fraction2):
    return fraction1 * fraction2

def divide_fractions(fraction1, fraction2):
    try:
        return fraction1 / fraction2
    except ZeroDivisionError:
        raise FractionError("Cannot divide by zero")

def are_fractions_equivalent(fraction1, fraction2):
    return fraction1 == fraction2


if __name__ == "__main__":
    f1 = create_fraction(1, 2)
    f2 = create_fraction(3, 4)
    print(add_fractions(f1, f2))