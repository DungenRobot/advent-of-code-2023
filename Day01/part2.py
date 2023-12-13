import re

numbers = '123456789'
words = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]
pattern = "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine"

def to_int(string):
    if string in numbers:
        return int(string)
    for i in range(len(words)):
        if string == words[i]: 
            return i + 1


with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        print(line.strip())
        first = -1
        last = 0



        matches = []

        for i in range(len(line)):
            s = re.search(pattern, line[i:])
            print(s)
            if s != None:
                print(s.group(0))
                matches.append(s.group(0))

        first = matches[0]
        last = matches[-1]

        print(first, last)

        first = to_int(first)
        last = to_int(last)

        print(first, last, "\n")

        total += (first * 10) + last
    print(total)

