def kthsmallest(k, items):
    if k >= len(items) or k < 0:
        return -1
    pos = partition(items)
    if pos == k:
        return items[pos]
    elif pos < k:
        return kthsmallest(k - pos - 1, items[pos + 1:])
    else:
        return kthsmallest(k, items[:pos + 1])


def partition(items):
    v = items[0]
    i, j = 1, len(items) - 1
    while(i <= j):
        while i <= j and v > items[i]:
            i += 1
        while i <= j and v < items[j]:
            j -= 1
        if i < len(items) and j >= 0 and i < j:
            items[i], items[j] = items[j], items[i]
            i += 1
            j -= 1
        else:
            break
    items[i - 1], items[0] = items[0], items[i - 1]
    return i - 1

if __name__ == "__main__":
    a = [1, 2, 4, 5, 2, 6, 7, 9, 0]
    print a
    print sorted(a)
    assert 0 == kthsmallest(0, a)
    assert 1 == kthsmallest(1, a)
    assert 2 == kthsmallest(2, a)
    assert 2 == kthsmallest(3, a)
    assert 4 == kthsmallest(4, a)
    assert 5 == kthsmallest(5, a)
    assert 6 == kthsmallest(6, a)
    assert 7 == kthsmallest(7, a)
    assert 8 == kthsmallest(8, a)
    assert 9 == kthsmallest(9, a)
