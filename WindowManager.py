import pygame
import random
import time
startup=0
#mysz i tlo
myszx = 10
myszy = 10
klik = 0
tlor = 0
tlog = 0
tlob = 0
bcolor = 0
tempcolor = str("")
#odpalanie
plikilan = 0
ponglan = 0
settingslan = 0
writelan = 0
clocklan = 0
#zegar
zegx = 100
zegy = 100
#pong
pongx = 100
pongy = 100
ballx = pongx+10
bally = pongy+10
ballmx = 1
ballmy = 1
#write
tekst = str(" ")
tekstx = 100
teksty = 100
#settings
setx = 100
sety = 100
tsetx = 100
tsety=100
setr = 0
setg = 0
setb = 0
tsetr = 0
tsetg = 0
tsetb = 0

pygame.init()
win = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Window Manager")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #tlo
    if bcolor==0:
        tlor = 0
        tlog = 0
        tlob = 0
        given_file = open('bcgr.data', 'r')

        lines = given_file.readlines()

        for line in lines:
            for c in line:
                if c.isdigit() == True:
                    tempcolor=tempcolor+c
        tlor=int(tempcolor)
        given_file.close()
        tempcolor = str("")
        given_file = open('bcgg.data', 'r')

        lines = given_file.readlines()

        for line in lines:
            for c in line:
                if c.isdigit() == True:
                    tempcolor=tempcolor+c
        tlog=int(tempcolor)
        given_file.close()
        tempcolor = str("")
        given_file = open('bcgb.data', 'r')

        lines = given_file.readlines()

        for line in lines:
            for c in line:
                if c.isdigit() == True:
                    tempcolor=tempcolor+c
        tlob=int(tempcolor)
        given_file.close()
        tempcolor = str("")
        setr = tlor
        setg = tlog
        setb = tlob
        bcolor=1


    
    while startup==0:
        btlogo = pygame.image.load('BTlogo.png')
        win.blit(btlogo, (0,0))
        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(3000)
        startup=1
    keys = pygame.key.get_pressed()
    #ikony i mysz
    if keys[pygame.K_LEFT] and myszx>=0:
        myszx -= 1
    if keys[pygame.K_RIGHT] and myszx<=800:
        myszx += 1
    if keys[pygame.K_UP] and myszy>=0:
        myszy -= 1
    if keys[pygame.K_DOWN] and myszy<=480:
        myszy += 1
    if keys[pygame.K_z] :
        klik = 1
    else:
        klik = 0
    win.fill((tlor, tlog, tlob))
    plikii = pygame.image.load('Pliki.png')
    pongi = pygame.image.load('Pong.png')
    settingsi = pygame.image.load('Settings.png')
    writei = pygame.image.load('Writer.png')
    clocki = pygame.image.load('Clock.png')
    winbtns = pygame.image.load('WinBtns.png')
    sysendi = pygame.image.load('End.png')
    font = pygame.font.SysFont('comicsans', 30)
    pliki = pygame.draw.rect(win, (0, 200, 0), (10, 10,50,50))
    win.blit(plikii, (10,10))
    pong = pygame.draw.rect(win, (0, 200, 200), (10, 10+60,50,50))
    win.blit(pongi, (10,10+60))
    settings = pygame.draw.rect(win, (200, 200, 200), (10, 10+60+60,50,50))
    win.blit(settingsi, (10,10+120))
    write = pygame.draw.rect(win, (200, 200, 0), (10, 70+60+60,50,50))
    win.blit(writei, (10,10+120+60))
    clock = pygame.draw.rect(win, (200, 200, 200), (10, 70+120+60,50,50))
    win.blit(clocki, (10,10+120+120))
    sysend = pygame.draw.rect(win, (200, 200, 200), (10, 70+60+120+60,50,50))
    win.blit(sysendi, (10,10+60+120+120))
    #programy
    #write
    if writelan == 1:
        pygame.draw.rect(win, (255,255,255) , (zegx, zegy, 150, 100), 0)
        pygame.draw.rect(win, (0,0,0) , (zegx, zegy, 150, 100), 2)

    #pong
    if ponglan == 1:
        pygame.draw.rect(win, (255,255,255) , (pongx, pongy, 300, 200), 0)
        pygame.draw.rect(win, (0,0,0) , (pongx, pongy, 300, 200), 2)
        pygame.draw.circle(win, (0, 128, 0), (ballx, bally), 4)

        pongend = pygame.draw.rect(win, (200, 0, 0), (pongx, pongy-30,30,30))
        pongmove = pygame.draw.rect(win, (200, 0, 200), (pongx+30, pongy-30,30,30))
        if mysz.colliderect(pongmove) ==0:
            ballx = ballx+ballmx
            bally = bally+ballmy
        else:
            pongpause= font.render("Wstrzymano", 6, (255, 0,0))
            win.blit(pongpause, (pongx+100, pongy+100))
        win.blit(winbtns, (pongx, pongy-30))
        if ballx >= pongx+300:
            ballmx = random.randint(1,3)
            ballmx = ballmx*-1
        if ballx <= pongx:
            ballmx = random.randint(1, 3)
        if bally >= pongy+200:
            ballmy = random.randint(1, 3)
            ballmy = ballmy*-1
        if bally <= pongy:
            ballmy = random.randint(1, 3)
        if mysz.colliderect(pongend) and klik == 1:
            ponglan = 0
        if mysz.colliderect(pongmove) and klik == 1:
            pongx = myszx-45
            pongy=myszy+20
        if keys[pygame.K_LEFT] and mysz.colliderect(pongmove) and klik == 1:
            ballx = ballx-1
        if keys[pygame.K_RIGHT] and mysz.colliderect(pongmove) and klik == 1:
            ballx =ballx+1
        if keys[pygame.K_UP] and mysz.colliderect(pongmove) and klik == 1:
            bally -= 1
        if keys[pygame.K_DOWN] and mysz.colliderect(pongmove) and klik == 1:
            bally=bally+1

    #zegar
    if clocklan == 1:
        pygame.draw.rect(win, (255,255,255) , (zegx, zegy, 150, 100), 0)
        pygame.draw.rect(win, (0,0,0) , (zegx, zegy, 150, 100), 2)
        obecnyczas = time.localtime()
        currenttime = time.strftime("%H:%M:%S", obecnyczas)
        czasomierz = font.render(currenttime, 3, (0, 0, 0))
        win.blit(czasomierz, (zegx+50, zegy+50))
        clockend = pygame.draw.rect(win, (200, 0, 0), (zegx, zegy,30,30))
        clockmove = pygame.draw.rect(win, (200, 0, 200), (zegx+30, zegy,30,30))
        win.blit(winbtns, (zegx, zegy))
        zegartitle= font.render("Zegar", 3, (50, 100, 200))
        win.blit(zegartitle, (zegx+70, zegy+7))
        if mysz.colliderect(clockend) and klik == 1:
            clocklan = 0
        if mysz.colliderect(clockmove) and klik == 1:
            zegx = myszx
            zegx=zegx-45
            zegy = myszy
            zegy=zegy-15

    #settings
    if settingslan == 1:
        pygame.draw.rect(win, (255,255,255) , (setx, sety, 300, 150), 0)
        pygame.draw.rect(win, (0,0,0) , (setx, sety, 300, 150), 2)
        pygame.draw.rect(win, (setr,setg,setb) , (setx+285, sety+10, 10, 130), 0)
        pygame.draw.rect(win, (0,0,0) , (setx+10, sety+40, 255, 3), 0)
        pygame.draw.rect(win, (0,0,0) , (setx+10, sety+80, 255, 3), 0)
        pygame.draw.rect(win, (0,0,0) , (setx+10, sety+80+40, 255, 3), 0)
        settitle = font.render("Kolor tla (RGB)", 1, (0, 0, 0))
        win.blit(settitle, (setx+10, sety+10))
        #suwaki
        tsetr = setx+setr
        tsetg = setx+setg
        tsetb = setx+setb
        suwaka = pygame.draw.rect(win, (255,0,0) , (tsetr+10, sety+40, 15, 15), 0)
        suwakb = pygame.draw.rect(win, (0,255,0) , (tsetg+10, sety+80, 15, 15), 0)
        suwakc = pygame.draw.rect(win, (0,0,255) , (tsetb+10, sety+80+40, 15, 15), 0)
        if mysz.colliderect(suwaka) and klik == 1:
            if keys[pygame.K_LEFT] and tsetr>setx:
                setr=setr-1
            if keys[pygame.K_RIGHT] and tsetr<setx+255:
                setr=setr+1

        if mysz.colliderect(suwakb) and klik == 1:
            if keys[pygame.K_LEFT] and tsetg>setx:
                setg=setg-1
            if keys[pygame.K_RIGHT] and tsetg<setx+255:
                setg=setg+1

        if mysz.colliderect(suwakc) and klik == 1:
            if keys[pygame.K_LEFT] and tsetb>setx:
                setb=setb-1
            if keys[pygame.K_RIGHT] and tsetb<setx+255:
                setb=setb+1
                

        setend = pygame.draw.rect(win, (200, 0, 0), (setx, sety-30,30,30))
        setmove = pygame.draw.rect(win, (200, 0, 200), (setx+30, sety-30,30,30))
        win.blit(winbtns, (setx, sety-30))
        if mysz.colliderect(setend) and klik == 1:
            given_file = open("bcgr.data", "w")
            given_file.write(str(setr))
            given_file.close()
            given_file = open("bcgg.data", "w")
            given_file.write(str(setg))
            given_file.close()
            given_file = open("bcgb.data", "w")
            given_file.write(str(setb))
            given_file.close()
            
            settingslan = 0
            bcolor = 0
        if mysz.colliderect(setmove) and klik == 1:
            setx = myszx
            setx=setx-45
            sety = myszy
            sety=sety+15



        
    #mysz
    pygame.draw.circle(win, (255, 255, 255), (myszx, myszy), 6, 5)
    mysz = pygame.draw.circle(win, (0, 0, 0), (myszx, myszy), 4)
    #odpalanie
    if mysz.colliderect(sysend) and klik == 1:
        exit()
    if mysz.colliderect(pliki) and klik == 1:
        plikilan = 1
    if mysz.colliderect(pong) and klik == 1:
        ponglan = 1
        pongx = 100
        pongy = 100
        ballx = pongx+10
        bally = pongy+10
        ballmx = 1
        ballmy = 1
    if mysz.colliderect(settings) and klik == 1:
        settingslan = 1
        setx=100
        sety=60
        tsetx=100
        tsety=60
    if mysz.colliderect(write) and klik == 1:
        writelan = 1
    if mysz.colliderect(clock) and klik == 1:
        clocklan = 1
        zegx = 100
        zegy = 350
    pygame.display.flip()
    pygame.display.update()
    win.fill((tlor, tlog, tlob))
    pygame.time.delay(15)
