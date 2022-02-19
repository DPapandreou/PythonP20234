def filehandler(file_name, delim):
    with open(file_name) as f:
        content = f.read()
        content = content.lower()
        content.rstrip("'\n'")
        content = list(content.split(delim))
    return content


def getmostfrequent(list):
    d = dict()
    for element in list:
        d[element] = 0
    for element in list:
        d[element] += 1
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


def getmostfrequentcombos(list, char_num):
    combos = dict()
    for element in list:
        if len(element) >= char_num:
            combo = ""
            for i in range(char_num):
                combo += element[i]
            combos[combo] = 0
    for element in list:
        if len(element) >= char_num:
            combo = ""
            for i in range(char_num):
                combo += element[i]
            combos[combo] += 1
    return sorted(combos.items(), key=lambda x: x[1], reverse=True)


def main():
    words = filehandler(str(input("Enter file name: ")), ' ')
    print(getmostfrequent(words))
    combos1 = list(getmostfrequentcombos(words, 2))
    print("The Most Common Combinations of the two first letters:",combos1[:3])
    combos2 = list(getmostfrequentcombos(words, 3))
    print("The Most Common Combinations of the three first letters:",combos2[:3])



main()

