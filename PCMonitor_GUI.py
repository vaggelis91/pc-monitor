from PyQt4.QtCore import *
from PyQt4.QtGui import *
import platform
import psutil
import shutil
import sys
import socket
from threading import Thread


class pc_monitor(QTabWidget):
    def __init__(self, parent = None):
        super(pc_monitor, self).__init__(parent)
        self.setGeometry(500, 500, 1000, 600)
        self.setWindowTitle('PC Monitor')

        self.sytem_info_tab = QWidget()
        self.processor_info_tab = QWidget()
        self.memory_info_tab = QWidget()
        self.disks_info_tab = QWidget()
        self.net_status_info_tab = QWidget()
        self.net_inter_info_tab = QWidget()

        self.addTab(self.sytem_info_tab, "Tab 1")
        self.addTab(self.processor_info_tab, "Tab 2")
        self.addTab(self.memory_info_tab, "Tab 3")
        self.addTab(self.disks_info_tab, "Tab 4")
        self.addTab(self.net_status_info_tab, "Tab 5")
        self.addTab(self.net_inter_info_tab, "Tab 6")
        sytem_info_tabUI(self)
        processor_info_tabUI(self)
        memory_info_tabUI(self)
        disks_info_tabUI(self)
        net_status_info_tabUI(self)
        net_inter_info_tabUI(self)


def sytem_info_tabUI(self):
    layout = QFormLayout()
    set_system_info(self, layout)
    self.setTabText(0, "System Information")
    self.sytem_info_tab.setLayout(layout)


def set_system_info(self, layout):
    layout.addWidget(QLabel("Operating system: " + platform.system()))

    user_name = [x[0] for x in psutil.users()]
    layout.addWidget(QLabel("User Name: " + user_name[0]))
    layout.addWidget(QLabel("Computer Name: " + platform.node()))

    if '64' in platform.machine():
        layout.addWidget(QLabel('Architecture: 64bit'))
    else:
        layout.addWidget(QLabel('Architecture: 32bit'))

    layout.addWidget(QLabel("Machine: " + platform.machine()))
    layout.addWidget(QLabel("Processor: " + platform.processor()))


def processor_info_tabUI(self):
    layout = QFormLayout()
    set_processor_info(layout)
    self.setTabText(1, "Processor")
    self.processor_info_tab.setLayout(layout)


def set_processor_info(layout):
    #mythread = Processor_thread()
    #mythread.start()
    layout.addWidget(QLabel('Number of physical cores: ' + str(psutil.cpu_count(logical=False))))
    layout.addWidget(QLabel('Number of logical cores: ' + str(psutil.cpu_count(logical=True))))
    layout.addWidget(QLabel('CPU Max Frequency: ' + str(psutil.cpu_freq()[2])))
    layout.addWidget(QLabel('CPU Current Frequency: ' + str(psutil.cpu_freq()[0])))
    layout.addWidget(QLabel('CPU cores usage: ' + str(psutil.cpu_percent(interval=0.5, percpu=True)[0]) + '%, ' + str(
            psutil.cpu_percent(interval=0.5, percpu=True)[1]) + '%, ' + str(
            psutil.cpu_percent(interval=0.5, percpu=True)[2]) + '%, ' + str(
            psutil.cpu_percent(interval=0.5, percpu=True)[3]) + '%'))


def memory_info_tabUI(self):
    layout = QFormLayout()
    set_memory(layout)
    self.setTabText(2, "Memory")
    self.memory_info_tab.setLayout(layout)


def set_memory(layout):
    layout.addWidget(QLabel('Total memory: ' + str(psutil.virtual_memory()[0])))
    layout.addWidget(QLabel('Used memory: ' + str(psutil.virtual_memory()[3])))
    layout.addWidget(QLabel('Free memory: ' + str(psutil.virtual_memory()[1])))
    layout.addWidget(QLabel('Memory Usage: ' + str(psutil.virtual_memory()[2]) + '%'))


def disks_info_tabUI(self):
    layout = QFormLayout()
    set_disks(layout)
    self.setTabText(3, "Disks And Removable Media")
    self.disks_info_tab.setLayout(layout)


def set_disks(layout):
    for i in range(0,len(psutil.disk_partitions(all=True))):
        if psutil.disk_partitions(all=True)[i][3] == 'cdrom':
            continue
        else:
            if psutil.disk_partitions(all=False)[i][0] == 'C:\\':
                layout.addWidget(QLabel('Primary Disk: ' + psutil.disk_partitions(all=False)[i][0]))
            elif 'fixed' in psutil.disk_partitions(all=False)[i][3]:
                layout.addWidget(QLabel('Secondary Disk: ' + psutil.disk_partitions(all=False)[i][0]))
            elif 'removable' in psutil.disk_partitions(all=False)[i][3]:
                layout.addWidget(QLabel('Removable Disk: ' + psutil.disk_partitions(all=False)[i][0]))
            else:
                layout.addWidget(QLabel('Undefined: ' + psutil.disk_partitions(all=False)[i][0]))

            layout.addWidget(QLabel('File System: ' + psutil.disk_partitions(all=False)[i][2]))
            layout.addWidget(QLabel('Total Disk Space :' + str(shutil.disk_usage(psutil.disk_partitions(all=False)[i][0])[0])))
            layout.addWidget(QLabel("Used Space: " + str(shutil.disk_usage(psutil.disk_partitions(all=False)[i][0])[1])))
            layout.addWidget(QLabel("Free Space:" + str(shutil.disk_usage(psutil.disk_partitions(all=False)[i][0])[2])))

            if 'fixed' in psutil.disk_partitions(all=False)[i][3]:
                layout.addWidget(QLabel('Type: Fixed'))
            elif 'removable' in psutil.disk_partitions(all=False)[i][3]:
                layout.addWidget(QLabel('Type: Removable'))
            else:
                layout.addWidget(QLabel('Type: Unknown'))

        layout.addWidget(QLabel(''))


def net_status_info_tabUI(self):
    layout = QFormLayout()
    set_network_info(layout)
    self.setTabText(4, "Network Status")
    self.net_status_info_tab.setLayout(layout)


def set_network_info(layout):
    layout.addWidget(QLabel('IP Address: ' + socket.gethostbyname(socket.gethostname())))
    layout.addWidget(QLabel('Node Name: ' + platform.node()))
    layout.addWidget(QLabel('Bytes Sent: ' + str(psutil.net_io_counters(pernic=False)[0])))
    layout.addWidget(QLabel('Bytes Received: ' + str(psutil.net_io_counters(pernic=False)[1])))
    layout.addWidget(QLabel('Packets Sent: ' + str(psutil.net_io_counters(pernic=False)[2])))
    layout.addWidget(QLabel('Packets Received: ' + str(psutil.net_io_counters(pernic=False)[3])))
    layout.addWidget(QLabel('Total number of errors While Receiving: ' + str(psutil.net_io_counters(pernic=False)[4])))
    layout.addWidget(QLabel('Total number of errors While Sending: ' + str(psutil.net_io_counters(pernic=False)[5])))
    layout.addWidget(QLabel('Total Number of Incoming Dropped Packets: ' + str(psutil.net_io_counters(pernic=False)[6])))
    layout.addWidget(QLabel('Total Number of Outgoing Dropped Packets: ' + str(psutil.net_io_counters(pernic=False)[7])))


def net_inter_info_tabUI(self):
    layout = QFormLayout()
    set_network_inter(layout)
    self.setTabText(5, "Network Interfaces")
    self.net_inter_info_tab.setLayout(layout)


def set_network_inter(layout):
    for i in psutil.net_if_addrs():
        layout.addWidget(QLabel(i + ' Interface'))
        if 'Loopback' in psutil.net_if_addrs().get(i)[0][1]:
            layout.addWidget(QLabel('IP Address: ' + psutil.net_if_addrs().get(i)[0][1]))
        else:
            layout.addWidget(QLabel('Mac Address: ' + psutil.net_if_addrs().get(i)[0][1]))

        layout.addWidget(QLabel('IPv4 Address: ' + psutil.net_if_addrs().get(i)[1][1]))

        try:
            layout.addWidget(QLabel('IPv6 Address: ' + (psutil.net_if_addrs().get(i)[2][1])))
        except:
            pass
        layout.addWidget(QLabel(''))


'''class Processor_thread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        pass'''

def main():
    app = QApplication(sys.argv)
    gui = pc_monitor()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()