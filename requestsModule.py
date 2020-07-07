import requests

res = requests.get('https://www.kanonierzy.com/')

print(type(res))


print(len(res.text))

print(res.text[:250])

print(res.status_code == requests.codes.ok)

try:
    res.raise_for_status()
except Exception as exc:
    print('Wystąpił następujący problem: {}'.format(exc))