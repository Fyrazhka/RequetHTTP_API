import os

import requests


def main():
    url_get = 'https://www.ibm.com/'
    r = requests.get(url_get)
    print(r.text)
    url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
    path = os.path.join(os.getcwd(),'example1.txt')
    r = requests.get(url)
    with open(path,'wb') as f:
        f.write(r.content)
    payload = {"name": "Joseph", "ID": "123"}
    r = requests.get(url_get, params=payload)
    url_post = 'http://httpbin.org/post'
    r_post = requests.post(url_post, data=payload)
    print(r_post.status_code)


if __name__ == '__main__':
    main()
