from __future__ import print_function
import pickle
import sys
import re
import timeit


def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def parse_drivers(drivers_file):
    with open(drivers_file) as f:
        file_data = f.read()
        drivers = re.findall(r"\w*\.sys", file_data, re.IGNORECASE)
    return drivers


def parse_executables(exe_file):
    with open(exe_file) as f:
        file_data = f.read()
        exes = re.findall(r"\w*\.exe", file_data, re.IGNORECASE)
    return exes


def main():
    # setup
    exe_file = sys.argv[1]
    drivers_file = sys.argv[2]
    all_av_drivers = load_data('drivers_data.pkl')
    av_executables = load_data('av_exe_data.pkl')
    # scan file for av exes
    print ('Scanning tasklist for av exe..')
    executables = parse_executables(exe_file)
    for exe in executables:
        if exe in av_executables:
            print ('Found', exe)
    # scan sys drivers
    print ('Scanning drivers for av solutions..')
    found = list()
    all_drivers = parse_drivers(drivers_file)

    for av_name, av_drivers in all_av_drivers.items():
        if any(driver in av_drivers for driver in all_drivers):
            found.append(av_name)
    if len(found) == 0:
        print ('Possible Antivirus solutions found by drivers search: None!')
    else:
        print ('Possible Antivirus solutions found by drivers search: {}'.format(','.join(found)))


if __name__ == '__main__':
    main()
