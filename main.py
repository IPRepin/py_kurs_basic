from config import vk_token
from config import version
from config import url_vk
from config import yd_token
from pprint import pprint
from tqdm import tqdm
import json
import requests
class vk_foto_in_yd():
    def __init__(self, vk_id, yd_id):
        self.params_vk = {
            'owner_id': vk_id,
            'access_token': vk_token,
            'v': version
        }
        self.yd_id = yd_id

    def photos_get(self, count=10):
        photos_get_url = f'{url_vk}/photos.get'
        photos_get_params = {
            'album_id': 'profile',
            'count': count,
            'extended': 'likes',
            'photo_sizes': '1',
        }
        req = requests.get(f'{photos_get_url}', params={**self.params_vk, **photos_get_params}).json()
        req_json = req['response']['items']
        return req_json


    def photo_file(self):
        fotos = []
        photos_def = self.photos_get()
        for item in photos_def:
            liks_count = item['likes']['count']
            date = item['date']
            name = f'{liks_count}_{date}.jpg'
            max_photo = item['sizes'][-1]
            photo_dict = {"name": name, "type": max_photo['type'], "url": max_photo['url']}
            fotos.append(photo_dict)
        self.save_to_json(fotos)
        return fotos

    def save_to_json(self, photo):
        with open('photo_json', 'w', encoding='utf8') as photo_file:
            json.dump(photo, photo_file)


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.yd_id)}

    def yd_folder(self):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        params = {"path": "vk-photo"}
        folder = requests.put(folder_url, params=params)
        return folder
    def yd_upload(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        photos_lst = self.photo_file()
        folder_path = self.yd_folder()
        for item in photos_lst:
            url = item['url']
            params = {"path": folder_path, "url": url}
            upload = requests.post(upload_url, params=params)
            return upload

def main():
    vk_id = input('Введите id пользователя: ')
    vk_client = vk_foto_in_yd(vk_id, yd_token)
    vk_client.photos_get()
    vk_client.photo_file()
    # vk_client.save_to_json()
    vk_client.get_headers()
    vk_client.yd_folder()
    vk_client.yd_upload()


if __name__ == '__main__':
    main()
