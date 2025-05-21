import requests
from typing import Tuple

url = "https://90c4db3d451c4b8db6070b92436aeb36.api.mockbin.io/"


def get_unique_pet(base_url: str, target_user: str, compare_user: str) -> Tuple[str, str]:
    res = requests.get(base_url)
    if res.status_code == 200:
        print("OK!")
    target_user_res = res.json().get('PetShop').get('Members').get(target_user)
    compare_user_res = res.json().get('PetShop').get('Members').get(compare_user)
    
    if target_user_res is None or compare_user_res is None:
        raise ValueError(f"Can't find {target_user} or {compare_user} in members list." 
                         f"members: {res.json().get('PetShop').get('Members')}")
    
    for k,v in target_user_res.get('Pets').items():
        if k not in compare_user_res.get('Pets').keys():
            return (k, v)

print(get_unique_pet(url, target_user="Julie", compare_user="John"))
