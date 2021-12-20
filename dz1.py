duration = 154

if duration < 60:
    print(f'{duration} секунд')
elif duration > 60 and duration < 3601:
    mm = duration // 60
    ss = duration % 60
    print(f'{mm} минут, {ss} секунд')
elif duration > 3600 and duration < 86401:
    mm = duration // 60
    hh = mm // 60
    ss = duration % 60
    if mm >= 60:
        mm = mm % 10
    print(f'{int(hh)} часов, {int(mm)} минут, {ss} секунд!')
elif duration > 86400:
    mm = duration // 60
    hh = mm // 60
    ss = duration % 60
    dd = hh // 24
    if mm >= 60 and hh >= 24:
        hh = hh - dd * 24
        mm = mm % 10
    print(f'{dd} день, {int(hh)} часов, {int(mm)} минут, {ss} секунд!')







