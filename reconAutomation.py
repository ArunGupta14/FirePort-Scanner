import subprocess
import argparse
import socket

def recon(host):
    temp_host = host
    hostIp = socket.gethostbyname(host)
    
    def waf_tool(temp_host):
        with open('f1.txt','a')as f:
            cmd = subprocess.getoutput(f'wafw00f {temp_host}')
            f.write(cmd)

    def nmap_tool(hostIp):
        with open('f1.txt','a')as f:
            cmd = subprocess.getoutput(f'nmap -v -A {hostIp}')
            f.write(cmd) 

    # calling fun tools
    waf_tool(temp_host)
    nmap_tool(hostIp)
    print('Your target data successfully store on f1.txt file')

parse = argparse.ArgumentParser(description='''This is the Reconnaissance automation tool. To help gather information of Target. It take Target host name or IP address. In backend it use nmap, dnsenum ''')

parse.add_argument('host', help='Give the host name required.')
parse.add_argument('--IP', help="Enter the target Ip")

data = parse.parse_args()

print("The Target is: ",data.host)
print('Please wait...')

if data.host == None:
    print('Please give the host name')
    exit()
else:
    try:
        recon(data.host)
    except socket.gaierror: 
        print("Please enter the correct host name")

