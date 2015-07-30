from worker import Worker

def main():
    joe = Worker("065868774")
    meg = Worker(147546555)
    joe.setHourlyRate()
    meg.setHourlyRate(25.22)
    joe.setTitle("bitch")
    meg.setTitle("CFO")
    joe.setHours(12)
    meg.setHours(22)
    joe.setHours(5)
    print joe.calcWages()
    print meg.calcWages()
