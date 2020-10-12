import pygame,random,time,os

black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)

t0=time.time()
green=(0,255,0)
SCREEN_WIDTH=1920
SCREEN_HEIGHT=1080

##background=pygame.image.load("wallpaper2you_194139.jpg").convert()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("western_scalado.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.x=200
        self.rect.y=740
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("western_blue_alreves_scalado.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.x=1600
        self.rect.y=740
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bala_scalada.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.x+=7
class Laser2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bala_alreves_scalada.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.x-=7
class Game(object):
    def __init__(self):
        self.game_over=False
        self.score=0
        self.redteam=False
        self.contador_red=0
        self.contador_blue=0
        self.blueteam=False
        ##self.start=340
        
        self.tiempo=False
        self.laser_list=pygame.sprite.Group()
        self.all_sprite_list= pygame.sprite.Group()
        self.laser2_list=pygame.sprite.Group()

        self.player=Player()
        self.player2=Player2()
        self.all_sprite_list.add(self.player, self.player2)

        self.sound=pygame.mixer.Sound("shotgun.wav")
        


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type==pygame.MOUSEBUTTONDOWN:
                laser= Laser()
                laser.rect.x=self.player.rect.x+60
                laser.rect.y=self.player.rect.y+48
                self.all_sprite_list.add(laser)
                self.laser_list.add(laser)
                self.sound.play()
                
                
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:    
                    laser2=Laser2()
                    laser2.rect.x=self.player2.rect.x-20
                    laser2.rect.y=self.player2.rect.y+48
                    self.all_sprite_list.add(laser2)
                    self.laser2_list.add(laser2)
                    self.sound.play()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    if self.game_over:
                        self.__init__()
            
            
            
        return False
    def run_logic(self):
        if not self.game_over:
            
            ##self.start-=1
            ##print(self.start)
            ##if self.start<=0:
                ##self.tiempo=True
                ##self.game_over=True
            self.all_sprite_list.update()
            laser_hit_list=pygame.sprite.spritecollide(self.player, self.laser2_list,True)
            laser2_hit_list=pygame.sprite.spritecollide(self.player2, self.laser_list,True)

            for laser in self.laser_list:
                if laser.rect.x<-10:
                    self.all_sprite_list.remove(laser)
                    self.laser_list.remove(laser)
            for laser2 in self.laser2_list:
                if laser2.rect.x>1920:
                    self.all_sprite_list.remove(laser2)
                    self.laser2_list.remove(laser2)
            for laser in laser_hit_list:
                self.redteam=True
                self.contador_red+=1
                self.game_over=True
            for laser2 in laser2_hit_list:
                self.blueteam=True
                self.contador_blue+=1
                self.game_over=True
    def display_frame(self, screen):
        screen.fill(white)
        background= pygame.image.load("wallpaper2you_194139.jpg").convert()
        screen.blit(background, [0,0])
        fuente=pygame.font.SysFont("Arial", 34, True, False)
        ##info=fuente.render("Haga click",0,(255,255,255))
        ##screen.blit(info,(5,5))
        
        if self.game_over:
            font = pygame.font.SysFont("arial", 25)
            if self.redteam==True:
                text=font.render("The blue win, Press R to Repeat", True, black)
                center_x=(SCREEN_WIDTH//2)-(text.get_width()//2)
                center_y=(SCREEN_HEIGHT//2)-(text.get_height()//2)
                screen.blit(text,[center_x,center_y])
            if self.blueteam==True:
                text=font.render("The red win, Press R to Repeat",True, black)
                center_x=(SCREEN_WIDTH//2)-(text.get_width()//2)
                center_y=(SCREEN_HEIGHT//2)-(text.get_height()//2)
                screen.blit(text,[center_x,center_y])
                

            #text=font.render((str(self.contador_blue)+"vs"+str(self.contador_red)), True, black)
            #center_x=(SCREEN_WIDTH//2)-(text.get_width()//2)
            #center_y=(SCREEN_HEIGHT//3)-(text.get_height()//2)
            #screen.blit(text,[center_x,center_y])

        if not self.game_over:
            self.all_sprite_list.draw(screen)

        pygame.display.flip()

def main():
    pygame.init()

    screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    
    done=False
    clock=pygame.time.Clock()
    
    game=Game()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(120)
    pygame.quit()

if __name__ =="__main__":
    main()


