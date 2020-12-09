def get_earliest(*dates):
    """Return earliest of given MM/DD/YYYY-formatted date strings."""
    def date_key(date):
        (m, d, y) = date.split('/')
        return y, m, d

    return min(dates, key=date_key)

# Without multiple unlimited arguments
# def get_earliest(date1, date2):
#     month_1, day_1, year_1 = date1.split('/')
#     month_2, day_2, year_2 = date2.split('/')
#     if (year_1, month_1, day_1) < (year_2, month_2, day_2):
#         return date1
#     else:
#         return date2


if __name__ == "__main__":
    d1 = "01/24/2007"
    d2 = "01/21/2008"
    d3 = "02/29/2009"
    d4 = "02/30/2006"
    d5 = "02/28/2006"
    d6 = "02/29/2006"
    print(get_earliest(d1, d2, d3))
