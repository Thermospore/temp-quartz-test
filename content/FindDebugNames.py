#!/usr/bin/env python3

import argparse
from pathlib import Path
import re

def main():
    # Read WAD file
    ap = argparse.ArgumentParser()
    ap.add_argument('wad_file', type=Path)
    args = ap.parse_args()
    wad = args.wad_file.read_bytes()

    # Find stDebugName calls (ST_DEBUGNAME followed by ST_STRING)
    # Croc2: 0xB0 0xD4. TENG/Aladdin: 0xD4 0xEA.
    pattern = br'(?:\xB0\0\0\0\xD4\0\0\0|\xD4\0\0\0\xEA\0\0\0)(....)'
    for m in re.finditer(pattern, wad, re.DOTALL):
        start = m.end() + int.from_bytes(m[1], 'little', signed=True)
        end = wad.find(b'\0', start)
        print(wad[start:end].decode('ascii'))

if __name__ == '__main__':
    main()
