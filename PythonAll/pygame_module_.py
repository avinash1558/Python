# pip install pygame


# from pygame import mixer
  
# # Starting the mixer
# mixer.init()
  
# # Loading the song
# mixer.music.load("song.mp3")
  
# # Setting the volume
# mixer.music.set_volume(0.7)
  
# # Start playing the song
# mixer.music.play()
  
# # infinite loop
# while True:
      
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input("  ")
      
#     if query == 'p':
  
#         # Pausing the music
#         mixer.music.pause()     
#     elif query == 'r':
  
#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'e':
  
#         # Stop the mixer
#         mixer.music.stop()
#         break

#video
# import pygame
# from pygame import display,movie
# pygame.init()
# screen = pygame.display.set_mode((1024, 768))
# background = pygame.Surface((1024, 768))

# screen.blit(background, (0, 0))
# pygame.display.update()

# movie = pygame.movie.Movie('C:\Python27\1.mpg')
# mrect = pygame.Rect(0,0,140,113)
# movie.set_display(screen, mrect.move(65, 150))
# movie.set_volume(0)
# movie.play()
 
# # http://www.fileformat.info/format/mpeg/sample/index.dir
# import pygame

# FPS = 60

# pygame.init()
# clock = pygame.time.Clock()
# movie = pygame.movie.Movie('mp3/audio.mp3')
# screen = pygame.display.set_mode(movie.get_size())
# movie_screen = pygame.Surface(movie.get_size()).convert()

# movie.set_display(movie_screen)
# movie.play()
# playing = True
# while playing:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             movie.stop()
#             playing = False

#     screen.blit(movie_screen,(0,0))
#     pygame.display.update()
#     clock.tick(FPS)

# pygame.quit()
