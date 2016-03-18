from Tools.scripts.treesync import raw_input

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


def validate_pivot_type(p_type):
    correct = False
    while not correct:
        if str.lower(p_type) == 'first':
            correct = True
        elif str.lower(p_type) == 'last':
            correct = True
        elif str.lower(p_type) == 'middle':
            correct = True
        else:
            p_type = input("INCORRECT ENTRY!\nPlease re-enter a valid pivot type: ")
    return p_type


def main():
    s = QuickSort()
    s.reset_pivot_type('last')
    num_list = read_in_list(raw_input('Enter in location of file: '))
    p_type = validate_pivot_type(input('Enter in which type of pivot you want to use: '))
    s.reset_pivot_type(p_type)
    s.quick_sort_helper(num_list)
    print(num_list)
    print("Count: " + str(s.count()))


if __name__ == '__main__':
    main()
