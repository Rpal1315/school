import unittest

# Mock the os.system function to return predefined values
def mock_os_system(command):
    if command == "cls":
        return True
    else:
        return False


class TestAltMatrixSum(unittest.TestCase):
    def test_alt_matrix_sum_2x2_positive(self):
    # Mock the input function to return predefined values
        with unittest.mock.patch(
            "builtins.input", side_effect=["2", "2", "1", "2", "3", "4"]
        ):
            # Capture the printed output
            with unittest.mock.patch("builtins.print") as mock_print:
                # Run the code
                exec(open("alt_matrix_sum.py").read())

    # Check if the correct sum was printed
    mock_print.assert_called_with("The sum of alternate elements of the matrix is:", 5)


def test_alt_matrix_sum_1x1(self):
    with unittest.mock.patch("builtins.input", side_effect=["1", "1", "5"]):
        with unittest.mock.patch("builtins.print") as mock_print:
            exec(open("alt_matrix_sum.py").read())

    mock_print.assert_called_with("The sum of alternate elements of the matrix is:", 5)


def test_alt_matrix_sum_3x3_negative(self):
    with unittest.mock.patch(
        "builtins.input",
        side_effect=["3", "3", "-1", "2", "-3", "4", "-5", "6", "-7", "8", "-9"],
    ):
        with unittest.mock.patch("builtins.print") as mock_print:
            exec(open("alt_matrix_sum.py").read())

    mock_print.assert_called_with(
        "The sum of alternate elements of the matrix is:", -22
    )


def test_alt_matrix_sum_all_zeros(self):
    with unittest.mock.patch(
        "builtins.input", side_effect=["2", "2", "0", "0", "0", "0"]
    ):
        with unittest.mock.patch("builtins.print") as mock_print:
            exec(open("alt_matrix_sum.py").read())

    mock_print.assert_called_with("The sum of alternate elements of the matrix is:", 0)


def test_alt_matrix_sum_large_matrix(self):
    # Mock the input function to return predefined values for a 10x10 matrix
    input_values = ["10", "10"] + [str(i) for i in range(100)]
    with unittest.mock.patch("builtins.input", side_effect=input_values):
        # Capture the printed output
        with unittest.mock.patch("builtins.print") as mock_print:
            # Run the code
            exec(open("alt_matrix_sum.py").read())

    # Calculate the expected sum of alternate elements
    expected_sum = sum(i for i in range(100) if ((i // 10) + (i % 10)) % 2 == 0)

    # Check if the correct sum was printed
    mock_print.assert_called_with(
        "The sum of alternate elements of the matrix is:", expected_sum
    )



if __name__ == "__main__":
    unittest.main()


