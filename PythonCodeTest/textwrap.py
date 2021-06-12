"""

import textwrap
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

print(wrap(input(), int(input())))
"""

def warp(string, max_width):
    return "\n".join(string[i:i+max_width] for i in range(0, len(string), max_width))
print(warp(input(), int(input())))