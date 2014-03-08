dict = {"fz": 26, "xx": 27}
dict["cc"] = 28
print dict["fz"]
print dict.get("aa")
print dict.get("bb", "not found")
print dict
print dict.pop("cc")
print dict