from PIL import Image
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type = int , default = 80)
parser.add_argument('--height',type = int , default = 80)
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height

print('IMG IS :' + str(IMG))
print('WIDTH IS :' + str(WIDTH))
print('Height is :' + str(HEIGHT))

# ascii_char = list("@#&$*ox!i;.")
#
# def get_char(r,g,b,alpha = 256):
#     if alpha == 0:
#         return ' '
#     length = len(ascii_char)
#     gray = int(0.299 * r + 0.578 * g +0.1414 *b)
#     uint = ()