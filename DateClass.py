from datetime import datetime

class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    def is_valid(self):
        """Checks if the date is valid considering month lengths and leap years."""
        try:
            datetime(self.year, self.month, self.day)
            return True
        except ValueError:
            return False

    def __lt__(self, other):
        """Compares two dates chronologically."""
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def day_of_week(self):
        """Returns the day of the week for the given date."""
        if self.is_valid():
            return datetime(self.year, self.month, self.day).strftime('%A')
        return "Invalid date"

# Example usage:
d1 = Date(2023, 3, 30)
d2 = Date(2024, 2, 29)
print(d1)  # Output: 2023-03-30
print(d2.is_valid())  # Output: True
print(d1 < d2)  # Output: True
print(d1.day_of_week())  # Output: Thursday
