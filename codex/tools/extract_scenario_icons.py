"""Extract the icons of the Scenario Editor units from an AoE2 DE installation.

Usage (from the repository root, with genieutils-py installed, e.g. in scripts/venv):
    scripts/venv/Scripts/python codex/tools/extract_scenario_icons.py "<AoE2DE folder>"

Reads the game's data file for each unit's icon number and the game's unit icons
(widgetui/textures/ingame/units/<icon>_50730.dds, uncompressed 32-bit DDS); nothing in the
installation is modified. For the units listed in codex/tools/scenario-units-stats.json it writes:
  - img/Unit/codex-<icon>.png                 48x48 icons that the site does not have yet
  - codex/tools/scenario-units-icons.json     unit name -> picture index for the site's trees
An icon the site already has (img/Unit/<icon>.png) is used as it is.
"""
import json
import struct
import sys
import zlib
from pathlib import Path

from genieutils.datfile import DatFile

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / 'codex' / 'tools'
SIZE = 48


def read_dds(path):
    """Pixels of an uncompressed 32-bit DDS as rows of (r, g, b, a)."""
    raw = path.read_bytes()
    if raw[:4] != b'DDS ':
        raise ValueError(f'{path.name}: not a DDS file')
    height, width = struct.unpack_from('<II', raw, 12)
    flags, fourcc, bits, rmask, gmask, bmask, amask = struct.unpack_from('<I4sIIIII', raw, 80)
    if not flags & 0x40 or bits != 32:
        raise ValueError(f'{path.name}: only uncompressed 32-bit DDS is supported')
    shifts = [(m & -m).bit_length() - 1 if m else None for m in (rmask, gmask, bmask, amask)]
    masks = (rmask, gmask, bmask, amask)
    pixels = struct.unpack_from(f'<{width * height}I', raw, 128)
    rows = []
    for y in range(height):
        row = []
        for x in range(width):
            v = pixels[y * width + x]
            row.append(tuple(((v & m) >> s) if m else 255 for m, s in zip(masks, shifts)))
        rows.append(row)
    return rows


def weights(src, dst):
    """Area-average weights: for each output index, the (source index, weight) pairs."""
    scale = src / dst
    out = []
    for i in range(dst):
        start, end = i * scale, (i + 1) * scale
        pairs = []
        j = int(start)
        while j < end and j < src:
            w = min(end, j + 1) - max(start, j)
            if w > 0:
                pairs.append((j, w / scale))
            j += 1
        out.append(pairs)
    return out


def resize(rows, size):
    """Shrink with area averaging, in premultiplied alpha."""
    h, w = len(rows), len(rows[0])
    pre = [[(r * a, g * a, b * a, a) for r, g, b, a in row] for row in rows]
    wx, wy = weights(w, size), weights(h, size)
    horiz = [[tuple(sum(row[j][c] * wt for j, wt in pairs) for c in range(4)) for pairs in wx] for row in pre]
    out = []
    for pairs in wy:
        line = []
        for x in range(size):
            r, g, b, a = (sum(horiz[j][x][c] * wt for j, wt in pairs) for c in range(4))
            if a > 0:
                line.append(tuple(min(255, round(v / a)) for v in (r, g, b)) + (min(255, round(a)),))
            else:
                line.append((0, 0, 0, 0))
        out.append(line)
    return out


def write_png(path, rows):
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data) & 0xffffffff)
    h, w = len(rows), len(rows[0])
    raw = b''.join(b'\x00' + bytes(v for px in row for v in px) for row in rows)
    png = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))
           + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))
    path.write_bytes(png)


def main():
    game = Path(sys.argv[1])
    dat = DatFile.parse(str(game / 'resources' / '_common' / 'dat' / 'empires2_x2_p1.dat'))
    units = dat.civs[0].units
    stats = json.loads((TOOLS / 'scenario-units-stats.json').read_text(encoding='utf-8'))
    icons = {}
    for name, rows in stats.items():
        if not rows:
            continue
        icon = units[rows[0]['id']].icon_id
        if icon < 0:
            continue
        if (ROOT / 'img' / 'Unit' / f'{icon}.png').exists():
            icons[name] = icon
            continue
        dds = game / 'widgetui' / 'textures' / 'ingame' / 'units' / f'{icon:03d}_50730.dds'
        if not dds.exists():
            print(f'{name}: no icon file for icon {icon}')
            continue
        try:
            pixels = read_dds(dds)
        except ValueError as e:
            print(f'{name}: skipped ({e})')
            continue
        write_png(ROOT / 'img' / 'Unit' / f'codex-{icon}.png', resize(pixels, SIZE))
        icons[name] = f'codex-{icon}'
    (TOOLS / 'scenario-units-icons.json').write_text(json.dumps(icons, indent=1, ensure_ascii=False) + '\n',
                                                     encoding='utf-8', newline='\n')
    print(f'{len(icons)} icons mapped')


if __name__ == '__main__':
    main()
