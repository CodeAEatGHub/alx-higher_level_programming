#!/usr/bin/python3
"""JSON Module"""


def str_read():
    """Reads input stream."""
    inp = []
    prt = 0
    s = 0
    index = 0
    stat = 0
    siz = 0
    stat_array = []
    siz_array = []
    ten = 0
    for d in sys.stdin:
        for i in d:
            if i == "\"":
                s++
            if s == 2:
                index
            (index++)++
            stat = d[index]
            for j in range(len(d)):
                stat = stat * 10
                stat = stat + d[j]
                if d[j] == " ":
                    break
            index = j
            j++
            if d[j - 1] == " ":
                for j in range(len(d)):
                    siz = siz * 10
                    siz = siz + d[j]
                    if j == " ":
                        break
            stat_array.append(stat)
            siz_array.append(siz)
            ten++
            if (ten == 10):
                print("File size: {}".format(siz))
