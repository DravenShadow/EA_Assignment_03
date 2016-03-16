class Sort:
    def __init__(self):
        self.count = 0

    def partition(self, arr, pivot_point, end_index):
        x = arr[end_index]
        i = pivot_point - 1
        for j in range(pivot_point, end_index):
            if arr[j] <= x:
                i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        temp = arr[i + 1]
        arr[i + 1] = arr[end_index]
        arr[end_index] = temp
        return i + 1

    def quicksort(self, arr, pivot_point, end_index):
        if pivot_point < end_index:
            q = self.partition(arr, pivot_point, end_index)
            self.quicksort(arr, pivot_point, q - 1)
            self.count += ((q - 1) - pivot_point) - 1
            self.quicksort(arr, q + 1, end_index)

    def reset_count(self):
        self.count = 0

    def get_count(self):
        print(self.count)


def main():
    list = [10, 4, 2, 5]
    s = Sort()
    s.quicksort(list, 0, (len(list) - 1))
    print(list)


if __name__ == '__main__':
    main()
