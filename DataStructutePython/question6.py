from prettytable import PrettyTable
word = []
fileName = input('Please input file name: ')
f = open(fileName, 'r')
content = f.readlines()
for line in content:
    line = line.split()
    word.append(line)
f.close()
print(word)


for i in range(len(content)):
    if i == 0:
        table = PrettyTable(word[0])
    else:
        table.add_row(word[i])

table.reversesort = True
print(table)