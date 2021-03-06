# Written by Eden Avikzer - home assignment

from pathlib import Path
# Import the argparse library
import argparse
# Import library that Support regular expressions (RE)
import re


# Receive arguments through the command line using argparse library
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('sedFormat', help='provide the strings you want to swap in sed format, eg, s/on/ON/',
                        default='')
    parser.add_argument('file', help="The file that should be searched, eg, input.txt")
    return parser.parse_args()


def load_file(args):
    my_file = Path(args.file)

    if my_file.is_file():     # file exists
        # open file and read the text
        file_to_read = open(args.file)
        data = file_to_read.read()
        # save the output
        new_data = replace_strings(data, args)
        return new_data

    else: # it's a string
        string = args.file
        new_data = replace_strings(string, args)
        return new_data


def replace_strings(data, args):
    substrings = args.sedFormat.split('/')
    string_to_find = substrings[1]
    replace_to = substrings[2]
    return re.sub(string_to_find, replace_to, data, 1)


file = load_file(get_arguments())
print(file)
print()

# -------------------------------------------------------------------------------------------------------------------
# Example - python sed.py s/on/ON/ input.txt
'''
 input.txt : The sed utility shall conform to the Base Definitions volume of Utility Syntax Guidelines, except that
 the order of presentation of the -e and -f options is significant.

 output: The sed utility shall cONform to the Base Definitions volume of Utility Syntax Guidelines,
  except that the order of presentation of the -e and -f options is significant.


'''