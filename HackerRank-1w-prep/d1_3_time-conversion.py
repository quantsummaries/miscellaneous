def timeConversion(s):
    am_flag = True if 'AM' in s else False
    s_clean = s.replace('AM', '').replace('PM', '')
    hms = s_clean.split(':')

    if am_flag and hms[0] == "12":
        hms[0] = "00"
    if not am_flag and hms[0] != "12":
        hms[0] = str(int(hms[0]) + 12)

    return ':'.join(hms)

for s in (['12:01:00PM', '12:01:00AM', '07:05:45PM']):
    print(timeConversion(s))
