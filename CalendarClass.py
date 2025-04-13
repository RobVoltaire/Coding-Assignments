from datetime import datetime, timedelta

class Appointment:
    def __init__(self, title, start_time, end_time):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def conflicts_with(self, other):
        return not (self.end_time <= other.start_time or self.start_time >= other.end_time)

    def __repr__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%H:%M')})"

class Calendar:
    def __init__(self, name):
        self.name = name
        self.appointments = []
    
    def add_appointment(self, appointment):
        self.appointments.append(appointment)
    
    def remove_appointment(self, appointment):
        self.appointments.remove(appointment)
    
    def find_appointments(self, date):
        return [appt for appt in self.appointments if appt.start_time.date() == date]
    
    def find_conflicts(self):
        conflicts = []
        for i in range(len(self.appointments)):
            for j in range(i + 1, len(self.appointments)):
                if self.appointments[i].conflicts_with(self.appointments[j]):
                    conflicts.append((self.appointments[i], self.appointments[j]))
        return conflicts
    
    def print_schedule(self, start_date, end_date=None):
        if end_date is None:
            end_date = start_date
        
        current_date = start_date
        while current_date <= end_date:
            print(f"Appointments for {current_date.strftime('%Y-%m-%d')}:\n")
            day_appointments = self.find_appointments(current_date.date())
            if day_appointments:
                for appt in sorted(day_appointments, key=lambda x: x.start_time):
                    print(f"  {appt}")
            else:
                print("  No appointments.")
            print("\n")
            current_date += timedelta(days=1)
