import csv
import json
import os
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    data = []
    with open(INPUT_FILENAME, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(OUTPUT_FILENAME, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)
    print("Данные конвентировались_файл пустой")
if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        data = json.load(output_f)
        print(data)