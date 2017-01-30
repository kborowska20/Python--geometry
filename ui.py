import os

#len_counting and print_table are taken from ccms


def len_counting(list_to_count, dict_of_lens):
    """
    Counts counts and sets max width of column
    Args:
        list_to_count: list of items
        dict_of_lens: dictionary of item lengths
    Returns:
         dict_of_lens: dictionary with updated values
    """
    for i in range(len(list_to_count)):
        if len(list_to_count[i]) > dict_of_lens[i]:
            dict_of_lens[i] = len(list_to_count[i])

    return dict_of_lens

def menu(title,options):
    print("\n{}".format(title))
    for i in range(0, len(options)):
        print("{}.     {}".format(i + 1, options[i]))

    print("\nSelect 0 to leave")



def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def multi_input(text):
    print(text)
    a = [float(x) for x in input().split()]
    return a

def print_table(table, title_list):
    len_of_items = {x: 0 for x in range(len(title_list))}

    title_lengths = len_counting(title_list, len_of_items)

    for line in table:
        max_lengths = len_counting(line, title_lengths)

    # top bar
    table_body = "-" * (sum(max_lengths.values()) + len(max_lengths)*3 - 1)
    string_in_between = ""
    string_to_print = ""

    # titles
    for i in range(len(title_list)):
        string_to_print += "|{:^{line_len}}".format(title_list[i], line_len=max_lengths[i]+2)
        string_in_between += "|" + "-" * (max_lengths[i]+2)

    strings_to_print = [string_to_print + "|"]

    # values
    for i in range(len(table)):
        string_to_print = ""

        for j in range(len(title_list)):
            string_to_print += "|{:^{line_len}}".format(table[i][j], line_len=max_lengths[j]+2)
        strings_to_print.append(string_in_between + "|")
        strings_to_print.append(string_to_print + "|")

    # wrap_up
    strings_to_print.insert(0, ("/" + table_body + "\\"))
    strings_to_print.append("\\" + table_body + "/")
    return "\n" + "\n".join(strings_to_print) + "\n"