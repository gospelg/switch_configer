import paramiko
import logging
import time

logging.basicConfig(filename='configer_log.log', level=logging.DEBUG)


def config_switches(switches, commands):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    username = 'uclocal'
    password = 'pswgdlJ63'
    port = 22
    for switch in switches:
        host = switch
        client.connect(hostname=switch, port=port, username=username, password=password)
        print 'connecting...'
        channel = client.invoke_shell()
        std_out = channel.recv(9999)
        #std_err = channel.recv_stderr(9999)
        channel.send(commands)
        time.sleep(1)
        if channel.recv_ready():
            logging.info(channel.recv(9999))
        else:
            logging.info("oops, someting wong")
            
        client.close()
        

def main():
    plink = 'C:\\users\\crosbyg\\desktop\\plink.exe'
    switches_list = raw_input('What switches do you want to configure? \n')
    cmd_list = raw_input("what commands do you wish to issue? \n")
     
    switches = open(switches_list).read().splitlines()
    commands = open(cmd_list).read()
    print commands
     
    config_switches(switches, commands)
    
main()
