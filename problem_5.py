import re
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    
    def before(self, time):
        if self.hour <= time.hour:
            if self.hour == time.hour:
                if self.minute <= time.minute:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

class BusSchedule:
    def __init__(self, name, arrival, departure):
        self.name = name
        self.arrival = arrival
        self.departure = departure

    def IsOnePointOfTime(self, busSchedule):
        if self.arrival.before(busSchedule.arrival) and busSchedule.arrival.before(self.departure):
            return True
        elif busSchedule.arrival.before(self.arrival) and self.arrival.before(busSchedule.departure):
            return True
        else:
            return False

n = input('How many are bus schedule will be inputed ?\nanswer : ')
listSchedule = []
print('Input in format : <Bus_Name> A <arrival_time> D <departure_time>')
for i in range(int(n)):
    inp = input()
    inp = re.split(' A | D ', inp)
    name = inp[0]
    arrHour = int(inp[1].split(':')[0])
    arrMinute = int(inp[1].split(':')[1])
    depHour = int(inp[2].split(':')[0])
    depMinute = int(inp[2].split(':')[1])
    arr = Time(arrHour, arrMinute)
    dep = Time(depHour, depMinute)
    listSchedule.append(BusSchedule(name, arr, dep))

countList = []
count_max = 0
for schedule1 in listSchedule:
    listBusATime = [schedule1]
    for schedule2 in listSchedule:
        if(schedule1 != schedule2):
            atTime = True
            for bus in listBusATime:
                if(not bus.IsOnePointOfTime(schedule2)):
                    atTime = False
                    break
            if atTime:
                listBusATime.append(schedule2)
    if len(listBusATime) > count_max:
        count_max = len(listBusATime)

print('Maximum number of bus inside the station at one time is {}'.format(count_max))
print('Complexity\nWorst Case : O(N^3)\nBest Case : O(N^2)')

