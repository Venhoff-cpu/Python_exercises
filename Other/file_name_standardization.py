from datetime import datetime
import numpy as np


def solution(s):
    result = ""
    list_to_modify = list(filter(None, s.splitlines()))
    list_before_sorting = [[ele.strip() for ele in x.split(",")] for x in list_to_modify]
    list_sorted = sorted(list_before_sorting, key=lambda y: datetime.strptime(y[2], "%Y-%m-%d %H:%M:%S"))
    cities = [ele[1] for ele in list_sorted]
    key, value = np.unique(cities, return_counts=True)
    dictionary = dict(zip(key, value))
    print(dictionary)
    for i in list_sorted[::-1]:
        city_name = i[1]
        city_count = dictionary.get(city_name)
        extension = i[0].split(".")[1]
        result = f"{city_name}{city_count}.{extension}\n" + result
        dictionary[city_name] -= 1
    return result


text = """
photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11
"""

print(solution(text))

#def sol():
#    data = csv.reader(open('costam.csv'))
#    sortedlist = sorted(data, key=operator.itemgetter(2))
#    i = 1
#    for line in sortedlist:
#        city = line[1]
#        print (f'{city}  {str(i).zfill(2)}')
#        i+=1
#sol()
