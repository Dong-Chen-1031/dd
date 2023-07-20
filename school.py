import requests

url = "http://163.20.9.3/qstudent/login.asp"

# payload = 'stud_no=155003&password=FF849117'

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
form_data = {
    'stud_no': '155003',
    'password': 'FF849117'
}
response = requests.post(url, data=form_data,headers=headers)


url = "http://163.20.9.3/qstudent/bitem_sco1.asp"
# coo={response.cookies["ASPSESSIONIDCSTQBSSS"]}
coo='ILEKEKFCDLLAPNJMNDPMHCEA'
headers = {
  'Cookie': f"ASPSESSIONIDCSTQBSSS={coo}"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

