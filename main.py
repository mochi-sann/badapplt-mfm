import os
import re
from PIL import Image


def rgba_to_hex(r, g, b, a):
    return "{:02x}{:02x}{:02x}".format(r, g, b)


def get_file_list(directory):
    file_list = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_list.append(file_path)
    return file_list


def resize_image(image_path, new_size):
    """
    画像を縮小する関数
    :param image_path: 元画像のパス
    :param new_size: 新しいサイズ (タプル形式)
    :return: 縮小された画像オブジェクト
    """
    with Image.open(image_path) as image:
        resized_image = image.resize(new_size)
        return resized_image


def extract_numbers(string):
    result = ""
    for char in string:
        if char.isdigit():
            result += char
    return result


def extract_color(string):

    # match = re.search(r"fg\.color=(\w{6})", string)
    # if match:
    #     return match.group(1)
    # else:
    #     return None
    return string[11:11 + 6]


def is_same_color(a, b) -> bool:
    if extract_color(a) == extract_color(b):
        return True
    else:
        return False


def convertcel(file_name: str):
    cels = []
    img = Image.open(file_name).convert('RGBA')
    width, height = img.size
    imgdata = img.getdata()
    for y in range(height):
        y_offset = y * width
        new_cel = []
        for x in range(width):
            # 画像から色データ取得
            r, g, b, a = imgdata[y_offset+x]

            # セルに設定
            # print(f'$[fg.color={rgba_to_hex(r, g,b,a)} ■]', end="")
            nwe_append_text = f'$[fg.color={rgba_to_hex(r, g,b,a)} ■]'
            # if new_cel and nwe_append_text == new_cel[len(new_cel) - 1]:
            if len(new_cel) > 0 and is_same_color(nwe_append_text, new_cel[len(new_cel) - 1]):
                new_txt = new_cel[len(new_cel) -
                                  1][:-1] + ' ■]'
                new_cel[len(new_cel) - 1] = new_txt

                # # new_cel.append('')
                # new_cel.append(nwe_append_text)
            else:
                new_cel.append(nwe_append_text)

        cels.append(new_cel)
    return cels


def cel_2_text(cels: list[list[str]]):
    # new_txt = "$[position.x=-1.3,y=-2 $[scale.x=0.5,y=0.4"
    new_txt = ""
    for i, value in enumerate(cels):
        add_text = " ".join(value)
        new_txt += add_text
        new_txt += "\n"

    new_txt += ""
    return new_txt


def write_to_file(filename, text):
    # 書き込み先のファイルを開く
    with open(filename, 'w') as f:
        # ファイルに文字列を書き込む
        f.write(text)


def convert_to_5digit(num):
    num_str = str(num)
    if len(num_str) < 5:
        return '0' * (5 - len(num_str)) + num_str
    else:
        return num_str


def main() -> None:
    file_list = get_file_list('./files/new/')
    file_list = sorted(file_list)

    # print(file_list)

    for i, value in enumerate(file_list):
        img_cels = convertcel(value)

        text = cel_2_text(img_cels)

        write_to_file("./files/txt/bad_apple-" +
                      convert_to_5digit(i) + ".txt", text)

        print("write ./files/txt/bad_apple-" +
              convert_to_5digit(i) + ".txt  " + str(len(text)))

    # for file in file_list:


main()

main()
