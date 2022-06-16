import requests
from crud import CRUD
from mixins import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin



crud = CRUD()
print(crud.list_records())
print(crud.retrieve_record('rec9If55CnO9RbQHf'))
print(crud.create_record())
print(crud.update_record('rec9If55CnO9RbQHf'))
print(crud.delete_record('rec9If55CnO9RbQHf'))
print(crud.retrieve_record('rec9If55CnO9RbQHf'))









# headers = {
#     "Accept": "application/json",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,de-DE;q=0.7,de;q=0.6",
#     "Content-Length": "0",
#     "Host": "httpbin.org",
#     "Origin": "https://httpbin.org",
#     "Referer": "https://httpbin.org/",
#     "Sec-Ch-Ua": r"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": r"\"Linux\"",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
#     "X-Amzn-Trace-Id": "Root=1-62a98b97-41d68ff11f2bb0475d5e342e"
#   }

# b = requests.get('https://httpbin.org/user-agent', headers=headers)
# print(b.text)