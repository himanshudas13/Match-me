import pygame
import random
from turtle import width
from pygame import mixer


pygame.init()

                                                                         #game colours and features
WIDTH= 1200
HEIGHT=770
white= (255, 255,255)
black= (0,0,0)
blue=(77, 0, 77)
grey = (128,128,128)
red  = (240, 7, 46)
green = (0, 255, 0)
fps =90
timer =pygame.time.Clock()
rows=6
cols=6
correct = [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]
options_list=[]
new_board =True
spaces=[]
used=[]
first_guess = False
second_guess = False
first_guess_num =0
second_guess_num=0
once=0
score = 0
matches =0
best_score =0
game_over=False
secs=1
mins=3
best_secs=00
best_mins=00
count=0
value=0
sound=0
#x=235+(8-cols)*45
#y=120+(6-rows)*45
                                                                                #main window creation
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("-MATCH-ME-")
P="icon.jpg"
ICON=pygame.image.load(P)
pygame.display.set_icon(ICON)
title_font = pygame.font.Font("abcd.ttf" , 75,)
menu_font = pygame.font.Font("bcde.ttf", 60,)
main_font = pygame.font.Font("lmn.ttf", 85,)
small_font = pygame.font.Font("rbt.ttf" , 26,)
win_font=pygame.font.Font("rbt.ttf" , 56,)
rules_font = pygame.font.Font("rbt.ttf" , 20,)

def create_window():
    
  top_menu = pygame.draw.rect(screen,black,[0,0, WIDTH ,HEIGHT/7.7])
  title_text = title_font.render('-MATCH-ME-', True,red)
  screen.blit(title_text,(400,20))
  
  bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT - HEIGHT/8.55,WIDTH,HEIGHT/7.7])
  restart_button = pygame.draw.rect(screen, red,[54,HEIGHT-120,50,50],7,7)
  
  img=pygame.image.load("restart.jpg")
  img=pygame.transform.scale(img,(40,40))
  img_rect=img.get_rect(topleft=(60,HEIGHT-115))
  screen.blit(img,(img_rect))
  restart_text= small_font.render('Restart', True ,white)
  screen.blit(restart_text,(35,HEIGHT-65))
  
  score_text= small_font.render(f'Current Score: {score}', True ,white)
  screen.blit(score_text,(20,235))
  best_text= small_font.render(f'Best score: {best_score}', True ,white)
  screen.blit(best_text,(WIDTH-190,235))
  
  fonx=pygame.font.Font("rbt.ttf",26)
  texl=fonx.render("Fastest: {}:{}".format(best_mins,best_secs),True,(255,255,255),(0,0,0))
  texl_rect=texl.get_rect()
  screen.blit(texl,(WIDTH-190,270))
  
  return restart_button 



def create_list_img(rows,cols,imagefile):                                                        #creating a list having all game images
    global options_list
    global spaces
    global used
    f= open(imagefile, "r")
    for item in range(rows*cols //2):
        q=f.readline()
        q.strip()
        q=q.rstrip('\n')
        options_list.append(q)
        item+=1
        final=0

    for item in range( rows*cols):                                           #randomly allocating images to slots on screen
        piece=options_list[random.randint(0, len(options_list)-1)]
        
        spaces.append(piece)
        if piece not in used:
            used.append(piece)
        else:
            used.remove(piece)    
            options_list.remove(piece)
    f.close()
def draw_board(rows,cols):                                                            #displaying slots with images
    # global rows
    # global cols
    global correct
    board_list =[]
    #global x 
    #global y
    x=240+(8-cols)*45
    y=110+(6-rows)*45
    for c in range(cols):
        for r in range(rows):
            
                piece = pygame.draw.rect(screen, white,[c*97+x,r*97+y,75,75],7,7)
                board_list.append(piece)
                img=pygame.image.load("imgc.jpg")
                img=pygame.transform.scale(img,(55,55))
                img_rect=img.get_rect(topleft=((c)*97+x+10,(r)*97+y+10))
                screen.blit(img,(img_rect))
            
                if correct[r][c]==1:

                 piece = pygame.draw.rect(screen, green,[c*97+x,r*97+y,80,80],10,10)
                 img_text =spaces[c*rows+r]
                 img=pygame.image.load(img_text)
                 img=pygame.transform.scale(img,(56,56))
                 img_rect=img.get_rect(topleft=(c*97+x+13,r*97+y+12))
                 screen.blit(img,(img_rect))
                
                 img_text =spaces[c*rows+r]
                 img=pygame.image.load(img_text)
                 img=pygame.transform.scale(img,(56,56))
                 img_rect=img.get_rect(topleft=(c*97+x+13,r*97+y+12))
                 screen.blit(img,(img_rect))
 
               
          
            
     
            
    
     
    return board_list

def check_guesses(first,second):                               #to check if first and second guesses are equal
    global spaces
    global correct
    global score
    global matches
    if spaces[first]== spaces[second]:
        col1 = first // rows
        col2 = second // rows
        row1 =  first - (first // rows*rows)
        row2 = second - (second // rows*rows)
        if correct[row1][col1]==0 and correct[row2][col2]==0:
            correct[row1][col1]=1
            correct[row2][col2]=1
            match_sound=mixer.Sound("match.wav")
            match_sound.play()
            score += 1
            matches +=1
            #print(correct) 
    else:
        score+=1 

def quit_game():
    quit_button = pygame.draw.rect(screen, red,[1080,HEIGHT-120,50,50],7,7)
    img=pygame.image.load("quit.jpg")
    img=pygame.transform.scale(img,(40,40))
    img_rect=img.get_rect(topleft=(1085,HEIGHT-115))
    screen.blit(img,(img_rect))
    quit_text= small_font.render('Quit', True ,white)
    screen.blit(quit_text,(1078,HEIGHT-65))
    return quit_button 

def display_board(rows,cols,t,img):
    x=240+(8-cols)*45
    y=110+(6-rows)*45
    #screen.fill("white")
    img=pygame.image.load(img)
    img=pygame.transform.scale(img,(WIDTH,HEIGHT))
    img_rect=img.get_rect(topleft=(0,0))
    screen.blit(img,(img_rect))
    
    top_menu = pygame.draw.rect(screen,black,[0,0, WIDTH,HEIGHT/7.7])
    title_text = title_font.render('-MATCH-ME-', True,red)
    screen.blit(title_text,(400,20))
  
    bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT - HEIGHT/8.55,WIDTH,HEIGHT/7.7])
    restart_button = pygame.draw.rect(screen, red,[54,HEIGHT-120,50,50],7,7)
  
    img=pygame.image.load("restart.jpg")
    img=pygame.transform.scale(img,(40,40))
    img_rect=img.get_rect(topleft=(60,HEIGHT-115))
    screen.blit(img,(img_rect))
    restart_text= small_font.render('Restart', True ,white)
    screen.blit(restart_text,(35,HEIGHT-65))
  
    score_text= small_font.render(f'Current Score: {score}', True ,white)
    screen.blit(score_text,(20,235))
    best_text= small_font.render(f'Best score: {best_score}', True ,white)
    screen.blit(best_text,(WIDTH-190,235))
  
    fonx=pygame.font.Font("rbt.ttf",26)
    texl=fonx.render("Fastest: {}:{}".format(best_mins,best_secs),True,(255,255,255),(0,0,0))
    texl_rect=texl.get_rect()
    screen.blit(texl,(WIDTH-190,270))
  
    
    text=fonx.render("Timer: {}:{}".format(mins,secs),True,(255,255,255),(0,0,0))
    text_rect=text.get_rect()
    screen.blit(text,(20,270))
    quit_game()
    
    
    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(screen, white,[i*97+x,j*97+y,75,75],7,7)
            img_text =spaces[i*rows+j]
            img=pygame.image.load(img_text)
            img=pygame.transform.scale(img,(55,55))
            img_rect=img.get_rect(topleft=(i*97+x+10,j*97+y+10))
            screen.blit(img,(img_rect))
    pygame.display.update()       
    pygame.time.delay(t)

def draw_menu():
    
    global value
    global running
    img=pygame.image.load("main.jpg")
    img=pygame.transform.scale(img,(WIDTH,HEIGHT))
    img_rect=img.get_rect(topleft=(0,150))
    screen.blit(img,(img_rect))
    #value+=1
   
    top_menu = pygame.draw.rect(screen,black,[0,0, WIDTH,150])
    main_text = main_font.render('-MATCH-ME-', True,(50, 157, 168))
    screen.blit(main_text,(320,20))
    
    play= pygame.draw.rect(screen,(26, 209, 13),[440,250, WIDTH//4,80,],0,5)
    play_text=menu_font.render("PLAY",True,black)
    screen.blit(play_text,(525,270))
    
    options= pygame.draw.rect(screen,(26, 209, 13),[440,350, WIDTH//4,80],0,5)
    options_text=menu_font.render("OPTIONS",True,black)
    screen.blit(options_text,(485,365))
    
    rules= pygame.draw.rect(screen,(26, 209, 13),[440,450, WIDTH//4,80],0,5)
    rules_text=menu_font.render("RULES",True,black)
    screen.blit(rules_text,(507,465))
    
    about= pygame.draw.rect(screen,(26, 209, 13),[440,550, WIDTH//4,80],0,5)
    about_text=menu_font.render("ABOUT",True,black)
    screen.blit(about_text,(495,565))
    
    exit= pygame.draw.rect(screen,(26, 209, 13),[440,650, WIDTH//4,80],0,5)
    exit_text=menu_font.render("EXIT",True,black)
    screen.blit(exit_text,(525,665))
    for event in pygame.event.get():                                            #exit strategy
        if event.type==pygame.QUIT:
          running=False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
          if play.collidepoint(event.pos):
              restart_game()
              value=1
          if options.collidepoint(event.pos):  
              value=2 
          if rules.collidepoint(event.pos):  
              value=3 
          if about.collidepoint(event.pos):  
              value=4 
          if exit.collidepoint(event.pos):  
              value=5 
    pygame.display.update()
   # pygame.time.delay(1550)

def go_back():
    global value
    global running
   
    img=pygame.image.load("main.jpg")
    img=pygame.transform.scale(img,(WIDTH,HEIGHT))
    img_rect=img.get_rect(topleft=(0,0))
    screen.blit(img,(img_rect))
    back= pygame.draw.rect(screen,(26, 209, 13),[10,10, 40,40,],0,5)
    img=pygame.image.load("back.png")
    img=pygame.transform.scale(img,(30,30))
    img_rect=img.get_rect(topleft=(15,15))
    screen.blit(img,(img_rect))
    for event in pygame.event.get():                                            #exit strategy
        if event.type==pygame.QUIT:
          running=False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
          if back.collidepoint(event.pos):
              value=0
              

def about():
    authors= pygame.draw.rect(screen,black,[50,200, WIDTH-100,HEIGHT-400,],7,5)
    f=open("abc.txt","r")
    i=0
    for x in  f:
     i+=1
     text=f.readline()
   
     authors_text=rules_font.render(text,True,white)
     screen.blit(authors_text,(50,186+i*40))
     
    f.close()   
    pygame.display.update()
def instructions():
    instructions= pygame.draw.rect(screen,black,[50,200, WIDTH-100,HEIGHT-400,],7,5)
    f=open("bcd.txt","r")
    i=0
    for x in  f:
     i+=1
     text=f.readline()
   
     instructions_text=rules_font.render(text,True,white)
     screen.blit(instructions_text,(55,186+i*40))
     
    f.close()
     
    pygame.display.update()
def difficulty():
    global value
    global running
    easy= pygame.draw.rect(screen,(black),[440,250, WIDTH//4,80,],0,5)
    easy_text=menu_font.render("EASY",True,white)
    screen.blit(easy_text,(515,270))
    
    medium= pygame.draw.rect(screen,(178,28,17),[440,350, WIDTH//4,80],0,5)
    medium_text=menu_font.render("MEDIUM",True,black)
    screen.blit(medium_text,(485,365))
    
    difficult= pygame.draw.rect(screen,(8, 55, 156),[440,450, WIDTH//4,80],0,5)
    difficult_text=menu_font.render("DIFFICULT",True,(227, 16, 19))
    screen.blit(difficult_text,(460,460))
    
    for event in pygame.event.get():                                           
        if event.type==pygame.QUIT:
          running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
          if easy.collidepoint(event.pos):
              restart_game()
              value=6
          if medium.collidepoint(event.pos): 
              restart_game() 
              value=1 
          if difficult.collidepoint(event.pos):  
              restart_game()
              value=7
              
          
    pygame.display.update()
    
def restart_game():
                    global secs
                    global mins
                    global count
                    global options_list
                    global used
                    global spaces
                    global new_board
                    global score
                    global matches
                    global first_guess
                    global second_geuss 
                    global correct
                    global game_over 
                    global sound
                    global final
                    secs=0
                    mins=0
                    count=0
                    options_list=[]
                    used =[]
                    spaces =[]
                    new_board = True
                    score=0
                    matches= 0
                    first_guess= False
                    second_geuss = False
                    correct = [[0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0]]
                    game_over = False
                    sound=0
                    final=0
def play_sound(back_music):
    global sound
    if sound==0 :
     mixer.music.load(back_music)
     mixer.music.play(-1)
     sound=1
    if sound==2:
    #   mixer.music.load("bgm.wav")
    #   mixer..play(-1)
      sound==0


# main function
m="bgm.wav"
mixer.music.load(m)
mixer.music.play(-1)

   
running = True                                                                 


while running:
    
 timer.tick(fps)
    #screen.fill(white)
 
 if value==0:
     screen.fill(white)
     draw_menu()
     
 elif value==5:
     running=False
     
 elif value==4:
     about()
     go_back()
     
 elif value==3:
     instructions() 
     go_back() 
     
 elif value==2:
    difficulty() 
    go_back()
    
    
 else:
    
    if value==1:
        rows=6
        cols=6
        imagefile="images.txt"
        back_img="img01.jpg"
        back_sound="strangerthings.wav"
        display_time=700
        time=3
    elif value==6:
        rows=6
        cols=5
        imagefile="imagesgot.txt"
        back_img="img02.jpg"
        back_sound="Game of Thrones.wav"
        display_time=600
        time=2
    elif value==7:
        rows=6
        cols=8
        imagefile="imagesmar.txt"
        back_img="img03.jpg"
        back_sound="marvel.wav"
        display_time=1000
        time=5
    
    
    img=pygame.image.load(back_img)
    img=pygame.transform.scale(img,(WIDTH,HEIGHT))
    img_rect=img.get_rect(topleft=(0,0))
    screen.blit(img,(img_rect))
    if not count:
     board=draw_board(rows,cols)
     play_sound(back_sound)
     
    if new_board:
        create_list_img(rows,cols,imagefile)
        display_board(rows,cols,display_time,back_img)
        new_board =False
        

    restart=create_window()
    close=quit_game()
   
    if count:
       
       winner = pygame.draw.rect(screen,black,[0,HEIGHT-HEIGHT/1.54,WIDTH,150],0,4)
       winner_text = title_font.render(f"TIME'S UP- YOU LOSE !!", True,red)
       screen.blit(winner_text,(200,HEIGHT-HEIGHT/1.71))
       sound=2
       pygame.display.update()
       
    
    if not count:
    
     clock=pygame.time.Clock()
     clock.tick(1)
     if secs==60:
        secs=0
        mins+=1
     secs+=1
     
     
     if mins==time:
       LOSE_sound=mixer.Sound("loser.wav")
       LOSE_sound.play()
       
       secs=0
       mins=0
       count+=1
       game_over=True
       pygame.display.update()
        
        
        
     font=pygame.font.Font("rbt.ttf",26)
     text=font.render("Timer: {}:{}".format(time-1-mins,60-secs),True,(255,255,255),(0,0,0))
     text_rect=text.get_rect()
     screen.blit(text,(20,270))
     
    
    

    if first_guess and second_guess:
     
     check_guesses(first_guess_num,second_guess_num)
     pygame.time.delay(70)
     first_guess=False 
     second_guess=False

    for event in pygame.event.get():                                            #exit strategy
        if event.type==pygame.QUIT:
          running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
                
                for i in range(len(board)):
                 button = board[i]
                 if not game_over:
                    if button.collidepoint(event.pos) and not first_guess:
                            first_guess=True
                            first_guess_num =i
                            click_sound=mixer.Sound("turn.wav")
                            click_sound.play()
                            #print(i)
                    elif button.collidepoint(event.pos) and not second_guess  and i !=first_guess_num:
                            second_guess=True
                            second_guess_num =i
                            click_sound=mixer.Sound("turn.wav")
                            click_sound.play()
                            #print(i)    
                if restart.collidepoint(event.pos):
                    restart_button = pygame.draw.rect(screen, red,[59,HEIGHT-116,45,45],7,7)
                    img=pygame.image.load("restart.jpg")
                    img=pygame.transform.scale(img,(30,30))
                    img_rect=img.get_rect(topleft=(65,HEIGHT-110))
                    screen.blit(img,(img_rect))
                    restart_text= small_font.render('Restart', True ,white)
                    screen.blit(restart_text,(35,HEIGHT-65))
                    pygame.display.update()       
                    pygame.time.delay(100)
                    restart_game() 
              
                    
                if close.collidepoint(event.pos):
                 quit_button = pygame.draw.rect(screen, red,[1083,HEIGHT-118,45,45],7,7)
                 img=pygame.image.load("quit.jpg")
                 img=pygame.transform.scale(img,(30,30))
                 img_rect=img.get_rect(topleft=(1089,HEIGHT-111))
                 screen.blit(img,(img_rect))
                 quit_text= small_font.render('Quit', True ,white)   
                 screen.blit(quit_text,(35,HEIGHT-65))  
                 pygame.display.update()       
                #  pygame.time.delay(20)
                 restart_game()    
                 #event.type==pygame.QUIT
                 value=0
                 final=0
                 mixer.music.load("bgm.wav")
                 mixer.music.play(-1) 
      
    # rows=5
    # cols=6         
    x=240+(8-cols)*45
    y=110+(6-rows)*45
    if not game_over:            
     if first_guess:
        # location = ((first_guess_num // rows)*97+x, (first_guess_num- (first_guess_num//rows*rows))*97+y)
        piece = pygame.draw.rect(screen, red,[(first_guess_num //rows)*97+x-7,(first_guess_num- (first_guess_num//rows*rows))*97+y-7,98,98],9,9)
        img_text =spaces[first_guess_num]
        img=pygame.image.load(img_text)
        img=pygame.transform.scale(img,(83,83))
        img_rect=img.get_rect(topleft=((first_guess_num //rows)*97+x,(first_guess_num- (first_guess_num//rows*rows))*97+y))
        # pygame.display.update() 
        screen.blit(img,(img_rect))
    
    
    if second_guess:
        #location = ((second_guess_num // rows)*97+x, (second_guess_num- (second_guess_num//rows*rows))*97+y)
        piece = pygame.draw.rect(screen, red,[(second_guess_num //rows)*97+x-7,(second_guess_num- (second_guess_num//rows*rows))*97+y-7,95,95],8,8)    
        img_text =spaces[second_guess_num]
        img=pygame.image.load(img_text)
        img=pygame.transform.scale(img,(83,83))
        img_rect=img.get_rect(topleft=((second_guess_num //rows)*97+x,(second_guess_num- (second_guess_num//rows*rows))*97+y))
        screen.blit(img,(img_rect))
        
   
   
    if matches == rows*cols//2:
         game_over= True
         winner = pygame.draw.rect(screen,black,[0,HEIGHT-500,WIDTH,150],0,4)
         if final==0:
          minsx=mins
          secsx=secs
          win_sound=mixer.Sound("winner.wav")
          win_sound.play()
          final=1
         winner_text = win_font.render(f'YOU WON IN {score} MOVES IN {minsx}MINS {secsx}SECS !', True,red)
         screen.blit(winner_text,(5,HEIGHT-450))
         
         if best_score > score  or best_score ==0:
             best_score=score   
         if best_mins>mins or (best_mins==0 and best_secs==0):
             best_mins=mins
             best_secs=secs
         elif best_mins>mins or best_mins==0:
             if best_secs>secs:
                 best_secs=secs
    pygame.display.flip()
pygame.quit()

     
