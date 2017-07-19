import platform
import psutil
import shutil
import socket
from threading import Thread
import time

print('System Information')
print('Operating system: ' + platform.system())
user_name = [x[0] for x in psutil.users()]
print('User Name: ' + user_name[0])
print('Computer Name: ' + platform.node())

if '64' in platform.machine():
    print('Architecture: 64bit')
else:
    print('Architecture: 32bit')

print('Machine: ' + platform.machine())
print('Processor: ' + platform.processor())

try:
    print('Battery: ' + str(psutil.sensors_battery()[0]) + '%')
    if psutil.sensors_battery()[2] == False:
        print('State: Not plugged')
    else:
        print('State: Plugged in')
except:
    pass

print('\nProcessor')
print('Number of physical cores: ' + str(psutil.cpu_count(logical=False)))
print('Number of logical cores: ' + str(psutil.cpu_count(logical=True)))
print('CPU Max Frequency: ' + str(psutil.cpu_freq()[2]))
print('CPU Current Frequency: ' + str(psutil.cpu_freq()[0]))
print('CPU Cores Usage: ' + str(psutil.cpu_percent(interval=1, percpu=True)[0]) + '%, ' + str(psutil.cpu_percent(interval=1, percpu=True)[1]) + '%, ' + str(psutil.cpu_percent(interval=1, percpu=True)[2]) + '%, ' + str(psutil.cpu_percent(interval=1, percpu=True)[3]) + '%')

print('\nMemory')
print('Total Memory: ' + str(psutil.virtual_memory()[0]))
print('Used Memory: ' + str(psutil.virtual_memory()[3]))
print('Free Memory: ' + str(psutil.virtual_memory()[1]))
print('Memory Usage: ' + str(psutil.virtual_memory()[2]) + '%')

print('\nDisks And Removable Media')
for i in range(0, len(psutil.disk_partitions(all=True))):
    if psutil.disk_partitions(all=True)[i][3] == 'cdrom':
        continue
    else:
        if psutil.disk_partitions(all=False)[i][0] == 'C:\\':
            print('Primary Disk: ' + psutil.disk_partitions(all=False)[i][0])
        elif 'fixed' in psutil.disk_partitions(all=False)[i][3]:
            print('Secondary Disk: ' + psutil.disk_partitions(all=False)[i][0])
        elif 'removable' in psutil.disk_partitions(all=False)[i][3]:
            print('Removable Disk: ' + psutil.disk_partitions(all=False)[i][0])
        else:
            print('Undefined: ' + psutil.disk_partitions(all=False)[i][0])

        print('File System: ' + psutil.disk_partitions(all=False)[i][2])
        print('Total Disk Space :' + str(shutil.disk_usage(psutil.disk_partitions(all=False)[i][0])[0]))
        print('Used Space: ' + str(shutil.disk_usage(psutil.disk_partitions(all=False)[i][0])[1]))
        print('Free Space: ' + str(shutil.disk_usage(psutil.disk_partitions(all=False)[i][0])[2]))

        if 'fixed' in psutil.disk_partitions(all=False)[i][3]:
            print('Type: Fixed')
        elif 'removable' in psutil.disk_partitions(all=False)[i][3]:
            print('Type: Removable')
        else:
            print('Type: Unknown')

print('\nNetwork Status')
print('IP Address: ' + socket.gethostbyname(socket.gethostname()))
print('Node Name: ' + platform.node())
print('Bytes Sent: ' + str(psutil.net_io_counters(pernic=False)[0]))
print('Bytes Received: ' + str(psutil.net_io_counters(pernic=False)[1]))
print('Packets Sent: ' + str(psutil.net_io_counters(pernic=False)[2]))
print('Packets Received: ' + str(psutil.net_io_counters(pernic=False)[3]))
print('Total number of Errors While Receiving: ' + str(psutil.net_io_counters(pernic=False)[4]))
print('Total number of Errors While Sending: ' + str(psutil.net_io_counters(pernic=False)[5]))
print('Total Number of Incoming Dropped Packets: ' + str(psutil.net_io_counters(pernic=False)[6]))
print('Total Number of Outgoing Dropped Packets: ' + str(psutil.net_io_counters(pernic=False)[7]))

print('\nNetwork Interfaces')
for i in psutil.net_if_addrs():
    print(i + ' Interface')
    if 'Loopback' in psutil.net_if_addrs().get(i)[0][1]:
        print('IP Address: ' + psutil.net_if_addrs().get(i)[0][1])
    else:
        print('Mac Address: ' + psutil.net_if_addrs().get(i)[0][1])
        print('IPv4 Address: ' + psutil.net_if_addrs().get(i)[1][1])

    try:
        print('IPv6 Address: ' + (psutil.net_if_addrs().get(i)[2][1]))
    except:
        pass


def get_processor_info_continually():
    while True:
        time.sleep(3)
        print('CPU Current Frequency: ' + str(psutil.cpu_freq()[0]))
        print('CPU Cores Usage: ' + str(psutil.cpu_percent(interval=0.5, percpu=True)[0]) + '%, ' + str(psutil.cpu_percent(interval=0.5, percpu=True)[1]) + '%, ' + str(psutil.cpu_percent(interval=0.5, percpu=True)[2]) + '%, ' + str(psutil.cpu_percent(interval=0.5, percpu=True)[3]) + '%')


def get_memory_info_continually():
    while True:
        time.sleep(3)
        print('Memory Usage: ' + str(psutil.virtual_memory()[2]) + '%')


def get_network_info_continually():
    while True:
        time.sleep(3)
        print('Bytes Sent: ' + str(psutil.net_io_counters(pernic=False)[0]))
        print('Bytes Received: ' + str(psutil.net_io_counters(pernic=False)[1]))
        print('Packets Sent: ' + str(psutil.net_io_counters(pernic=False)[2]))
        print('Packets Received: ' + str(psutil.net_io_counters(pernic=False)[3]))


def Main():
    Thread(target=get_processor_info_continually).start()
    Thread(target=get_memory_info_continually).start()
    Thread(target=get_network_info_continually).start()

if __name__ == '__main__':
    Main()