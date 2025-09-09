import requests

url = "https://panel.aiguard2.top/vp3cSLc0juM/25e19963-5e35-4416-8fd3-3245d287a0cb/sub/?asn=unknown#Saeed-test"  # replace
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Error:", response.status_code)
