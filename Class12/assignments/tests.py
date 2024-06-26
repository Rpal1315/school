from grading import grading
from io import StringIO
import sys

class Tests:
    # correctly calculates grades for multiple students
    def test_correctly_calculates_grades_for_multiple_students(self,monkeypatch):
        inputs = iter(["2", "Alice", "95", "90", "85", "Bob", "70", "75", "80"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        expected_output = ["Alice : A", "Bob : B"]


        captured_output = StringIO()
        sys.stdout = captured_output

        grading()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip().split('\n')
        assert output == expected_output

    # handles zero entries without errors
    def test_handles_zero_entries_without_errors(self,monkeypatch):
        inputs = iter(["0"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        from io import StringIO
        import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    grading()

    sys.stdout = sys.__stdout__

    output = captured_output.getvalue().strip()
    assert output == ""

# assigns grade A for average marks >= 90
    def test_assigns_grade_A_for_average_marks_above_90(monkeypatch):
        inputs = iter(["1", "Alice", "95", "90", "85"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        expected_output = ["Alice : A"]

        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        grading()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip().split('\n')
        assert output == expected_output

    # assigns grade B for average marks between 60 and 89
    def test_assigns_grade_b_for_average_marks_between_60_and_89(self,monkeypatch):
        inputs = iter(["2", "Alice", "70", "80", "85", "Bob", "60", "65", "70"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        expected_output = ["Alice : B", "Bob : B"]

        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        grading()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip().split('\n')
        assert output == expected_output

    # handles typical input values for marks and names
    def test_handles_typical_input_values(self, monkeypatch):
        inputs = iter(["2", "Alice", "95", "90", "85", "Bob", "70", "75", "80"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        expected_output = ["Alice : A", "Bob : B"]

        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        grading()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip().split('\n')
        assert output == expected_output