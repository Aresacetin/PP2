import re

with open("raw.txt", "r") as input_file:
    s = input_file.read()

p = re.compile(r"([0-9]+)\.\n([\[\]\w\-а-яА-Я %(),№\.]+)\n([0-9,]+) x ([0-9 ,]+)\n([0-9 ,]+)")

result = re.findall(p, s)
parsed_string = ""
for item in result:
    item = list(item)
    for i in range(len(item)):
        item[i] = item[i].replace(",", ".")

    parsed_string += ",".join(item) + "\n"

with open("parsed.csv", "w") as output_file:
    output_file.writelines(parsed_string)

