import time, random, ftd2xx

def init():
 dev = ftd2xx.open(0)
 dev.setTimeouts(5000, 5000)
 dev.setBitMode(0xff, 0x40) # синхронное FIFO
 dev.setUSBParameters(0x10000, 0x10000) # максимальный объем FIFO - 65536 Байт = 64 кБ
 dev.setLatencyTimer(2) 
 dev.setFlowControl(ftd2xx.defines.FLOW_RTS_CTS, 0, 0)
 dev.purge(ftd2xx.defines.PURGE_RX) # очистка буфера
 dev.purge(ftd2xx.defines.PURGE_TX) # очистка буфера
 return dev

tx_data = str(bytearray([ random.randrange(0, 256) for i in range(65536)]))

dev = init()
print("\nDevice Details :")
print("Serial : " , dev.getDeviceInfo()['serial'])
print("Type : " , dev.getDeviceInfo()['type'])
print("ID : " , dev.getDeviceInfo()['id'])
print("Description : " , dev.getDeviceInfo()['description'])
x = 1
while x < 100:
    f = open("example.txt", "wb") 
    f.write(dev.read(x))
    f.close()
    x += 1
dev.close()