# Add error handeling



from datetime import datetime
import socket as s

list_of_site = []
list_of_ip = []
currentday = datetime.now().replace(microsecond=0)

def get_ip_addr():
    while True:
        site = input("\nEnter another site or 'q' to exit: ")
        site = site.lower()
        if site == "q":
            break
        else:
            try:
                ip = s.gethostbyname(site)
                print(f"The IP for {site} is {ip}.")
                list_of_site.append(site)
                list_of_ip.append(ip)
            except:
                print("Sorry. That site didn't work.")
                continue

def write_ip_to_list():
    with open("Websites and IPs.txt", 'w') as file:
        file.write(f'This file was created on {currentday}\n')
        for i in range(len(list_of_ip)):                  
            file.write(f'{list_of_site[-1]}:  {list_of_ip[-1]}\n')
            list_of_ip.pop(-1)
            list_of_site.pop(-1)
    print('The websites and IPs have been saved to a text file.')

def main():
    get_ip_addr()
    write_ip_to_list()
    
    
main()
