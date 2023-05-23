import serial
import serial.tools.list_ports
import re

class driverhardware:

    def __init__(self):
        self.serial = serial.Serial(port=None,
                                    baudrate = 9600,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS,
                                    timeout=1,
                                    rtscts=False)
        self.setDevice("3101C")
        
    def setPort(self, portname):
        self.serial.port = portname

    def openPort(self):
        if not self.serial.isOpen():
            self.serial.open()
        self.serial.reset_output_buffer()
        self.serial.reset_input_buffer()
    
    def closePort(self):
        self.serial.close()
    
    def listPorts(self):
        aux = serial.tools.list_ports.comports()
        ports = [aa.device for aa in aux]
        return list(ports)

    def setDevice(self, devicename):
        if devicename not in ["3101C","3102","LD1050","dummy"]:
            raise BaseException(f"Invalid device: {devicename}")
        else:
            self.device = devicename
            if devicename == "dummy":
                self.lepeso = self.lepesodummy
            elif devicename == "3101C":
                self.requestcmd = bytearray([0,1,ord('P'),0x0D,0x0A])
                self.cpattern = re.compile(r"\:(.*)\:")
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
        self.serial.write(self.requestcmd)
        resp = self.serial.readline().decode()
        # resp = "PB:-02,000 T: 00,000 "
        # resp = "SATURA"
        if len(resp) == 0:
            raise BaseException("Sem resposta do sistema.")
        elif resp.startswith("SAT"):
            raise BaseException("Medida saturada.")
        elif resp.startswith("S<BRE"):
            raise BaseException("Sobrecarga.")
        else:
            aux = self.cpattern.search(resp)[1][:-1].replace(",",".")
            return float(aux)
    
    def lepesoLD1050(self):
        return 7.0


        