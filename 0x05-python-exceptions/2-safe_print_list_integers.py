#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list[:x]:
            if type(i) == int:
                print("{:d}".format(i), end="")
                count += 1
        print()
    except (ValueError, TypeError):
        pass
    finally:
        return count
