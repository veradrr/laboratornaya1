# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        list1 = []
        for i in reader:
            list1.append(i)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(list1, f, indent=4)




if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
