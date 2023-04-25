
def insert(list, value):
    i = 0
    while i < len(list) and value > list[i]:
        i += 1
    while i < len(list):
        temp = list[i]
        list[i] = value
        value = temp
        i += 1
    list.append(value)


def insertion_sort(input):
    if not input:
        return []
    sorted = [input[0]]
    for i in range(1, len(input)):
        insert(sorted, input[i])
    return sorted


input_list = [8, 4, 23, 42, 16, 15]
sorted_list = insertion_sort(input_list)
print(sorted_list)




