import sys


tab = '    '
replace_backbracket_to = ' '


def remove_braces_from_file(file, suffix='compiled', connector='.'):
    braces = 0

    nobracessource = ''

    ignore_backbraces = 0

    with open(file, 'r') as raw:
        raw = raw.read().splitlines()

    for line in raw:
        tabulated_line = tab * braces + line.strip().strip(tab)
        no_spaces_line = line.replace(' ', '')

        if '{' in line:
            # check, whether warning is False, and brace is just a dict initialize
            if no_spaces_line[no_spaces_line.index('{') - 1] in ['(', '=', '+', ':']:
                ignore_backbraces += 1  # ignore closing brace
                tabulated_line = line
            else:
                braces += 1
                tabulated_line = tabulated_line.strip('{')

                if tabulated_line[-1] == ' ':
                    tabulated_line = tabulated_line[:-1]

                tabulated_line += ':'

        if '}' in line:
            if ignore_backbraces > 0:
                ignore_backbraces -= 1
            else:
                braces -= 1

                tabulated_line = tabulated_line.replace('}', replace_backbracket_to)

                if tabulated_line.strip().endswith(':'):
                    tabulated_line = tabulated_line[:-1]

                if tabulated_line.strip() in [':']:
                    continue

        if tabulated_line == line.strip():
            tabulated_line = line

        nobracessource += tabulated_line + '\n'

    try:
        new_filename = file.split('.')
        new_filename = '.'.join(new_filename[:-1]) + connector + suffix + '.py'  # add suffix before .py extension
        # new_filename.insert(-1, suffix)

        with open(new_filename, 'w') as modified_file:
            if not nobracessource.endswith('\n'): nobracessource += '\n'    # PEP8: file should end with a newline
            modified_file.write(nobracessource)

        print('[COMPILED]', file, '-->', new_filename)

        return new_filename
    except PermissionError:
        print('[ERROR] Permission denied to write a modified source. Please, run me with a sudo or smth like that')
        sys.exit()


if __name__ == '__main__':
    files = sys.argv[1:]

    if len(files) == 0:
        print('[USAGE] python3 braces-to.py <files>')
        sys.exit()

    for file in files:
        remove_braces_from_file(file)
