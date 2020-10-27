import os


valid = ['.py']


def count_lines():
    dirs = os.listdir()
    result = 1

    for d in dirs:

        if os.path.isdir(d):
            os.chdir(d)
            result += count_lines()
            os.chdir('..')

        elif os.path.splitext(d)[1] in valid:
            
            with open(d, 'r') as f:
                result += f.read().count('\n')

    return result


print(count_lines() - 28)
quit()