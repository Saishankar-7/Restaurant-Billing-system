import requests  
 
url= 'https://www.fast2sms.com/dev/bulkV2'


querystring={
    'authorization':'sBRw4GJfWrzOZ5IcSQmvdyLPTagKtjo1kiA8XUV07lqnuxeMDpebLT5mcA6EB2JUfWtMH9XaDIuqxk8C',
    'sender-id':'FSTSMS',
    'language':'english',
    'route':'p',
    'numbers':'7997113028'
}
headers={
    'cache-control':'no-cache'
   
}
response= requests.request("GET",url,headers=headers,params=querystring)

print(response.text)