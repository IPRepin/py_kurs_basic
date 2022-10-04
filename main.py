from config import vk_token
from config import version
from config import url_vk
from config import yd_token
from pprint import pprint
import pandas as pd
import json
import time
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
        return req




    def photo_file(self, reg):
        file_dic = {}
        for file in req[0]['sizes']['type']:
            for name in req['date']:
                for url in req['url']:
                    if file == 'z':
                        file_dic[url] = name
        pprint(file_dic)


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.yd_id)}

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        url_file_path = None # доделать логику получения ссылки на файл
        params = {"path": url_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()



def main():
    vk_id = input('Введите id пользователя: ')
    vk_client = vk_foto_in_yd(vk_id, yd_token)
    # pd.DataFrame(vk_client.photos_get())
    # pprint(vk_client.photos_get())
    vk_client.photos_get()
    vk_client.photo_file(vk_client.photos_get())



if __name__ == '__main__':
    main()
