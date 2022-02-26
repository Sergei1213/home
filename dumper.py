import requests

def main():
    try:
        i = 0
        for i in range(9999999999999):
            r = requests.get("https://lenta.ru/rubrics/media/")
            i = i+1
            print(f"{i}:{r.status_code}")
        
    except:
        pass
if __name__ == "__main__":
    main()