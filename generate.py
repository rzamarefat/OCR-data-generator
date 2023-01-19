import os
from PIL import Image, ImageFont, ImageDraw 
import random
from tqdm import tqdm
import cv2
import arabic_reshaper
from bidi.algorithm import get_display
import math

from PIL import Image

def get_bgs():
    bgs = []
    for bg in os.listdir(PATH_TO_BGS):
        absolute_path_bg = PATH_TO_BGS + "/" + bg
        bgs.append(absolute_path_bg)

    return bgs

def get_fonts():
    fonts = []
    for f in os.listdir(PATH_TO_FONTS):
        absolute_path_font = PATH_TO_FONTS + "/" + f
        fonts.append(absolute_path_font)

    return fonts

def get_words():
    words = []
    with open(PATH_TO_WORDS_TXT_FILE, 'r') as f:
        content = f.readlines()
        for c in content: 
            c = c.strip()
            if not(len(c) == 0):
                words.append(c)
    return words


def main():
    fonts = get_fonts()
    words = get_words()
    bgs = get_bgs()

    counter = len([s for s in os.listdir(PATH_TO_GENERATED_IMAGES)])
    while counter <=  NUMBER_OF_IMGS:
        print(f"Image # {counter}")

        fnt_path = fonts[random.randint(0, len(fonts) - 1)]
        random_text = words[random.randint(0, len(words) - 1)]
        words.remove(random_text)
        random_text = random_text.strip()
        
        # print("words", random_text, len(random_text.strip()))

        # random_text = [random_text.replace(item_to_remove, "") for item_to_remove in ["*", "_", "-", "«", "»", "!", "؟", ":", "؛", "'", '"', "-"]][0]
        # chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ")
        # chars = "ا ب پ ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی آ".split(" ")
        # number_of_chars_to_join = random.randint(2, 10)
        # random_txt_as_list = [f"{chars[random.randint(0, len(chars) - 1)]}" for n in range(1, number_of_chars_to_join)]
        # random_text = "".join(random_txt_as_list)

        if len(random_text.strip()) == 0:
            continue


        random_text_reshaped = arabic_reshaper.reshape(random_text)
        random_text_corrected = get_display(random_text_reshaped)
        fnt = ImageFont.truetype(fnt_path, random.randint(70, 80))
        width, height = fnt.getsize(random_text)
        bg_path = bgs[random.randint(0, len(bgs) - 1)]
        bg = Image.open(bg_path)
        bg_width, bg_height = bg.size
        if int(width) == 0 or int(height) == 0:
            continue 

        bg_resized = bg.resize((int(1.3 * width), int(1.3 * height)), Image.LANCZOS)
        bg_resized_width, bg_resized_height = bg_resized.size 
        draw_image = ImageDraw.Draw(bg_resized)

        if bg_path.split("/")[-1].__contains__("dark"):
            color = (random.randint(220, 250),random.randint(220, 250),random.randint(220, 250))
        else:
            color = (random.randint(0, 50),random.randint(0, 50),random.randint(0, 50))
        
        draw_image.text(((bg_resized_width / 2 ), (bg_resized_height / 2)), random_text, color, anchor="mm", font=fnt)
        text_random_angle_for_rotation = random.randint(-35, 35)

        # bg_resized = bg_resized.rotate(text_random_angle_for_rotation, expand=1)
        name_of_new_image = str(counter) + IMAGE_FORMAT
        # name_of_new_image = random_text + IMAGE_FORMAT
        path_to_save_new_image = PATH_TO_GENERATED_IMAGES + "/" + name_of_new_image
        # print("name_of_new_image", name_of_new_image)

        bg_resized = bg_resized.resize((200,50))
        # bg_resized = bg_resized.convert('L')
        if IMAGE_FORMAT == ".tif":
            bg_resized.save(path_to_save_new_image, "TIFF")
        elif IMAGE_FORMAT == '.png':
            bg_resized.save(path_to_save_new_image, "PNG")
        elif IMAGE_FORMAT == ".jpg":
            bg_resized.save(path_to_save_new_image, "JPEG")


        with open(PATH_TO_SAVE_GT_FILE, "a+") as file: 
            file.writelines(path_to_save_new_image)
            file.writelines(" ")
            file.writelines("-->")
            file.writelines(" ")
            file.writelines(random_text)
            file.writelines("\n")
            file.seek(0)

        counter += 1

if __name__ == "__main__":
    NUMBER_OF_IMGS = 1
    PATH_TO_FONTS = os.getcwd() + "/farsi_fonts"
    # PATH_TO_FONTS = os.getcwd() + "/eng_fonts"
    PATH_TO_GENERATED_IMAGES = os.path.join(os.getcwd() , "images")
    # PATH_TO_GENERATED_IMAGES = os.path.join((os.getcwd() , "new_images")
    PATH_TO_SAVE_GT_FILE = os.path.join(os.getcwd(), "gt", "gt.txt")


    PATH_TO_WORDS_TXT_FILE = os.path.join(os.getcwd() , "all_words_ocr.txt")

    PATH_TO_BGS = os.path.join(os.getcwd() , "bgs")

    # IMAGE_FORMAT = ".jpg"
    IMAGE_FORMAT = ".png"
    # IMAGE_FORMAT = ".tif"
    main()
