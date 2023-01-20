import argparse

parser = argparse.ArgumentParser(description='OCR data generator')

parser.add_argument('--bgs', default='./bgs', type=str, help='root to background images')
parser.add_argument('--gt-save-path', default='./gt.txt', type=str, help='path to save gt file (.txt)')
parser.add_argument('--images-save-path', default='./images', type=str, help='root path to save generated image file')
parser.add_argument('--image-number', default='10', type=str, help='number of required images')
parser.add_argument('--words-corpus', default='10', type=str, help='path to a txt file containing words in each row')


args = parser.parse_args()

def generate(args):
    print(args)

if __name__ == "__main__":
    generate(args)