import paramiko
import logging

logging.basicConfig(filename='configer_log.log', level=logging.DEBUG)


def config_switches(switches, commands):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    username = uclocal
    password = pswgdlJ63
    port = 22
    for switch in switches:
        host = switch
        client.connect(hostname=switch, port=port, username=username, password=password)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        stdin.write(commands)
        logging.info(stdout.read())
        stdout.close()
        stdin.close()
        client.close()
        

def main():
    plink = 'C:\\users\\crosbyg\\desktop\\plink.exe'
    switches_list = raw_input('What switches do you want to configure? \n')
    cmd_list = raw_input("what commands do you wish to issue? \n")
     
    switches = open(switches_list).read().splitlines()
    commands = open(cmd_list).read()
     
    config_switches(switches, commands)
    
main()
