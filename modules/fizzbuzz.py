import os

DEBUG =  os.environ.get("DEBUG")

def fizz_buzz(config, start, end) -> list[str]:
    result: list = []

    for i in range(start, end + 1):
        cache = ""
        for item in config:
            if i % item["value"] == 0:
                cache += item["name"]

        if cache:
            result.append(cache)
            if DEBUG:
                print(cache)

        if DEBUG:
            if not any([i % item["value"] == 0 for item in config]):
                print(i)

    return result
