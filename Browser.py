import os
import datetime
from selenium import webdriver
import time


def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content


def Broser_and_ss(note_id,  number, driver):
    driver.get("http://localhost:3000/notes/" + note_id)

    # ウインドウサイズをWebサイトに合わせて変更　※全画面用
    # width = driver.execute_script("return document.body.scrollWidth;")
    # height = driver.execute_script("return document.body.scrollHeight;")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, " + str(150) + ");")

    time.sleep(0.5)

    # スクショをPNG形式で保存
    driver.get_screenshot_as_file("./files/ss/" + number + ".png")


def split_string_by_newline(string):
    """
    改行で区切られた文字列を受け取り、各行を要素とする配列を返す関数。
    """
    return string.split('\n')


def convert_to_5digit(num):
    num_str = str(num)
    if len(num_str) < 5:
        return '0' * (5 - len(num_str)) + num_str
    else:
        return num_str


def main():

    noteid_text_file = read_file("./notes_id.txt")
    noteid_arry = split_string_by_newline(noteid_text_file)
    # ヘッドレス実行　※全画面用
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # ブラウザ起動
    driver = webdriver.Chrome()

    # 保存する画像ファイル名
    fname = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S asdf')

    # スクショ保存ディレクトリが存在しなければ生成

    driver.set_window_size(1000, 900)
    driver.get("http://localhost:3000/notes/9c0h6nppzz")
    time.sleep(5)

    for i, value in enumerate(noteid_arry):
        # テスト用URLに接続（郵便局、深い意味はないです。。。）
        driver.get("http://localhost:3000/notes/" + value)

        # ウインドウサイズをWebサイトに合わせて変更　※全画面用
        # width = driver.execute_script("return document.body.scrollWidth;")
        # height = driver.execute_script("return document.body.scrollHeight;")
        time.sleep(1.5)
        driver.execute_script("window.scrollTo(0, " + str(150) + ");")

        time.sleep(0.5)

        # スクショをPNG形式で保存
        driver.get_screenshot_as_file(
            "./files/ss/" + convert_to_5digit(i) + ".png")
        print(convert_to_5digit(i))

    # driver.get("http://localhost:3000/notes/9c0h6nlxzw")
    #
    # # ウインドウサイズをWebサイトに合わせて変更　※全画面用
    # # width = driver.execute_script("return document.body.scrollWidth;")
    # # height = driver.execute_script("return document.body.scrollHeight;")
    # time.sleep(3)
    # driver.execute_script("window.scrollTo(0, " + str(150) + ");")
    #
    # time.sleep(0.5)
    # # スクショをPNG形式で保存
    # driver.get_screenshot_as_file("./files/ss/" + fname + "new.png")
    driver.quit()


main()
