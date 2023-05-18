def zip_lists(a, b):
    result = ""
    current1 = a.head
    current2 = b.head

    while current1 or current2:
        if current1 is not None:
            result += "{ " + str(current1.value) + " } " + "-> "
            current1 = current1.next
        if current2 is not None:
            result += "{ " + str(current2.value) + " } " + "-> "
            current2 = current2.next

    if current1 is None and current2 is not None:
        while current2:
            result += "{ " + str(current2.value) + " } " + "-> "
            current2 = current2.next

    if current2 is None and current1 is not None:
        while current1:
            result += "{ " + str(current1.value) + " } " + "-> "
            current1 = current1.next

    result += "None"
    return result

