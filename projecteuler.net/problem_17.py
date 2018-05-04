def write_out_hundred(num, written):
    """
    this will be a group of hundreds
    :param num: a string version of a number from 1 to 999 (inclusive)
    :param written: a list of words that we'll add to
    :return: true/false if successful
    """
    value = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
             10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
             17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
             60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: 'Zero'}
    if num > 99:
        written.append(value[num // 100])
        written.append('Hundred')
        num %= 100
    if num > 19:
        written.append(value[(num // 10) * 10])
        num %= 10
    if num:
        written.append(value[num])
    return True


def number_break(num):
    written = []
    hundreds, thousands, millions, billions, trillions = '', '', '', '', ''
    if num[0] == '-':
        written.append('Negative')
        num = num[1:]
    if len(num) > 15:
        return 'Error: Number greater than trillions'
    hundreds = int(num[-3:])
    num = num[:-3]
    if num:
        thousands = int(num[-3:])
        num = num[:-3]
    if num:
        millions = int(num[-3:])
        num = num[:-3]
    if num:
        billions = int(num[-3:])
        num = num[:-3]
    if num:
        trillions = int(num)
    if trillions:
        write_out_hundred(trillions, written)
        written.append('Trillion')
    if billions:
        write_out_hundred(billions, written)
        written.append('Billion')
    if millions:
        write_out_hundred(millions, written)
        written.append('Million')
    if thousands:
        write_out_hundred(thousands, written)
        written.append('Thousand')
    write_out_hundred(hundreds, written)
    print(' '.join(written))


for _ in range(int(input().strip())):
    number_break(input().strip())
