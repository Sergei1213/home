import requests

def main():
    try:
        url = str(input("Введіть посилання сайту: ")).strip()
        i = 0
        for i in range(9999999999999):
            r = requests.get(url)
            i = i+1
            print(f"{i}:{r.status_code}")
        
    except:
        pass
if __name__ == "__main__":
    main()