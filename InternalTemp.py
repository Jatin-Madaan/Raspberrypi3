# show the temperature of processor on thinkspeak pi3 B+
import http.client
import urllib
import sys
import time as t
sleep = 5
key = 'GLJXKZ99OR14PDB7'
def temperature():
    while True:
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())
        temp = temp / 1000
        params = urllib.parse.urlencode({'field1' : temp, 'key': key})
        headers = {"Content-typeZZe" : "application/x-www-form-urlencoded","Accept":"text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST","/update",params,headers)
            response = conn.getresponse()
            print(temp)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        t.sleep(sleep)
temperature()
