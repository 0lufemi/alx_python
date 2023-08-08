from sys import argv

argument_len = len(argv) - 1

if __name__ == "__main__":
    if argument_len == 0:
        print("{} arguments.".format(argument_len))
    elif argument_len == 1:
        print("{} argument:".format(argument_len))
    else:
        print("{} arguments:".format(argument_len))

    serial_num = 1
    for argument in argv:
        if argv.index(argument) == 0:
            continue
        print("{}: {}".format(serial_num, argument))
        serial_num += 1
