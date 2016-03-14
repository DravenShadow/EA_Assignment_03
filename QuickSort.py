count = 0


def partition(arr, pivot_point, end_index):
    x = arr[end_index]
    i = pivot_point - 1
    for j in xrange(pivot_point, end_index):
        if arr[j] <= x:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i + 1]
    arr[i + 1] = arr[end_index]
    arr[end_index] = temp
    return i + 1


def quicksort(arr, pivot_point, end_index):
    if pivot_point < end_index:
        q = partition(arr, pivot_point, end_index)
        quicksort(arr, pivot_point, q - 1)
        count += ((q-1) - pivot_point) -1
        quicksort(arr, q + 1, end_index)


def main():
    list = [10, 4, 2, 5]
    quicksort(list, 0, (len(list) - 1))
    print list


if __name__ == '__main__':
    main()
