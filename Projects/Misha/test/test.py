li = ["abc", "dca", "coa"]

li_mapped = map(lambda a: a.replace("c", "g"), li)

li_filtered = filter(lambda a: a.count("d"), li)


print([a for a in li_filtered])
print([a for a in li_mapped])