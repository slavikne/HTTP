import requests
from pprint import pprint
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        API_BASE_URL = "https://cloud-api.yandex.net/"
        headers = {
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        response = requests.get(API_BASE_URL + "v1/disk/resources/upload", params={'path': file_path},
                                headers=headers)
        upload_url = response.json()["href"]
        response = requests.put(upload_url, headers=headers, files={'file': open('foto.jpg', "rb")})

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'homework/foto.jpg'
    token = ' '
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

