from config import vk_token
from config import version
from config import url_vk
from config import yd_token
from pprint import pprint
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



def main():
    # vk_id = input('Введите id пользователя: ')
    vk_client = vk_foto_in_yd(304437267, yd_token)
    pprint(vk_client.photos_get())

if __name__ == '__main__':
    main()
