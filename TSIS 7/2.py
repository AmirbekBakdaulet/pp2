import pygame, os
pygame.init()
path = input("path:")
songs = [file for file in os.listdir(path) if file.endswith(".mp3")]
c=0
print(songs)
pygame.display.set_mode((100, 100))
done = False
while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE]:
                    pygame.mixer.music.load(songs[c])
                    pygame.mixer.music.play()
                elif pressed[pygame.K_s]:
                     pygame.mixer.music.stop()
                elif pressed[pygame.K_RIGHT]:
                    c=(c+1)%len(songs)
                    pygame.mixer.music.load(songs[c])
                    pygame.mixer.music.play()
                elif pressed[pygame.K_LEFT]:
                    c=(c-1)%len(songs)
                    pygame.mixer.music.load(songs[c])
                    pygame.mixer.music.play()
                elif pressed[pygame.K_q]:
                    done = True
pygame.quit()