"""
            Author:  Rowland DePree                         Main.py

            This is a program designed to validate the user input, read in a file, and do quick sort.
"""
from QuickSort import QuickSort


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
    """
    Validates the user input of the pivot type
    :param p_type:
    :return:
    """
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
    """
    Main method
    :return:
    """
    s = QuickSort()
    num_list = read_in_list(input('Enter in location of file: '))
    p_type = validate_pivot_type(input('Enter in which type of pivot you want to use: '))
    if p_type == 'first':
        s.first_quicksort(num_list, 0, len(num_list) - 1)
    elif p_type == 'last':
        s.end_quicksort(num_list, 0, len(num_list) - 1)
    else:
        s.mid_quicksort(num_list, 0, len(num_list) - 1)
    print(num_list)
    print("Count: ")
    s.get_count()
    s.reset_count()


if __name__ == '__main__':
    """
        Starts the main method
    """
    main()
