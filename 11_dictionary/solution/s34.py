my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
seen = set()
result = {}
for key, value in my_dict.items():
    if value not in seen:
        result[key] = value
        seen.add(value)
print(result)
