# read in
# put data for 2 epics and 3 lans into lists
# remove duplicates?
# make global dict
# go through epics and add all unique names to both dicts with value 0
# go through all three lans and inc value of the name if it exists in the dict
# out to file all existing names:1
# out to file all existing names:>1

import csv
from collections import defaultdict
from math import ceil

mems = defaultdict(lambda: 0)


def parse(filename, num):
    csv_reader = csv.reader(open(filename), delimiter=',')
    namelist = []

    next(csv_reader)
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)

    for row in csv_reader:
        name = row[1] + ", " + row[0]
        if name not in namelist:
            namelist.append(name)
            mems[name] += num

def file_len(fname):
    with open(fname) as f:
        num_lines = sum(1 for line in f)
    return num_lines

parse("EPIC1.csv", 10)
parse("EPIC2.csv", 10)
parse("LAN1.csv", 1)
parse("LAN2.csv", 1)
parse("LAN3.csv", 1)
parse("LAN4.csv", 1)

rangeLst = [12,13,14]

been_to_one = [x[0] for x in list(mems.items()) if x[1] == 11 or x[1] == 21]
been_to_two_or_more = [x[0]
                       for x in list(mems.items()) if x[1] in rangeLst or x[1] >21]

open("conditional.txt", "w+")
open("voting.txt", "w+")

list.sort(been_to_one)
list.sort(been_to_two_or_more)

with open('conditional.txt', 'w') as f:
    for item in been_to_one:
        f.write("%s\n" % item)

with open('voting.txt', 'w') as f:
    for item in been_to_two_or_more:
        f.write("%s\n" % item)

print("Total voting Memebers: ", file_len("voting.txt"))
print("Total conditional members: ", file_len("conditional.txt"))
print("Needed for Quorum: ", ceil((file_len("voting.txt")/2)))
