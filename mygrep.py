import sys
import argparse
import pdb

GREEN = '\033[92m'
END = '\033[0m'

def myfind(pattern, string, color):
    count = 0
    result = ''
    index = 0
    while index < len(string):
        for j in range(len(pattern)):
            if string[index+j] != pattern[j]:
                result += string[index]
                break   # pattern broke
            elif j == len(pattern) - 1: # pattern match
               if not color:
                   return string # found first match, stop search
               else:
                   count += 1
                   result += GREEN + pattern + END
                   index += j   # jump ahead
        index += 1
    if count == 0:
        result = ''
    return result

if __name__ == '__main__':
    # set up argparse argument parser
    parser = argparse.ArgumentParser(description="Find occurrences of a pattern in a file.")
    parser.add_argument('pattern', metavar="PATTERN", type=str, help="the pattern to find")
    parser.add_argument('filename', metavar="FILENAME", type=argparse.FileType('r'), nargs="?", default=sys.stdin, help="the file to search")
    parser.add_argument('--color', action='store_true', help="highlight pattern in output")

    # unpack args
    args = parser.parse_args()
    pattern = args.pattern
    f = args.filename

    # read lines
    line = f.readline()
    while line:
        result = myfind(pattern, line, args.color)
        if len(result) > 0:
            print result.strip()
        line = f.readline()
