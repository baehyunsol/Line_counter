import os


valid = ['.py', '.c', '.md', '.rs', '.cpp', '.h', '.json']


def count_lines_and_chars():

    lines = {}
    chars = {}

    for v in valid:
        lines[v] = 0
        chars[v] = 0

    dirs = os.listdir()

    for d in dirs:

        if os.path.isdir(d):
            os.chdir(d)
            child_lines, child_chars = count_lines_and_chars()

            for v in valid:

                if child_lines[v] > 1:
                    lines[v] += child_lines[v]

                chars[v] += child_chars[v]

            os.chdir('..')

        elif os.path.splitext(d)[1] in valid:

            with open(d, 'r') as f:
                ff = f.read()
                lines[os.path.splitext(d)[1]] += ff.count('\n') + 1
                chars[os.path.splitext(d)[1]] += len(ff)

    return lines, chars


print(count_lines_and_chars())
