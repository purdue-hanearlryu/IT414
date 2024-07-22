# Step 1: Defining function for addition
def add_numbers(a, b):
    return a + b


# Step 2: Defining function to call the addition function
def main():
    num1 = 10  # Example number 1
    num2 = 20  # Example number 2
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")


# Step 3: Unit testing to test the addition function w/ examples
import unittest


class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-1, -1), -2)
        self.assertEqual(add_numbers(0, 0), 0)


# Main execution
if __name__ == "__main__":
    # Running main function
    main()

    # Running unit test
    unittest.main(argv=[''], exit=False, verbosity=2)
