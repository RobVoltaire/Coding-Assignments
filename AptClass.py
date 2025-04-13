from datetime import datetime, timedelta

class DateTime:
    def __init__(self, year, month, day, hour, minute):
        self.datetime = datetime(year, month, day, hour, minute)
    
    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M')

class Appointment(DateTime):
    def __init__(self, year, month, day, hour, minute, title, duration, location, description):
        super().__init__(year, month, day, hour, minute)
        self.title = title
        self.duration = duration  # in minutes
        self.location = location
        self.description = description
    
    def end_time(self):
        return self.datetime + timedelta(minutes=self.duration)
    
    def conflicts_with(self, other):
        return not (self.end_time() <= other.datetime or self.datetime >= other.end_time())
    
    def __str__(self):
        return (f"Appointment: {self.title}\nDate & Time: {super().__str__()}\nDuration: {self.duration} minutes\n"
                f"Location: {self.location}\nDescription: {self.description}")

# Example usage
appt1 = Appointment(2025, 4, 10, 14, 30, "Doctor's Visit", 60, "Clinic", "Routine check-up")
appt2 = Appointment(2025, 4, 10, 15, 0, "Meeting", 30, "Office", "Project discussion")

print(appt1)
print(appt2)
print("Conflicts:", appt1.conflicts_with(appt2))
