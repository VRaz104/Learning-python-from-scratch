#You want to create a custom Temperature class that:
#stores temperature in Celsius
#lets you add two temperatures using +
#prints a friendly string (e.g., "25°C")
#shows a clear, developer-friendly representation
#allows comparing temperatures using > and <

class temperature:
    def __init__(self, celsius):
        self.celsius=celsius
    def __str__(self):
        return f"{self.celsius} degrees"
    def __add__(self, other):
        return (self.celsius + other.celsius)
    def __gt__(self, other):
        return self.celsius>other.celsius
    def __lt__(self,other):
        return self.celsius<other.celsius
    t1=float(input("First temperature:"))
    t2=float(input("Second temperature:"))
    print(t1)
    t3=t2+t1
    print(t3)
    print(t1>t2)
    print(t1<t2)