import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
#Format the result
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))


# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))


#Order the result
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))