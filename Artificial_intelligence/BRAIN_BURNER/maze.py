#!/usr/bin/env python

from Queue import Queue
from PIL import Image
import numpy as np
import hashlib

start = (1, 1)
end = (3999, 3999)
stack = []

def iswhite(value):
    if value == (255,255,255):
        return True

def getadjacent(n):
    x,y = n
    dxy = [(0,1),(0,-1),(1,0),(-1,0)]
    return [(x+dx, y+dy) for (dx, dy) in dxy if 0 <= x+dx <= 3999 and 0 <= y+dy <= 3999]

def loadImage():
    base_img = Image.open("/home/I309571/my_own/CTF/Artificial_intelligence/data.png")
    base_pixels = base_img.load()
    return base_pixels

def BFS(pixels):
    queue = Queue()
    queue.put([start]) # Wrapping the start tuple in a list

    pixels[1,1] = (127,127,127) # mark start
    while not queue.empty():
        path = queue.get()
        pixel = path[-1]

        if pixel == end:
            return path

        for adjacent in getadjacent(pixel):
            x,y = adjacent
            if iswhite(pixels[x,y]):
                pixels[x,y] = (127,127,127) # mark visited node
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)
    print "Queue has been exhausted. No answer was found."

def DFS(current, pixels):
    stack.append(current)
    if current == end:
        return path
    for adjacent in getadjacent(current):
      x,y = adjacent
      if iswhite(pixels[x,y]):
          pixels[x,y] = (127,127,127) # mark
          DFS(adjacent, pixels)
    stack.pop(-1)

if __name__ == '__main__':
    base_pixels = loadImage()
    path = BFS(base_pixels)

    npath = list()
    for p in path:
        x,y = p
        npath.append((y,x))

    md5 = hashlib.md5(str(npath))
    print (md5.hexdigest())

