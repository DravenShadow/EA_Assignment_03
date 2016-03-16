class Sort:
    def __init__(self, pivot_type):
        self.pivot_type = pivot_type
        self.count = 0

    def partition_1(self, arr, pivot_point, end_index):
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

    def partition_2(self, arr, left, pivot_index, right):
        pivot = arr[pivot_index]
        done = False

        while not done:
            while arr[left] < pivot and left <= right:
                left += 1
            while arr[right] > pivot and right >= left:
                right -= 1

            if right <= left:
                done = True
            else:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp

        if self.pivot_type == 'first':
            return pivot_index + 1
        elif self.pivot_type == 'last':
            return pivot_index - 1
        else:
            if (right - left) % 2 == 0:
                return ((right - left) // 2) + 0.5
            else:
                return (right - left) // 2

    def quicksort(self, arr, pivot_point, end_index):
        left = 0
        if self.pivot_type == 'first':
            if pivot_point < end_index:
                q = self.partition_2(arr,left, pivot_point, end_index)
                self.quicksort(arr, pivot_point, q - 1)
                self.count += abs(((q - 1) - pivot_point) - 1)
                self.quicksort(arr, q + 1, end_index)
                self.count += abs(((q - 1) - pivot_point) - 1)
        elif self.pivot_type == 'last':
            if pivot_point > 0:
                q = self.partition_2(arr, left, pivot_point, end_index)
                self.quicksort(arr, q, q - 1)
                self.count += abs(((q - 1) - pivot_point) - 1)
                self.quicksort(arr, q, end_index)
                self.count += abs(((q - 1) - pivot_point) - 1)
        else:
            if len(arr) % 2 == 0:
                q = self.partition_2(arr,left, pivot_point, end_index)
                self.quicksort(arr, pivot_point, q - 1)
                self.count += ((q - 1) - pivot_point) - 1
                self.quicksort(arr, q + 1, end_index)
            else:
                q = self.partition_2(arr,left, pivot_point, end_index)
                self.quicksort(arr, pivot_point, q - 1)
                self.count += abs(((q - 1) - pivot_point) - 1)
                self.quicksort(arr, q + 1, end_index)
                self.count += abs(((q - 1) - pivot_point) - 1)

    def quicksort_helper(self, arr):
        if self.pivot_type == 'first':
            self.quicksort(arr, 0, len(arr) - 1)
        elif self.pivot_type == 'last':
            self.quicksort(arr, len(arr) - 1, len(arr) - 1)
        else:
            if len(arr) % 2 == 0:
                self.quicksort(arr, (len(arr) // 2) + 0.5, len(arr) - 1)
            else:
                self.quicksort(arr, len(arr) // 2,  len(arr) - 1)

    def reset_count(self):
        self.count = 0

    def get_count(self):
        print(self.count)

    def reset_pivot_type(self, new_type):
        self.pivot_type = new_type


def main():
    list = [10, 1, 2, 3, 4]
    list2 = [10, 1, 2, 3]
    s = Sort('first')
    '''
    s.quicksort_helper(list)
    print(list)
    s.get_count()
    s.reset_count()
    '''
    s.reset_pivot_type('last')
    s.quicksort_helper(list)
    print(list)
    s.get_count()


if __name__ == '__main__':
    main()
