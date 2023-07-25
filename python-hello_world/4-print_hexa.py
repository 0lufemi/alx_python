for i in range(99):
    if i < 16:
        print("{:d} = 0x{:01X}".format(i, i).lower())
    else:
        print("{:d} = 0x{:02x}".format(i, i).lower())
