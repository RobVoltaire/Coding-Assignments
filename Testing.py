from datetime import datetime, time

class TimeSlot:
    def __init__(self, start: time, end: time):
        if start >= end:
            raise ValueError("Start time must be before end time")
        self.start = start
        self.end = end

    def conflicts_with(self, other):
        return max(self.start, other.start) < min(self.end, other.end)

    def __str__(self):
        return f"{self.start.strftime('%H:%M')} - {self.end.strftime('%H:%M')}"


class Appointment:
    def __init__(self, date: datetime.date, timeslot: TimeSlot, description: str):
        self.date = date
        self.timeslot = timeslot
        self.description = description

    def conflicts_with(self, other):
        return self.date == other.date and self.timeslot.conflicts_with(other.timeslot)

    def __str__(self):
        return f"{self.date}: {self.timeslot} - {self.description}"


class Calendar:
    def __init__(self, name: str):
        self.name = name
        self.appointments = []

    def add_appointment(self, appointment: Appointment):
        for existing in self.appointments:
            if appointment.conflicts_with(existing):
                raise ValueError(f"Conflict detected with {existing}")
        self.appointments.append(appointment)

    def show_schedule(self):
        print(f"\n{self.name} Schedule:")
        for appointment in sorted(self.appointments, key=lambda x: (x.date, x.timeslot.start)):
            print(appointment)


class WorkCalendar(Calendar):
    def __init__(self):
        super().__init__("Work Calendar")


class PersonalCalendar(Calendar):
    def __init__(self):
        super().__init__("Personal Calendar")


# Demonstration
def main():
    work_calendar = WorkCalendar()
    personal_calendar = PersonalCalendar()
    
    # Creating time slots
    morning_meeting = TimeSlot(time(9, 0), time(10, 0))
    lunch_break = TimeSlot(time(12, 0), time(13, 0))
    evening_dinner = TimeSlot(time(18, 0), time(19, 0))
    
    today = datetime.today().date()
    
    # Creating appointments
    meeting = Appointment(today, morning_meeting, "Team Meeting")
    lunch = Appointment(today, lunch_break, "Lunch with Client")
    dinner = Appointment(today, evening_dinner, "Dinner with Family")
    
    # Adding appointments
    work_calendar.add_appointment(meeting)
    work_calendar.add_appointment(lunch)
    personal_calendar.add_appointment(dinner)
    
    # Attempt to create a conflicting appointment
    try:
        conflict_meeting = Appointment(today, TimeSlot(time(9, 30), time(10, 30)), "Overlapping Meeting")
        work_calendar.add_appointment(conflict_meeting)
    except ValueError as e:
        print("Error:", e)
    
    # Display schedules
    work_calendar.show_schedule()
    personal_calendar.show_schedule()


if __name__ == "__main__":
    main()
