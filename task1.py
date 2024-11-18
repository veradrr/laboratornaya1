import json


FILENAME = "input.json"
def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    summa = 0
    for i in json_data:
        a = i["score"] * i["weight"]
        summa += a
    return round(summa, 3)


print(task())
