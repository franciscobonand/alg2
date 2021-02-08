#!/usr/bin/env python3

import sys
import compression as lz78comp

def invalid_input(usr_input):
    valid_cmds = ["-x", "-c"]
    valid_file_types = ["txt", "lz78"]
    file_type = usr_input[2].split(".")[1]

    if len(usr_input) != 3 and len(usr_input) != 5:
        return True
    elif usr_input[1] not in valid_cmds:
        return True
    elif file_type not in valid_file_types:
        return True

    if usr_input[1] == "-c" and file_type != "txt":
        return True
    elif usr_input[1] == "-x" and file_type != "lz78":
        return True

    if len(usr_input) == 5 and usr_input[3] != "-o":
        return True

if __name__ == "__main__":
    cli_input = sys.argv

    if invalid_input(cli_input):
        print("Please insert a valid command")
        raise Exception("Commands should be like './main.py -(c/x) file.(txt/lz78) [-o result_file_name]'")

    f_name = ""

    if cli_input[1] == "-c":
        if len(cli_input) == 5 :
            f_name = cli_input[4] + ".lz78"
        else :
            f_name = cli_input[2].split(".")[0] + ".lz78"

        lz78comp.compress(cli_input[2], f_name)
        print("File ", cli_input[2], " compressed to ", f_name, " !")
    
    elif cli_input[1] == "-x":
        if len(cli_input) == 5 :
            f_name = cli_input[4] + ".txt"
        else :
            f_name = cli_input[2].split(".")[0] + ".txt"

        decoded_text = lz78comp.decompress(cli_input[2])
        lz78comp.create_txt_file(f_name, decoded_text)
        print("File ", cli_input[2], " decompressed to ", f_name, " !")