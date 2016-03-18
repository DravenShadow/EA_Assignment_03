import QuickSort


def read_in_list(file):
    """
    A method to read in a file containing numbers
    :param file:
    :return:
    """
    list = []
    f = open(file, 'r')
    for line in f:
        if line[0:(len(line) - 1)] == '':
            pass
        else:
            list.append(int(line[0:(len(line) - 1)]))
    f.close()
    return list


def main():
    list = [10, 1, 2, 3, 4, 6, 9]
    list2 = [10, 1, 2, 3]
    s = QuickSort('first')
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
