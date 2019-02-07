

import requests


def is_page_alive(url):
    r = requests.get(url)
    #print(r.status_code)

    if(r.status_code == 200):
        return True
    else:
        return False


flag = is_page_alive("https://github.com/espressif/esp-mqtt1")

print(flag)