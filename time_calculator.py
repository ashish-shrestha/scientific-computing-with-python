def add_time(start, duration, day =''):
    begin = start.split(":")
    increase = duration
    day = day.lower().capitalize()

    # set up week, days, dayNumber
    week = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
    days = list(week.keys())
    day_number = list(week.values())

    hours = int(begin[0])
    minutes = begin[1].split(" ")
    initial_am_pm = minutes[1]
    final_am_pm = initial_am_pm
    minutes = int(minutes[0])

    '''print('initial begin hour', hours)
    print('initial begin minute', minutes)
    print('initial am pm', initial_am_pm) '''

    increase = increase.split(":")
    hours_to_add = int(increase[0])
    minutes_to_add = int(increase[1])
    ''' 
    print('initial hours to add', hours_to_add)
    print('initial minutes to add', minutes_to_add) 
    '''

    final_minutes = minutes + minutes_to_add
    hours_to_add += (final_minutes // 60)
    final_minutes = (final_minutes % 60)
    final_minutes_formatted = '0' + str(final_minutes)
    if len(final_minutes_formatted) > 2:
        final_minutes_formatted = final_minutes_formatted[1:]
    '''
    print('minutes:', minutes)
    print('final minute:', final_minutes)
    print('hours to add:', hours_to_add)
    '''
    final_hours = hours + hours_to_add
    if final_hours > 12:
        final_hours = final_hours % 12
        if final_hours == 0:
            final_hours = 12

    # print('final hours:', final_hours)

    # determine distance to 12:00 to determine am/pm
    minutes_to_twelve = (12 * 60) - ((hours * 60) + minutes)
    # print('minutes to 12:', minutes_to_twelve)
    total_minutes_to_add = (hours_to_add * 60) + final_minutes
    # print('total minutes to add:', total_minutes_to_add)
    if total_minutes_to_add - minutes_to_twelve >= 0:
        # print('total minutes to add is beyond 12 time')
        if initial_am_pm == 'PM':
            final_am_pm = 'AM'

            if (total_minutes_to_add - minutes_to_twelve) >= (12 * 60):
                cycles = (total_minutes_to_add - minutes_to_twelve) // (12 * 60)
                if cycles % 2 != 0:
                    if final_am_pm == 'PM':
                        final_am_pm = 'AM'
                    else:
                        final_am_pm = 'PM'
        else:
            final_am_pm = 'PM'
            if (total_minutes_to_add - minutes_to_twelve) >= (12 * 60):
                cycles = (total_minutes_to_add - minutes_to_twelve) // (12 * 60)
                if cycles % 2 != 0:
                    if final_am_pm == 'PM':
                        final_am_pm = 'AM'
                    else:
                        final_am_pm = 'PM'
        '''    
        remaining_minutes = total_minutes_to_add - minutes_to_twelve
        # print('remaining minutes', remaining_minutes)
        if remaining_minutes >= (12 * 60):
            result = remaining_minutes // (12 * 60)
            # print('result:', result)
            if result % 2 != 0:
                if final_am_pm == 'AM':
                    final_am_pm = 'PM'
                else:
                    final_am_pm = 'PM'
        '''

    # print('final ampm:', final_am_pm)
    result = str(final_hours) + ":" + final_minutes_formatted + " " + final_am_pm

    # determining days passed
    if initial_am_pm == 'AM':
        minutes_to_midnight = (12 * 60) + minutes_to_twelve
    else:
        minutes_to_midnight = minutes_to_twelve

    days_passed = 0
    if total_minutes_to_add >= minutes_to_midnight:
        # print('total minutes to add:', total_minutes_to_add)
        # print('minutes to midnight:', minutes_to_midnight)
        days_passed += 1
        remaining_minutes_to_add = total_minutes_to_add - minutes_to_midnight
        # print('remaining_minutes to add:', remaining_minutes_to_add)
        if day != '':
            final_day_num = days.index(day) + 1
        else:
            final_day_num = 1
        # print('final dayNum:', final_day_num)
        final_day_num += remaining_minutes_to_add // (24 * 60)
        days_passed += remaining_minutes_to_add // (24 * 60)
        if final_day_num > 7:
            final_day_num = (final_day_num % 7)
        # print('final day is:', days[final_day_num])
        final_day = days[final_day_num]
        if day != '':
            result = result + ', ' + final_day
        if days_passed != 0:
            if day != '':
                if days_passed == 1:
                    result = result + ' (next day)'
                else:
                    result = result + ' (' + str(days_passed) + ' days later)'
            else:
                if days_passed == 1:
                    result = result + ' (next day)'
                else:
                    result = result + ' (' + str(days_passed) + ' days later)'
    else:
        if day != '':
            final_day = day
            # print('final day is:', day)
            result = result + ', ' + final_day
    return result

add_time("2:59 PM", "24:00")

    # return new_time