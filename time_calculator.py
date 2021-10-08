def main():
    #print("Start time: ")
    #start = input()
    #print("Duration: ")
    #duration = input()
    #print("Day?: ")
    #day = input()

    # Temp params
    start = "5:01 AM"
    duration = "0:00"
    day = "none"

    print(add_time(start, duration, day))


def add_time(start, duration, day="null"):
    tempHour = ""
    tempMins = ""
    new_time = ""
    addHour = ""
    days = 0
    dayChange = False

    currentTimeType = ""
    if "AM" in start:
        currentTimeType = "AM"
    else:
        currentTimeType = "PM"

    colonLoc = start.find(':')
    currentHour = start[0:colonLoc]
    currentMinutes = start[colonLoc+1:colonLoc+3]

    addColonLoc = duration.find(':')
    addHourTemp = int(duration[0:addColonLoc])
    addMinutes = duration[addColonLoc+1:addColonLoc+3]
    if(int(addHourTemp) == 0 and int(addMinutes) == 0):
        return start
    if(addHourTemp >= 24):
        days = (addHourTemp // 24) + 1
        addHour = addHourTemp - ((days-1) * 24)
        dayChange = True
    else:
        addHour = addHourTemp
    

    if((int(currentHour) + int(addHour) > 12) or (int(currentMinutes) + int(addMinutes) >= 60)):
        if(currentTimeType == "PM"):
            dayChange = True
            currentTimeType = "AM"
        else:
            currentTimeType = "PM"
        if((int(currentHour) + int(addHour) > 12)):
            tempHour = (int(currentHour) + int(addHour)) - 12
        else:
            tempHour = int(currentHour)
        if(int(currentMinutes) + int(addMinutes) > 59):
            tempHour += 1
            tempMins = int(currentMinutes) + int(addMinutes) - 60
        else:
            tempMins = int(currentMinutes) + int(addMinutes)

        new_time += str(tempHour)
        new_time += ':'
        if(int(tempMins) <= 9):
            new_time += '0'
            new_time += str(tempMins)
        else:
            new_time += str(tempMins)

        new_time += " "
        new_time += currentTimeType
        if(days > 1):
            new_time += " ("
            new_time += str(days)
            new_time += " days later)"
        elif((days <= 1) and (dayChange == True)):
            new_time += " (next day)"
    else:
        new_time += str(int(currentHour) + int(addHour))
        new_time += ':'
        new_time += str(int(currentMinutes) + int(addMinutes))
        new_time += " "
        new_time += currentTimeType
        if(dayChange == True):
            new_time += " (next day)"
        return new_time

    return new_time


main()
