import re
from datetime import datetime


def solution(s):
    result = ""
    new_list = list(filter(None, s.splitlines()))
    for i in new_list:
        if re.search(r"^admin\s*[-|r][-|w][x]", i):
            size = re.search(r"\s{2}[\d]{1,8}\s", i)
            if size:
                if int(size.group()) <= 14680064:
                    my_date = (re.search(r"[\d][\d]\s*[\w]{3}\s*[\d]{4}", i)).group()
                    if not result:
                        result = my_date

                    if datetime.strptime(result, '%d %b %Y') > datetime.strptime(my_date, '%d %b %Y'):
                        result = my_date
    return result


text = """
admin  -wx 29 Sep 1983        833 source.h
admin  r-x 23 Jun 2003     854016 blockbuster.mpeg
admin  --x 02 Jul 1997        821 delete-this.py
admin  -w- 15 Feb 1971      23552 library.dll
admin  --x 15 May 1979  645922816 logs.zip
jane   --x 04 Dec 2010      93184 old-photos.rar
jane   -w- 08 Feb 1982  681574400 important.java
admin  rwx 26 Dec 1952   14680064 to-do-list.txt
"""

print(solution(text))
