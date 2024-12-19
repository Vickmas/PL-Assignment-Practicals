#Practical Five: Expressions

# ---------------------------------
# Operator Precedence
# ---------------------------------
def demonstrate_operator_precedence():
    """Demonstrate operator precedence with examples."""
    print("\n# Operator Precedence")
    expr1 = 10 + 5 * 2  # Multiplication has higher precedence than addition
    expr2 = (10 + 5) * 2  # Parentheses override precedence
    expr3 = 10 > 5 and 3 < 7 or not 2 == 2  # Logical and comparison operators precedence

    print(f"10 + 5 * 2 = {expr1}")  # Should output 20
    print(f"(10 + 5) * 2 = {expr2}")  # Should output 30
    print(f"10 > 5 and 3 < 7 or not 2 == 2 = {expr3}")  # Should output True

# ---------------------------------
# Conditional, Relational, and Boolean Expressions
# ---------------------------------
def demonstrate_conditionals():
    """Demonstrate conditional, relational, and boolean expressions."""
    print("\n# Conditional, Relational, and Boolean Expressions")

    x, y = 10, 20

    # Relational operators
    if x < y:
        print(f"{x} is less than {y}")
    elif x == y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is greater than {y}")

    # Boolean operators
    is_x_positive = x > 0
    is_y_negative = y < 0

    if is_x_positive and not is_y_negative:
        print("x is positive and y is not negative.")

# ---------------------------------
# Operator Overloading
# ---------------------------------
class Vector:
    """A simple class to demonstrate operator overloading."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

def demonstrate_operator_overloading():
    """Demonstrate operator overloading with custom behavior."""
    print("\n# Operator Overloading")
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    print("v1 =", v1)
    print("v2 =", v2)

    print("v1 + v2 =", v1 + v2)
    print("v1 - v2 =", v1 - v2)
    print("v1 * 3 =", v1 * 3)
    print("v2 / 2 =", v2 / 2)

# ---------------------------------
# Type Coercion
# ---------------------------------
def demonstrate_type_coercion():
    """Demonstrate implicit and explicit type coercion in Python."""
    print("\n# Type Coercion")

    # Implicit type coercion
    result = 10 + 3.5  # int is coerced to float
    print(f"10 + 3.5 (Implicit Coercion) = {result} (type: {type(result)})")

    # Explicit type coercion
    num_str = "123"
    coerced_num = int(num_str)
    print(f"String '123' explicitly converted to integer: {coerced_num} (type: {type(coerced_num)})")

    # Potential pitfalls of implicit coercion
    mixed_type_result = "Number: " + str(42)
    print(f"""Mixed type concatenation (explicit conversion): {mixed_type_result}""")

# ---------------------------------
# Main Function
# ---------------------------------
def main():
    """Run all demonstrations."""
    demonstrate_operator_precedence()
    demonstrate_conditionals()
    demonstrate_operator_overloading()
    demonstrate_type_coercion()

if __name__ == "__main__":
    main()
