#!/usr/bin/env python
"""
pick color shades based on primary colors

Kristofer D. Kusano - 6/15/14
"""
import colorsys

basecolors = [(0, 0, 255), (255, 0, 0), (255, 117, 25), (255, 255, 102), (102, 0, 255), (255, 0, 170)]
hues = [0.5, 0.9, 0.8, 0.7, 0.6, 0.4, 0.3, 0.2]

with open('colors_out.txt', 'w+') as f:
    print('allColors: [', end='', file=f)
    for b in basecolors:
        bh = colorsys.rgb_to_hls(b[0], b[1], b[2])
        for h in hues:
            hh = colorsys.hls_to_rgb(bh[0], h, 1.0)
            print('"#{:02X}{:02X}{:02X}"'.format(int(hh[0]*255), int(hh[1]*255), int(hh[2]*255)), end=",", file=f)
        print('', file=f)
    print('],', file=f)