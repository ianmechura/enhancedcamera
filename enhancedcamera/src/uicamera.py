import pygame.camera
import pygame.image
import sys
import copy
import target_controller
import threading

class UI:

    targeting_camera = None

    def __init__(self, tgt_ctrl):
        self.tgt_ctrl = tgt_ctrl;
        pygame.init()
        pygame.camera.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.retical = Retical(self.screen)
        self.ctrl = CompassCtrl(self.screen)
        camera_list = self.list_cameras()
        print(camera_list)
        dimensions = self.get_window_dimensions()
        self.init_camera(camera_list, 1, dimensions)
        self.init_lookfeel()
        pygame.display.set_caption("Live Video Feed")


        #get current frame from camera
        img = self.targeting_camera.get_image()
        WIDTH = img.get_width()
        HEIGHT = img.get_height();

        while True :
            self.draw_loop()

        # ui_thread = threading.Thread(target=self._ui_thread, daemon=True)
        # ui_thread.start()


    def _ui_thread(self):
        while True :
            self.draw_loop()

    def start(self):
        ui_thread = threading.Thread(target=self._ui_thread, daemon=True)
        ui_thread.start()



    def list_cameras(self):
        cameras = pygame.camera.list_cameras()
        print("[ Available Cameras: ]")
        for c in cameras:
            print(c)
        return cameras

    def get_window_dimensions(self):
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        return (width, height)


    def init_camera(self, cameras, cam_index, size):
        self.targeting_camera = pygame.camera.Camera(cameras[1], size)
        self.targeting_camera.start()

    def init_lookfeel(self):
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 32)
    

    def draw_loop(self):

       
        img = self.targeting_camera.get_image()
        self.screen.blit(img, (0,0))
        self.retical.update()
        self.ctrl.update()    
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if self.ctrl.rect_north.collidepoint(x, y):
                    print("CLICK ED NORTH!")
                    self.tgt_ctrl.move_north()
                elif self.ctrl.rect_south.collidepoint(x, y):
                    print("CLICK ED south!")
                    self.tgt_ctrl.move_south()
                elif self.ctrl.rect_east.collidepoint(x, y):
                    print("CLICK ED east!")
                    self.tgt_ctrl.move_east()
                elif self.ctrl.rect_west.collidepoint(x, y):
                    print("CLICK ED west!")
                    self.tgt_ctrl.move_west()
                print(e)                            

        
class Retical:

    rect_retical = None
    img_retical = None


    def __init__(self, screen):
        self.screen = screen        
        self.img_retical = pygame.image.load("../reticals/retical.png")
        self.rect_retical = self.img_retical.get_rect()
        self.rect_retical.top = 100
        self.rect_retical.left = 300

    def update(self):
        self.screen.blit(self.img_retical, self.rect_retical)


class CompassCtrl:

    img_north = None
    img_east = None
    img_south = None
    img_east = None

    def __init__(self, screen):
        self.screen = screen
        compass_ctrl_xpos=(screen.get_width()/5)*4
        compass_ctrl_ypos=20

        self.img_north = pygame.image.load("../sprites/north.png")
        self.img_south = pygame.image.load("../sprites/south.png")
        self.img_east = pygame.image.load("../sprites/east.png")
        self.img_west = pygame.image.load("../sprites/west.png")

        self.rect_north = self.img_north.get_rect()
        self.rect_north.top = compass_ctrl_ypos+50 
        self.rect_north.left = compass_ctrl_xpos+50 

        self.rect_south = self.img_south.get_rect()
        self.rect_south.top = compass_ctrl_ypos+250 
        self.rect_south.left = compass_ctrl_xpos+50

        self.rect_east = self.img_east.get_rect()
        self.rect_east.top = compass_ctrl_ypos+(200-62)
        self.rect_east.left = compass_ctrl_xpos+(62+95)

        self.rect_west = self.img_west.get_rect()
        self.rect_west.top = compass_ctrl_ypos+(200-62)
        self.rect_west.left = compass_ctrl_xpos-45

    def update(self):
        self.screen.blit(self.img_north, self.rect_north)
        self.screen.blit(self.img_south, self.rect_south)
        self.screen.blit(self.img_east, self.rect_east)
        self.screen.blit(self.img_west, self.rect_west)






  

