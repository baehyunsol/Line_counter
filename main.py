import os


valid = ['.py', '.c', '.md', '.rs', '.cpp', '.h', '.json']


def count():

    lines = {}
    chars = {}
    files = {}

    for v in valid:
        lines[v] = 0
        chars[v] = 0
        files[v] = 0

    dirs = os.listdir()

    for d in dirs:

        if os.path.isdir(d):
            os.chdir(d)
            child_lines, child_chars, child_files = count()

            for v in valid:
                lines[v] += child_lines[v]
                chars[v] += child_chars[v]
                files[v] += child_files[v]

            os.chdir('..')

        elif os.path.splitext(d)[1] in valid:

            with open(d, 'r') as f:
                ff = f.read()
                lines[os.path.splitext(d)[1]] += ff.count('\n') + 1
                chars[os.path.splitext(d)[1]] += len(ff)
                files[os.path.splitext(d)[1]] += 1

    return lines, chars, files


def wrapper_count():

    lines, chars, files = count()

    valids = [x for x in files if files[x] > 0]
    result = {}

    for v in valids:
        result[v] = {
            'files': files[v],
            'lines': lines[v],
            'chars': chars[v]
        }

    return result


print(wrapper_count())
