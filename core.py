import requests
import argparse
import geocoder
import sys
import time
import folium
import webbrowser

def getIP():
	get_api = "https://api.ipify.org?format=json"
	r = requests.get(get_api).json()

	print('Your external ip: ', r['ip'])

def ipTracker(targetIP):
	global latlong
	geo = geocoder.ip(targetIP)
	latlong = geo.latlng
	if len(geo.street) == 0:
		street = 'Null'
	else:
		street = geo.street

	location = {

        '\n# IP': geo.ip,
        '|_ Street': street,
        '|_ City': geo.city,
        '|_ State': geo.state,
        '|_ Country': geo.country,
        '|_ latlng': geo.latlng
    }
	for key in location:
		print(f'{key}: {location[key]}')

def mapDisplayer():
	global latlong
	if latlong == None:
		parser.print_help()
	else:
		my_map = folium.Map(location = latlong, zoom_start = 12 )
		folium.Marker(latlong, popup = ' Current Location ').add_to(my_map)
		my_map.save("map.html")
		webbrowser.open("map.html")

if __name__ == '__main__':

	latlong = None

	print(r"""
U _____ u ____     _   _    ____     _       _____             U  ___ u  _   _     
\| ___"|/|  _"\ U |"|u| |U /"___|U  /"\  u  |_ " _|     ___     \/"_ \/ | \ |"|    
 |  _|" /| | | | \| |\| |\| | u   \/ _ \/     | |      |_"_|    | | | |<|  \| |>   
 | |___ U| |_| |\ | |_| | | |/__  / ___ \    /| |\      | | .-,_| |_| |U| |\  |u   
 |_____| |____/ u<<\___/   \____|/_/   \_\  u |_|U    U/| |\u\_)-\___/  |_| \_|    
 <<   >>  |||_  (__) )(   _// \\  \\    >>  _// \\_.-,_|___|_,-.  \\    ||   \\,-. 
(__) (__)(__)_)     (__) (__)(__)(__)  (__)(__) (__)\_)-' '-(_/  (__)   (_")  (_/  
                   U  ___ u  _   _     _      __   __                              
                    \/"_ \/ | \ |"|   |"|     \ \ / /                              
                    | | | |<|  \| |>U | | u    \ V /                               
                .-,_| |_| |U| |\  |u \| |/__  U_|"|_u                              
                 \_)-\___/  |_| \_|   |_____|   |_|                                
                      \\    ||   \\,-.//  \\.-,//|(_                               
                     (__)   (_")  (_/(_")("_)\_) (__)                              
		""")
	time.sleep(2)
	parser = argparse.ArgumentParser()
	parser.add_argument('-g', '--get-ip', action="store_true", help='Get your external ip address!')
	parser.add_argument('-t', '--target', type=str, help='Get info about the target ip!')
	parser.add_argument('-m', '--map', action='store_true', help='Display the value on a map in a browser page!')
	opts = parser.parse_args()
	ip = opts.get_ip
	target = opts.target
	maps = opts.map

	if len(sys.argv) <= 1:
		parser.print_help()
	if ip:
		getIP()
	if target:
		ipTracker(target)
	if maps:
		mapDisplayer()

