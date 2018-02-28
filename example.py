import sys
sys.stderr = open('/dev/null')       # Silence silly warnings from paramiko
import paramiko as pm
sys.stderr = sys.__stderr__
import os

class AllowAllKeys(pm.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

HOST = '127.0.0.1'
USER = ''
PASSWORD = ''

client = pm.SSHClient()
client.load_system_host_keys()
client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
client.set_missing_host_key_policy(AllowAllKeys())
client.connect(HOST, username=USER, password=PASSWORD)

channel = client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

stdin.write('''
cd tmp
ls
exit
''')
print stdout.read()

stdout.close()
stdin.close()
client.close()
