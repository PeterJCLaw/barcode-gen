#!/usr/bin/env python3
import time
import argparse
import re
import pyqrcode
import io

parser = argparse.ArgumentParser()
parser.add_argument('codes', metavar='NNNNNNNN', nargs='+', help="list of codes to generate (with or without dashes)")
args = parser.parse_args()

# sanitise codes, so we can support both with and without dashes.
codes =  args.codes
# translate(-10,0) scale(0.7, 1.2)
template = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg
  PUBLIC '-//W3C//DTD SVG 1.1//EN'
  'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>
<svg height="29.000mm" version="1.1" width="90.300mm" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(-2,-2)">
{bar}
</g>
<g>
<text
x="255"
y="61"
style="fill:black;font-size:16pt;text-anchor:middle;"
>
{code}
</text>
</g>
</svg>"""
for code in codes:
    out_file = code+".svg"
    qr = pyqrcode.create(code)
    svg = io.BytesIO()
    qr.svg(svg, scale=4)
    svg_content = svg.getvalue().decode("utf-8")
    svg_content = '\n'.join(svg_content.split('\n')[1:])
    with open(out_file,'w') as o:
        print(template.format(bar=svg_content,code=code),file=o)
