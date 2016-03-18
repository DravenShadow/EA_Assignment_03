class Sort:
    def __init__(self, pivot_type):
        self.pivot_type = pivot_type
        self.count = 0

    def first_partition(self, arr, left, pivot_index, right):
        left += 1
        pivot = arr[pivot_index]
        done = False
        while not done:
            while arr[left] < pivot and left < right:
                left += 1
            while arr[right] > pivot and right > left:
                right -= 1
            if right <= left:
                done = True
            else:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp

        temp = arr[pivot_index]
        arr[pivot_index] = arr[left]
        arr[left] = temp
        return left

    def end_partition(self, arr, left, pivot_index, right):
        right -= 1
        pivot = arr[pivot_index]
        done = False
        while not done:
            while arr[left] < pivot and left < right:
                left += 1
            while arr[right] > pivot and right > left:
                right -= 1
            if right <= left:
                done = True
            else:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
        temp = arr[pivot_index]
        arr[pivot_index] = arr[left]
        arr[left] = temp
        return left - 1

    def middle_partition(self, arr, pivot_index, right, left):
        pivot = arr[pivot_index]
        done = False
        while not done:
            while arr[left] < pivot and left < right:
                left += 1
            while arr[right] > pivot and right > left:
                right -= 1
            if right <= left:
                done = True
            else:
                if left == pivot_index:
                    pivot_index = right
                elif right == pivot_index:
                    pivot_index = left

                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
        return pivot_index

    def quicksort(self, arr, pivot_point, end_index, left=0, len_of_arry=0):
        if self.pivot_type == 'first':
            if pivot_point < end_index:
                q = self.first_partition(arr, left, pivot_point, end_index)
                self.quicksort(arr, 0, q - 1)
                self.quicksort(arr, q + 1, end_index)
        elif self.pivot_type == 'last':
            if pivot_point > left:
                q = self.end_partition(arr, left, pivot_point, end_index)
                self.quicksort(arr, q, q - 1)
                self.quicksort(arr, q, end_index)
        else:
            if len_of_arry > 1:
                q = self.middle_partition(arr, pivot_point, end_index, left)
                if q % 2 == 0:
                    self.quicksort(arr, (int(q / 2) - 1), q, 0, q - left)
                else:
                    self.quicksort(arr, int((q / 2) + 0.5), q, 0, q - left)

                if (end_index - q) % 2 == 0:
                    self.quicksort(arr, end_index - int((end_index - q) / 2), end_index, q + 1, (end_index - q))
                else:
                    self.quicksort(arr, end_index - int((end_index - q) // 2), end_index, q + 1, (end_index - q))

    def quicksort_helper(self, arr):
        if self.pivot_type == 'first':
            self.quicksort(arr, 0, len(arr) - 1)
        elif self.pivot_type == 'last':
            self.quicksort(arr, len(arr) - 1, len(arr) - 1)
        else:
            if len(arr) % 2 == 0:
                self.quicksort(arr, int(len(arr) / 2) - 1, len(arr) - 1, 0, len(arr))
            else:
                self.quicksort(arr, int((len(arr) / 2) - 0.5), len(arr) - 1, 0, len(arr))

    def reset_count(self):
        self.count = 0

    def get_count(self):
        print(self.count)

    def reset_pivot_type(self, new_type):
        self.pivot_type = new_type


def main():
    list = [10, 1, 2, 3, 4, 6, 9]
    list2 = [10, 1, 2, 3]
    s = Sort('first')
    '''
    s.quicksort_helper(list)
    print(list)
    s.get_count()
    s.reset_count()
    '''
    s.reset_pivot_type('last')
    s.quicksort_helper(list2)
    print(list2)
    s.get_count()


if __name__ == '__main__':
    main()
