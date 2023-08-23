import pygame.camera
import pygame.image
import sys
from queues import Queue


def main():
    bus = MessageEventBus()
    visual = VisualSystem()
    motive = MotiveSystem()
    target = TargetingSystem()
    fire_ctrl = FireControlSystem()

    bus.register(visual)
    bus.register(motive)
    bus.register(target)
    bus.register(fire_ctrl)

    monitor = SystemMonitor()
    monitor.register(visual)
    monitor.register(target)

class Subsystem(object):
    
    def __init__(self, bus):
        bus.register(self, self.onEvent)

    
class MessageEventBus:
    
    queueRegistry = {}
    subscriptions = {}

    def register(subsystem, callback):
        self.queueRegistry[subsystem.id] = Queue()

    def notify(subsystemId, message):
        queueRegistry[subsystemId].enqueue(message)

    def subscribe(subscriber, subscription):
        subscriptions[subscriber] = subscription




class SystemMonitor:
    desc = "Monitors subsystems and reports issues"

    def register(self, subsystem):
        print(subsystem)

class VisualSystem(Subsystem):
    #perhaps auditory would be better maybe feedback
    desc = "Video Feed"

    def __init__(self, bus):

        super.__init__(self, bus)
        SIZE = (1200, 600)

        pygame.camera.init()
        screen = pygame.display.set_mode(( 1200, 600 ))
        cameras = pygame.camera.list_cameras()
        webcam = pygame.camera.Camera(cameras[0], SIZE)
        webcam.start()

    def onEvent(event):
        print(event)



class MotiveSystem:
    desc = "Vehicular motion control"

class TargetingSystem:
    desc = "Control Stepper Motors to aim at targets"

class FireControlSystem:
    desc = "Actuate physical triggering mechanisms"


