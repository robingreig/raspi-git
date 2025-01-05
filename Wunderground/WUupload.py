import requests

ambient_tempc=-15.83
print("ambient_tempc: ",ambient_tempc)
ambient_tempf = (ambient_tempc *1.8)+32
print("ambient_tempf: ",ambient_tempf)

# create a string to hold the first part of the URL

WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
WU_station_id = "IROCKYVI10"
WU_station_pwd = "nmxihjyz"
WUcreds = "ID=" + WU_station_id + "&PASSWORD="+ WU_station_pwd
date_str = "&dateutc=now"
action_str = "&action=updateraw"

temp_str = "{0:.2f}".format(ambient_tempf)
print("temp_str: ",temp_str)

r = requests.get(
	str(WUurl) +
	str(WUcreds) +
	str(date_str) +
	"&tempf=" + str(temp_str) +
	str(action_str))

#r= requests.get(
#    WUurl + 
#    WUcreds + 
#    date_str + 
#    "&tempf=" + temp_str + 
#    action_str)


print("Received " + str(r.status_code) + " " + str(r.text))
