#!/usr/bin/env python3

import sys
import compression as z78comp

def invalid_input(usr_input):
    valid_cmds = ["-x", "-c"]
    valid_file_types = ["txt", "z78"]
    file_type = usr_input[2].split(".")[1]

    if len(usr_input) != 3 and len(usr_input) != 5:
        return True
    elif usr_input[1] not in valid_cmds:
        return True
    elif file_type not in valid_file_types:
        return True

    if usr_input[1] == "-c" and file_type != "txt":
        return True
    elif usr_input[1] == "-x" and file_type != "z78":
        return True

    if len(usr_input) == 5 and usr_input[3] != "-o":
        return True

if __name__ == "__main__":
    cli_input = sys.argv

    if invalid_input(cli_input):
        print("Please insert a valid command")
        raise Exception("Commands should be like './main.py -(c/x) file.(txt/z78) [-o result_file_name]'")

    if cli_input[1] == "-c":
        txt_file = open(cli_input[2], "rb")
        btext = txt_file.read()
        txt_file.close()
        bcompressed = z78comp.compress(btext)
        z78comp.create_compressed_file(cli_input, bcompressed)
    elif cli_input[1] == "-x":
        z78_file = open(cli_input[2], "rb")
        compressed_file = z78_file.read()
        z78_file.close()
        btext = z78comp.uncompress(compressed_file)
        z78comp.create_txt_file(cli_input, btext)