import requests

ambient_temp=-15.83

# create a string to hold the first part of the URL

WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
WU_station_id = "IROCKYVI10"
WU_station_pwd = "nmxihjyz"
WUcreds = "ID=" + WU_station_id + "&PASSWORD="+ WU_station_pwd
date_str = "&dateutc=now"
action_str = "&action=updateraw"

temp_str = "{0:.2f}",format(ambient_temp)

r= requests.get(
    WUurl +
    WUcreds +
    date_str +
    "&tempf=" + temp_str +
    action_str)

print("Received " + str(r.status_code) + " " + str(r.text))
