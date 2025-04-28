def add(a, b):
    """Add two numbers together and return the result."""
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the product."""
    return a * b

class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def __init__(self):
        self.result = 0

    def divide(self, a, b):
        """Divide a by b and return the result. Returns None if division by zero."""
        if b == 0:
            return None
        return a / b

def greet(name):
    """Return a greeting string with the provided name."""
    return f"Hello, {name}!"
