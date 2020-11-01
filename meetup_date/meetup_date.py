import datetime
import calendar
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    """Return date of the nth weekday of the given month."""
    c_month = calendar.monthcalendar(year, month)
    first_week = c_month[0]
    last_week = c_month[-1]

    if nth < 0:
        if last_week[weekday]:
            return datetime.date(year, month, c_month[nth][weekday])
        else:
            return datetime.date(year, month, c_month[nth-1][weekday])

    else:
        if first_week[weekday]:
            return datetime.date(year, month, c_month[nth-1][weekday])
        else:
            return datetime.date(year, month, c_month[nth][weekday])


# def meetup_date(year, month, *, nth=4, weekday=calendar.THURSDAY):
#     """Return date of the nth weekday of the given month."""
#     if nth > 0 and calendar.weekday(year, month, 1) == weekday:
#         nth -= 1
#     return calendar.Calendar(weekday).monthdatescalendar(year, month)[nth][0]