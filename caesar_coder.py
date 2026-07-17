def caesar_coder(file, create_file=False):
    f = open(file)

    ascii_list = [ord(char) for char in f.read()]
    ascii_c_list = []
    for a in ascii_list:
        if chr(a).isalpha():
            c = a+3
            if not chr(c).isalpha():
                ascii_c_list.append(chr(c-26))
            else:
                ascii_c_list.append(chr(c))
        else: 
            ascii_c_list.append(chr(a))

    if create_file:
        with open("caesar_coded.txt", "w", encoding="ascii") as f:
            f.write("".join(ascii_c_list))

    print("".join(ascii_c_list))

caesar_coder("demofile.txt", create_file=True)