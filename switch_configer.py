import paramiko
import logging
import time

#define log
logging.basicConfig(filename='configer_log.log', level=logging.DEBUG)


#switches is an array of IP addresses, commands an array of strings, that are cmds given to the devices
def config_switches(switches, commands):
    client = paramiko.SSHClient()
    #tell paramiko to ignore errors related to not having a stored hostkey
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    #parameters for the ssh connection
    username = 'username to login to devices'
    password = 'password to login to devices'
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
    #input name of txt file with list of switch IPs, delineated by \n
    switches_list = raw_input('What switches do you want to configure? \n') 
    #again, txt file with list of cmds. \n delineates commands, needs to end with \n
    cmd_list = raw_input("what commands do you wish to issue? \n") 
     
    switches = open(switches_list).read().splitlines()
    commands = open(cmd_list).read()
    #shows what commands are about to be issued
    print commands
    confirm = raw_input('These commands will be issued. Are you sure you want to continue? Y or N? \n')
    
    if confirm.lower() == 'y':
        config_switches(switches, commands)
    else:
        main()
    
main()
