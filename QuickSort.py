"""
        Author: Rowland DePree                                      QuickSort.py

        This is a class designed to create an QuickSort object that will then allow you to sort by either the first element
        as the pivot, the last element as the pivot, or the middle elemnt as the pivot.  It also keeps track of the count
        the number of comparisons.
"""

class QuickSort:
    def __init__(self, pivot_type=None):
        self.pivot_type = pivot_type
        self.count = 0

    def first_quicksort(self, arr, begin, end):
        """
        This is a method to do quick sort using the first element as the pivot.  The original form of this code is from:
        http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
        :param arr:
        :param begin:
        :param end:
        :return:
        """
        if begin < end:
            splitpoint = self.first_partition(arr, begin, end)

            self.first_quicksort(arr, begin, splitpoint - 1)
            self.count += ((end - begin) - 1)
            self.first_quicksort(arr, splitpoint + 1, end)
            self.count += ((end - begin) - 1)

    def first_partition(self, arr, begin, end):
        """
        This is a method to partition using the first element as the pivot.  The original form of this code is from:
        http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
        :param arr:
        :param begin:
        :param end:
        :return:
        """
        pivot = arr[begin]

        left = begin + 1
        right = end

        done = False
        while not done:

            while left <= right and arr[left] <= pivot:
                left += 1

            while arr[right] >= pivot and right >= left:
                right -= 1

            if right < left:
                done = True
            else:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp

        temp = arr[begin]
        arr[begin] = arr[right]
        arr[right] = temp

        return right

    def end_partition(self, arr, begin, end):
        """
        A method designed to partition the list.  The original form of this code was from:
        http://hetland.org/coding/python/quicksort.html
        :param arr:
        :param begin:
        :param end:
        :return:
        """
        pivot = arr[end]
        bottom = begin - 1
        top = end
        done = 0
        while not done:
            while not done:
                bottom += 1
                if bottom == top:
                    done = 1
                    break
                if arr[bottom] > pivot:
                    arr[top] = arr[bottom]
                    break
            while not done:
                top -= 1
                if top == bottom:
                    done = 1
                    break
                if arr[top] < pivot:
                    arr[bottom] = arr[top]
                    break
        arr[top] = pivot
        return top

    def end_quicksort(self, arr, begin, end):
        """
        A method designed to do quicksort using the last element as the pivot.  The original form of this code is from:
        http://hetland.org/coding/python/quicksort.html
        :param arr:
        :param begin:
        :param end:
        :return:
        """
        if begin < end:
            split = self.end_partition(arr, begin, end)
            self.end_quicksort(arr, begin, split - 1)
            self.count += ((end - begin) - 1)
            self.end_quicksort(arr, split + 1, end)
            self.count += ((end - begin) - 1)
        else:
            return

    def mid_parition(self, arr, left, right):
        """
        This is a method to do quick sort using the middle element as the pivot.  The original form of this code is from:
        http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/quicksort.pdf
        :param arr:
        :param left:
        :param right:
        :return:
        """
        if (left + right) % 2 == 0:
            mid = int(((left + right) / 2) - 1)
        else:
            mid = int(((left + right) // 2))

        temp = arr[left]
        arr[left] = arr[mid]
        arr[mid] = temp

        pivot = arr[left]

        low = left + 1
        high = right
        while low < high:
            while arr[high] > pivot:
                high -= 1
            while low <= high and arr[low] <= pivot:
                low += 1
            if low <= high:
                temp = arr[low]
                arr[low] = arr[high]
                arr[high] = temp
        temp = arr[left]
        arr[left] = arr[high]
        arr[high] = temp
        return high

    def mid_quicksort(self, arr, left, right):
        """
        This is a method to parition an list using the middle element as the pivot.  The original form of this code is from:
        http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/quicksort.pdf
        :param arr:
        :param left:
        :param right:
        :return:
        """
        if left < right:
            q = self.mid_parition(arr, left, right)
            self.mid_quicksort(arr, left, q - 1)
            self.count += ((right - left) - 1)
            self.mid_quicksort(arr, q + 1, right)
            self.count += ((right - left) - 1)

    def reset_count(self):
        self.count = 0

    def get_count(self):
        print(str(self.count))
