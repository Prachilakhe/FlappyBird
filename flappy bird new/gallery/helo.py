   if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

          elif event.type == KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
              return