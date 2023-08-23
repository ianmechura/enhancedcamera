import pygame.camera
import pygame.image
import sys
import copy

pygame.init()

# display_settings = pygame.display.Info()

#create camera stuff
#SIZE = (1200, 600)
# SIZE = (display_settings.current_w, display_settings.current_y)

pygame.camera.init()
# screen = pygame.display.set_mode(( 1200, 600 ))
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

cameras = pygame.camera.list_cameras()

print("[ Available Cameras: ]")
for c in cameras:
    print(c)

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
window_size = (width, height)

webcam = pygame.camera.Camera(cameras[1], window_size)
webcam.start()


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)


def write_text(mesg, surface, r):
    text = font.render(mesg, True, green, blue)
    textRect = text.get_rect()
    textRect.left = r.left
    textRect.top = r.top
    surface.blit(text, r)

def display_coords(label, r, surface, offset):
    r2 = copy.deepcopy(r)

    if (offset != 0):
        r2.left += offset
        r2.top += offset

    txt = "{LAB}={XX},Y={YY}"
    write_text(txt.format(LAB=label, XX=r.left, YY=r.top), surface, r2)



#get current frame from camera
img = webcam.get_image()
WIDTH = img.get_width()
HEIGHT = img.get_height();


#prepare graphics


img_retical = pygame.image.load("./reticals/retical.png")
rect_retical = img_retical.get_rect()
rect_retical.top = 100
rect_retical.left = 300

x=200
msg = "Screen Width: {wid}".format(wid=screen.get_width())
print(msg)

x= (screen.get_width()/5)*4
y=20

img_north = pygame.image.load("./sprites/north.png")
img_south = pygame.image.load("./sprites/south.png")
img_east = pygame.image.load("./sprites/east.png")
img_west = pygame.image.load("./sprites/west.png")

rect_north = img_north.get_rect()
rect_north.top = y+50 
rect_north.left = x+50 

rect_south = img_south.get_rect()
rect_south.top = y+250 
rect_south.left = x+50

rect_east = img_east.get_rect()
rect_east.top = y+(200-62)
rect_east.left = x+(62+95)


rect_west = img_west.get_rect()
rect_west.top = y+(200-62)
rect_west.left = x-45

pygame.display.set_caption("Live Video Feed")
    

while True :

    screen.blit(img, (0,0))
    screen.blit(img_retical, rect_retical)
    screen.blit(img_north, rect_north)
    screen.blit(img_south, rect_south)
    screen.blit(img_east, rect_east)
    screen.blit(img_west, rect_west)
    
    pygame.display.flip()
    img = webcam.get_image()
    
#Handle UI events

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            if rect_north.collidepoint(x, y):
                print("CLICK ED NORTH!")
            elif rect_south.collidepoint(x, y):
                print("CLICK ED south!")
            elif rect_east.collidepoint(x, y):
                print("CLICK ED east!")
            elif rect_west.collidepoint(x, y):
                print("CLICK ED west!")

            print(e)

                            
