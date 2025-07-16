import os

DEBUG =  os.environ.get("DEBUG")

def fizz_buzz(fizzbuzzes, sample_range_start, sample_range_end) -> list[str]:
    result: list = []

    for i in range(
        sample_range_start,
        sample_range_end + 1
    ):
        cache = ""
        for item in fizzbuzzes:
            if i % item["value"] == 0:
                cache += item["name"]

        if cache:
            result.append(cache)
            if DEBUG:
                print(cache)

        if DEBUG:
            if not any([
                i % item["value"] == 0
                for item in fizzbuzzes
            ]):
                print(i)

    return result
