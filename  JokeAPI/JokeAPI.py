import json
import requests
import pandas as pd


def get_joke():
    r = requests.get("https://official-joke-api.appspot.com/jokes/ten")
    result = json.loads(r.text)
    return result


def main():
    df = pd.DataFrame(get_joke())
    df.drop(columns=["type", "id"], inplace=True)
    print(df)


if __name__ == '__main__':
    main()
