import platform
import subprocess
from plyer import notification

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

while True:
    if ping('www.google.com'):
        print('Running...')
        notification.notify(
            title = 'Internet Status',
            message = 'Internet is ACTIVE.',
            timeout = 10
        )
        break
    else:
        print('Not Running...')
        ping('www.google.com')
