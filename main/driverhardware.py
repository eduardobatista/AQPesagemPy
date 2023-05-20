import serial
import serial.tools.list_ports

class driverhardware:

    def __init__(self):
        self.serial = serial.Serial(port=None,
                                    baudrate = 19200,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS,
                                    timeout=100,
                                    rtscts=False)
        self.setDevice("dummy")
        
    def setPort(self, portname):
        self.serial.port = portname

    def openPort(self):
        self.serial.open()
    
    def closePort(self):
        self.serial.close()
    
    def listPorts(self):
        ports = serial.tools.list_ports.comports()
        return list(ports)

    def setDevice(self, devicename):
        if devicename not in ["3101C","3102","LD1050","dummy"]:
            raise BaseException(f"Invalid device: {devicename}")
        else:
            self.device = devicename
            if devicename == "dummy":
                self.lepeso = self.lepesodummy
            elif devicename == "3101C":
                self.lepeso = self.lepeso3101C
            if devicename == "3102":
                self.lepeso = self.lepeso3102
            if devicename == "LD1050":
                self.lepeso = self.lepesoLD1050            
    
    def lepesodummy(self):
        return 10.0
    
    def lepeso3102(self):
        return 9.0
    
    def lepeso3101C(self):
        return 8.0
    
    def lepesoLD1050(self):
        return 7.0


        