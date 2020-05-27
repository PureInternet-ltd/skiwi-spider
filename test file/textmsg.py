import urllib.request
import json

msgtext = "%E6%82%A8%E5%A5%BD%EF%BC%8C%E6%88%91%E4%BB%AC%E6%B3%A8%E6%84%8F%E5%88%B0%E6%82%A8%E5%8F%91%E5%B8%83%E6%96%B0%E7%9A%84%E7%A7%9F%E6%88%BF%EF%BC%8CRental%20NZ%E5%85%8D%E8%B4%B9%E5%8F%91%E5%B8%83%E7%A7%9F%E6%88%BF%EF%BC%8C%E7%BD%91%E5%9D%80%EF%BC%9A%20http%3A%2F%2Frentalnz.co.nz%2F%20%E5%AE%A2%E6%9C%8D%E5%BE%AE%E4%BF%A1%EF%BC%9ARentalNZ"

url="http://101.100.3.114:8778/sendsms?username=smsuser&password=itauckland0903&phonenumber=0220335015&message="+msgtext
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
data=resp.read().decode('utf-8')
y = json.loads(data)

print(y["report"][0]["1"][0]["result"])

# data=resp.read().decode('utf-8')
# ms = '{"message":"xxx","report":[{"1":[{"port":"umts-1.4","phonenumber":"0220335015","time":"2020-05-25 12:33:24","result":"success"}]}]}'

# print(y["message"])