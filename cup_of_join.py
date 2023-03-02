def join(*lists, sep="-"):
    if not lists and not sep:
        return None
    re = []
    i = 0
    for list1 in lists:
        for j in range(0, len(list1)):
            re.append(list1[j])
        i = i+1
        if i != len(lists):
            re.append(sep)
    return re


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())
