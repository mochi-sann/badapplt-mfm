import requests
import json
import os
MISSKEY_TOKEN = "4xwIuw5r4p9J7nSRTteMeEqJ7JRtVkV6"


def get_text_files(directory: str) -> list[str]:
    """
    特定のディレクトリの下にあるテキストファイルの一覧を取得する関数

    Parameters:
    ----------
    directory : str
        ディレクトリのパス

    Returns:
    -------
    list
        テキストファイルのパスのリスト
    """
    text_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                text_files.append(os.path.join(root, file))
    return text_files


def append_to_file(file_path: str, text: str) -> None:
    with open(file_path, 'a') as file:
        file.write(text + '\n')


def post_and_file_write(body: str):
    url = "http://localhost:3000/api/notes/create"

    payload = json.dumps({
        "i": "4xwIuw5r4p9J7nSRTteMeEqJ7JRtVkV6",
        "text": body
    })
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()

    print(response_data["createdNote"]["id"])
    append_to_file("notes_id.txt", response_data["createdNote"]["id"])


def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content


def main():
    txt_files = get_text_files("./files/txt/")
    txt_files = sorted(txt_files)
    for txt_file in txt_files:
        text_file_value = read_file(txt_file)
        print("read " + txt_file)
        post_and_file_write(text_file_value)

# print(txt_files)


main()
