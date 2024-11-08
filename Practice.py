for item in enumerate(['a', 'b', 'c']):
    print(item)


def enumerate_items(items):
    index = 0
    for item in items:
        yield index, item
        index += 1

for index, item in enumerate_items(['a', 'b', 'c']):
    print(index, item)