import os, sys
from optparse import OptionParser

parser = OptionParser()

(options, args) = parser.parse_args()

if len(args) < 1:
    parser.print_usage()
    sys.exit(1)

with open(args[0], 'rb') as f:
    rom = bytes(f.read())

if rom[0] == 0xaa and rom[1] == 0x55:
    print('Game type')
elif rom[0] == 0x55 and rom[1] == 0xaa:
    print('Test type')
else:
    print(f'Unknown rom type {hex(rom[0])} {hex(rom[1])} - may be bad dump')