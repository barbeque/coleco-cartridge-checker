import os, sys
from optparse import OptionParser
import struct

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

sprite_table_address = struct.unpack('<H', rom[2:4])[0]
print(f'Sprite table address {hex(sprite_table_address)}')

sprite_order_table_address = struct.unpack('<H', rom[4:6])[0]
print(f'Sprite order table address {hex(sprite_order_table_address)}')

work_buffer_address = struct.unpack('<H', rom[6:8])[0]
print(f'Work buffer address {hex(work_buffer_address)}')

controller_map_address = struct.unpack('<H', rom[8:10])[0]
print(f'Controller map address {hex(controller_map_address)}')

game_entry_point = struct.unpack('<H', rom[10:12])[0]
print(f'Game entry point address {hex(game_entry_point)}')

# decode name from $8024 and stop at the first
# non-numeric after the second slash
game_name = ''
offset = 0x24
slashes_seen = 0
while True:
    c = chr(rom[offset])
    if c == '/':
        slashes_seen += 1
        game_name = game_name + c
    elif slashes_seen == 2 and (ord(c) not in range(ord('0'),ord('9') + 1)):
        break # terminating
    else:
        game_name = game_name + c
    offset += 1

print(f'Game name "{game_name}"')