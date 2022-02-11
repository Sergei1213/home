import string
import secrets
import requests
from datetime import datetime
import time 

def main():
    current_time = datetime.now()
    string_time = str(current_time.time())
    good_time_str = string_time[:8]

    curent_day = current_time.day  
    string_day = str(curent_day)
    letters_and_digits = string.ascii_lowercase + string.digits
    crypt_rand_string = ''.join(secrets.choice(letters_and_digits) for i in range(16))

    addres = ''.join(secrets.choice(letters_and_digits) for i in range(42))
    url = "https://api.blockchain-infos.com/api/v1/sign-up/bitcoin"

    json = {
        "message": "dopamine Thu Feb "f'{curent_day}'" 2022 "f'{good_time_str}'" GMT+0300",
        "address": f"{addres}",
        "signature": "J4Ku+4DASKZnUKjmKqJsIWAYkcdq7QmZToDjhaEiCaf6OWiIiC+ZetyafoEbPHQMfytJF7xt7msPUox7Ld2hrw0=",
        "referred_from_referral_code": "Z6G2N0D8",
        "unique_device_id": f"{crypt_rand_string}"
    }

    lea = len(str(json))
    headers = {
        'accept':'application/json',
        'accept-encoding':'gzip',
        'connection':'Keep-Alive',
        'content-length':f'{lea}',
        'content-type':'application/json',
        'host':'api.blockchain-infos.com',
        'user-agent':'okhttp/3.12.12'
    }

    r = requests.post(url, json, headers)
    global status
    status = r.status_code
    time.sleep(1)
    
    return status
    


if __name__ == "__main__":
    n = int(input("Enter number: "))
    i = 0
    for i in range(n):
        try:
            main()
            i = i+1
            print(""f'{i}'": ["f'{status}'"]")
        except:
            print("[ERROR]")
