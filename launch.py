import json

from modules.fizzbuzz import fizz_buzz

CONFIG_LOCATION = "./config/config.json"

if __name__ == '__main__':
    with open(CONFIG_LOCATION, "r") as f:
        config = json.load(f)
        fizzbuzzes = config["fizzbuzzes"]
        test_range = config["test_range"]
        reverse = config["reverse"]

    # Sort the fizzbuzzes by their rank
    fizzbuzzes = sorted(fizzbuzzes, key=lambda x: x["rank"])

    if reverse:
        fizzbuzzes.reverse()

    print(fizzbuzzes)

    result = fizz_buzz(fizzbuzzes, test_range["start"], test_range["end"])
    print(result)
