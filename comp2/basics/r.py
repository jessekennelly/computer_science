# Create a Date class here. It should have an __init__ function that allows the user 
# to set initial values of month, day and year. Pass the values as parameters in that
# order (month then day then year). The default values should be January 1, 1970:
class Date:
    def __init__(self, month=1, day=1, year=1970):
        self.month = month
        self.day = day
        self.year = year
    
    def format_in_words(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
        "October", "November", "December"]
        index = self.month - 1
        if self.month < 1 or self.month > 12:
            return "Invalid date"
        else:
            return f"{months[index]} {self.day}, {self.year}"
    
    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"
    
    def is_valid(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        index = self.month -1 
        if (self.month < 13 and self.month > 0):
            if self.year > 1582:
                if((self.year % 400 == 0) or  (self.year % 100 != 0) and (self.year % 4 == 0)):
                    if self.month == 2 and (self.day == 28 or self.day == 29):
                        return True
            if self.day <= days[index]:
                return True
        else: 
            return False
                        
        
    def is_leap_year(self):
        if self.year > 1582:
            if((self.year % 400 == 0) or  (self.year % 100 != 0) and (self.year % 4 == 0)):
                return True
        else:
            return False
        
    
    def advance(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mon = self.month - 1
        if self.year > 1582:
            if((self.year % 400 == 0) or  (self.year % 100 != 0) and (self.year % 4 == 0)):
                self.day = 29
        elif self.day == days[mon]:
            self.month += 1
            self.day = 1
        
        else:
            self.day += 1
            
    def day_of_year(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        index = self.month -1
        if index < 0:
            index = 0
        if self.month == 1:
            return self.day
        else:
            return self.day + days[index]
    
    
if __name__ == "__main__":
    # To properly test your class, do not change the code below
    # three date objects get created by the code below:
    today = Date(1, 20, 2022)
    default_day = Date()
    georgia_birthday = Date(11, 15, 1887)
    # output the three dates in m/d/y format:
    print(today)
    print(default_day)
    print(georgia_birthday)
    # output the three dates using the name of the month:
    print(today.format_in_words())
    print(default_day.format_in_words())
    print(georgia_birthday.format_in_words())
    today = Date(2, 26, 2023)
    # add your own test code below
