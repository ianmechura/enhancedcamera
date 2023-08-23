import serial
import queue
import threading
import copy


class Device:
    
    queue_read_from_device = queue.Queue()
    queue_write_to_device = queue.Queue()
    started = False
    subscriptions = [ queue_read_from_device ]
    
    
    __all__ = ['start', 'send', 'subscribe']

    def _init_comport(self):
        try:
            self.serial_con = serial.Serial(port=self.comport, baudrate=self.baudrate, timeout=1)
        except serial.SerialException:

            print("Failed to connect to device on port {comport} please enter a different port".format(comport=self.comport))  
            self.comport = input("Enter port name (COM1):")
            self.baudrate = input("Enter baud rate (9600):")
            self._init_comport()
    
    def __init__(self, comport, baudrate):
        self.comport = comport
        self.baudrate = baudrate
        print("Initializing communication with device on {comport} at {baudrate} baud".format(comport=self.comport, baudrate=self.baudrate))
        self._init_comport()
   

    def start(self):
        if not self.started:
            
            input_thread = threading.Thread(target=self._proc_read_from_device, daemon=True)
            input_thread.start()
            
            output_thread = threading.Thread(target=self._proc_write_to_device, daemon=True)
            output_thread.start()
            
            device_thread = threading.Thread(target=self._device_proc, daemon=True)
            device_thread.start()
            
            self.started = True
        else:
            raise Exception("Attempt to start device that has already been started.")
        

    def _device_proc(self):
        while True:
            recv = self.serial_con.readline()
            self.queue_read_from_device.put(recv)        
            
    def _proc_read_from_device(self):
        while True:
            while not self.queue_read_from_device.empty():
                item = self.queue_read_from_device.get()
                for sub in self.subscriptions:
                    sub.put(copy.copy(item))
            
    def _proc_write_to_device(self):
        while True:
            if not self.queue_write_to_device.empty():
                mesg = self.queue_write_to_device.get()
                serial.write(mesg)
                    
    def subscribe(self, queue):
        self.subscriptions.append(queue)
            
    def send(self, mesg):
        if self.started:
            self.queue_write_to_device.put(mesg)
        else:
            raise Exception("Attempt to write to a device that has not been started.")
            
                
        
        