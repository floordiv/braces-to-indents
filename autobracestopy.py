import os
import sys
import importlib
from multiprocessing import Process
braces_to = importlib.import_module('braces-to')


args = sys.argv[1:]

if len(args) == 0 or not os.path.isfile(args[0]):
    print('[ERROR] please, enter valid file to compile')
    sys.exit()

filename = args[0]
compiled_file = '.'.join(filename.split('.')[:-1]) + '_compiled.py'  # add suffix before .py extension



config = {
    'remove-after-finishing': False,
    'rebuild': True,
}


def run_file(file):
    importlib.import_module(file.replace('/', '.'))

    if config['remove-after-finishing']:
        os.remove(file)


for val, key in zip(config.keys(), [bool, bool]):     # parse arguments
    if '--' + val in args:
        config[val] = key(args[args.index('--' + val) + 1])


if config['rebuild'] or not os.path.isfile(compiled_file):
    compiled_file = braces_to.remove_braces_from_file(filename, 'compiled', '_')


Process(target=run_file, args=(compiled_file[:-3],)).start()
