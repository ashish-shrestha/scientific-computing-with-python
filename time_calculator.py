def add_time(start, duration, day =''):
    begin = start.split(":")
    increase = duration
    day = day

    hours = int(begin[0])
    minutes = begin[1].split(" ")
    ampm = minutes[1]
    minutes = int(minutes[0])

    print('initial begin hour', hours)
    print('initial begin minute', minutes)
    print('initial ampm', ampm)

    increase = increase.split(":")
    hours_to_add = int(increase[0])
    minutes_to_add = int(increase[1])
    print('initial hours to add', hours_to_add)
    print('initial minutes to add', minutes_to_add)

    final_minutes = minutes + minutes_to_add
    hours_to_add += (final_minutes // 60)
    final_minutes = (final_minutes % 60)

    print('minutes:', minutes)
    print('final minute:', final_minutes)
    print('hours to add:', hours_to_add)

    final_hours = hours + hours_to_add

    print('final hours:', final_hours)

    # determine distance to 12:00 to determine am/pm
    minutes_to_12 = (12 * 60) - ((hours * 60) + minutes)
    print('minutes to 12:', minutes_to_12)
    total_minutes_to_add = (hours_to_add * 60) + minutes_to_add
    print('total minutes to add:', total_minutes_to_add)
    if total_minutes_to_add - minutes_to_12 >= 0:
        remaining_minutes = total_minutes_to_add - minutes_to_12
        print('remaining minutes', remaining_minutes)
        if remaining_minutes >= (12 * 60):
            result = remaining_minutes // (12 * 60)
            print('result:', result)
            if result % 2 == 0:
                if ampm == 'AM':
                    ampm = 'PM'
                else:
                    ampm = 'PM'
        else:
            if ampm == 'AM':
                ampm = 'PM'
            else:
                ampm = 'PM'
    else:
        if ampm == 'AM':
            ampm = 'PM'
        else:
            ampm = 'PM'

    print('final ampm:', ampm)




add_time("11:30 AM", "12:32")







    #return new_time