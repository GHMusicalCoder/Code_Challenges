def clock(time):
    the_hour = {0: 'twelve', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven'}
    the_minute = {0: 'oh', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                  7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                  14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                  19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 100: ''}
    hour, minute = map(int, time.split(':'))
    if minute == 0:
        your_minute = ''
    elif minute < 10:
        your_minute = the_minute[0] + ' ' + the_minute[minute]
    elif minute < 20:
        your_minute = the_minute[minute]
    else:
        your_minute = the_minute[minute // 10 * 10] + ' ' + the_minute[minute%10 if minute % 10 else 100]
    return f"It's {the_hour[hour if hour < 12 else hour - 12]} {your_minute} {'am' if hour < 13 else 'pm'}"


print(clock('00:00'))
print(clock('01:30'))
print(clock('12:05'))
print(clock('14:01'))
print(clock('20:29'))
print(clock('21:00'))