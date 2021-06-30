import os
import keyring

keyringPassword = keyring.get_password("definedLabel", "username")
command = 'yum update -y'
os.system('echo %s|sudo -S %s' % (keyringPassword, command))
