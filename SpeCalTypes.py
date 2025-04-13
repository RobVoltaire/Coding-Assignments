from datetime import datetime, time

class Calendar:
    def __init__(self):
        self.appointments = []
    
    def add_appointment(self, title, date, start_time, end_time):
        new_appointment = {
            'title': title,
            'date': date,
            'start_time': start_time,
            'end_time': end_time
        }
        if self._check_conflict(new_appointment):
            print("Conflict detected! Appointment not added.")
            return False
        self.appointments.append(new_appointment)
        return True
    
    def _check_conflict(self, new_appointment):
        for appointment in self.appointments:
            if appointment['date'] == new_appointment['date'] and (
                appointment['start_time'] < new_appointment['end_time'] and 
                appointment['end_time'] > new_appointment['start_time']
            ):
                return True
        return False
    
    def display_appointments(self):
        for app in self.appointments:
            print(f"{app['title']} - {app['date']} {app['start_time']} to {app['end_time']}")

class WorkCalendar(Calendar):
    def __init__(self):
        super().__init__()
        self.work_hours = (time(9, 0), time(17, 0))  # 9 AM to 5 PM

    def add_appointment(self, title, date, start_time, end_time):
        if not (self.work_hours[0] <= start_time <= self.work_hours[1]) or not (self.work_hours[0] <= end_time <= self.work_hours[1]):
            print("Error: Work appointments must be within work hours (9 AM - 5 PM).")
            return False
        return super().add_appointment(title, date, start_time, end_time)

    def display_appointments(self):
        print("Work Calendar:")
        super().display_appointments()

class SchoolCalendar(Calendar):
    def __init__(self):
        super().__init__()
        self.school_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}

    def add_appointment(self, title, date, start_time, end_time):
        if date.strftime('%A') not in self.school_days:
            print("Error: School appointments must be on a weekday.")
            return False
        return super().add_appointment(title, date, start_time, end_time)
    
    def display_appointments(self):
        print("School Calendar:")
        super().display_appointments()

# Example Usage
if __name__ == "__main__":
    work_cal = WorkCalendar()
    school_cal = SchoolCalendar()
    
    work_cal.add_appointment("Team Meeting", datetime(2025, 4, 1), time(10, 0), time(11, 0))
    work_cal.add_appointment("Client Call", datetime(2025, 4, 1), time(16, 0), time(17, 30))
    
    school_cal.add_appointment("Math Class", datetime(2025, 4, 1), time(8, 0), time(9, 30))
    school_cal.add_appointment("Project Discussion", datetime(2025, 4, 6), time(10, 0), time(11, 0))
    
    work_cal.display_appointments()
    school_cal.display_appointments()
