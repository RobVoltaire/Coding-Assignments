class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def is_valid(self):
        return 0 <= self.hours < 24 and 0 <= self.minutes < 60 and 0 <= self.seconds < 60

    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)
    
    def normalize(self):
        """Ensures that minutes and seconds are within valid ranges by carrying over extra seconds/minutes."""
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60
        self.hours %= 24  # Ensures the hour wraps around within 0-23
    
    def add(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
    
    def subtract(self, other):
        total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        
        result_seconds = (total_seconds_self - total_seconds_other) % (24 * 3600)
        
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        
        return Time(hours, minutes, seconds)
