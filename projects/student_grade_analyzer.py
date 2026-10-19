"""Analyze student marks and assign grades from the command line.

Run: python projects/student_grade_analyzer.py
"""

from statistics import mean


def get_marks() -> list[float]:
    """Read comma-separated marks and validate that each value is between 0 and 100."""
    while True:
        raw_marks = input("Enter marks separated by commas (0-100): ")
        try:
            marks = [float(value.strip()) for value in raw_marks.split(",")]
        except ValueError:
            print("Please enter numbers only, separated by commas.")
            continue

        if not marks or any(not 0 <= mark <= 100 for mark in marks):
            print("Enter at least one mark, and keep every mark between 0 and 100.")
            continue

        return marks


def get_grade(mark: float) -> str:
    """Convert a numeric mark to a letter grade."""
    if mark >= 90:
        return "A+"
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 50:
        return "D"
    return "F"


def display_report(marks: list[float]) -> None:
    """Print individual grades and a concise class summary."""
    print("\n--- Student Marks Report ---")
    for index, mark in enumerate(marks, start=1):
        print(f"Student {index}: {mark:.1f}/100 | Grade: {get_grade(mark)}")

    print("\n--- Class Summary ---")
    print(f"Students: {len(marks)}")
    print(f"Average:  {mean(marks):.2f}")
    print(f"Highest:  {max(marks):.1f}")
    print(f"Lowest:   {min(marks):.1f}")
    print(f"Passed:   {sum(mark >= 50 for mark in marks)}")
    print(f"Failed:   {sum(mark < 50 for mark in marks)}")


def main() -> None:
    """Run the grade analyzer."""
    display_report(get_marks())


if __name__ == "__main__":
    main()
