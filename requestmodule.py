import requests
from bs4 import BeautifulSoup
res=requests.get("https://www.codewithharry.com/blogpost/django-cheatsheet/")
# print(res.text)
# url="https://jsonplaceholder.typicode.com/posts"
# data={
#      "userId": 1,
#     "body": "animal",
#     "title": "dog"
# }
# headers = {
#     "Content-type":"application/json;charset=UTF-8"
    
# }

# res=requests.post(url,headers=headers, json=data)
# # print("data added successfully")
# print(res.text)
preety=BeautifulSoup(res.text,"html.parser")
# print(preety.prettify())
for h in preety.find_all("p"):
    print(h.text)
