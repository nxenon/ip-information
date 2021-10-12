import requests
try :
    import colorama
except :
    print('colorama is not installed !')
    print('Try installing colorama')
    import os
    try:
        os.system('pip3 install colorama')
    except:
        print('Installing (colorama) failed ! try to install it manually !')
        exit()
    else:
        from colorama import Fore
else:
    from colorama import Fore

class IpInfo():
    def __init__(self,url):
        self.url = url

    def check_status(self):
        query_check = requests.get(self.url)
        self.query_check_json = query_check.json()
        if self.query_check_json['status'] == 'success' :
            return 'success'
        else:
            print(Fore.RED,'Invalid IP or FQDN !',Fore.RESET)
            return 'failed'

    def get_info(self):
        info = self.query_check_json
        print("")
        print('Target :    ',Fore.CYAN,info['query'],Fore.RESET)
        print('Country :   ',Fore.CYAN,info['country'],Fore.RESET)
        print('RegionName :',Fore.CYAN,info['regionName'],Fore.RESET)
        print('City :      ',Fore.CYAN,info['city'],Fore.RESET)
        print('TimeZone :  ',Fore.CYAN,info['timezone'],Fore.RESET)
        print('ISP :       ',Fore.CYAN,info['isp'],Fore.RESET)
        print("")
        print('Location based on lat and lon in google map :')
        google_map_prefix = 'https://www.google.com/maps/place/'
        lat_and_lon = str(info['lat']) + "," + str(info['lon'])
        google_map_location = google_map_prefix + lat_and_lon
        print(Fore.GREEN,google_map_location,Fore.RESET)
        print("")

url_prefix = 'http://ip-api.com/json/'
yes_list = ['yes','y','yeah','yup']

while True :
    print(Fore.YELLOW,"If you wanna get your IP info type (me)",Fore.RESET)
    target = input('Target IP address or FQDN :').lower().strip()

    if target == 'me' :
        target = ''
    elif target == '' :
        print(Fore.YELLOW,'You entered nothing so that your IP address will be checked.',Fore.RESET)

    url = url_prefix + target
    target_ip_info = IpInfo(url)
    target_status = target_ip_info.check_status()

    if target_status == 'success' :
        # printing ip information
        target_ip_info.get_info()
        again_or_not = input('again (y)? :').lower().strip()
        if again_or_not in yes_list:
            continue
        else:
            break

    elif target_status == 'failed' :
        again_or_not = input('again (y)? :').lower().strip()
        if again_or_not in yes_list :
            continue
        else:
            break

print(Fore.CYAN,'Bye...',Fore.RESET)
exit()
