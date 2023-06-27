#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for item in range(list_length):
        try:
            new_list.append(my_list_1[item] / my_list_2[item])
            err = None
        except ZeroDivisionError:
            err = "division by 0"
            new_list.append(0)
        except (TypeError, ValueError):
            new_list.append(0)
            err = "wrong type"
        except IndexError:
            err = "out of range"
            new_list.append(0)
        finally:
            if err:
                print("{}".format(err))
    return (new_list)
