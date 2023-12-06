import pygame

# pygame setup
promptVar = "Hello World!"
response1Var = "1"
response2Var = "2"
response3Var = "3"
scoreP = 0
scoreO = 0
numberOfLoops = 0
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Define the font
    font = pygame.font.Font(None, 32)

    # Create the selection box selectRect
    selectRect = pygame.Rect(100, 100, 300, 100)
    color = WHITE

    # Create the lines of font for selection box
    response1 = font.render(response1Var, True, BLACK)
    response2 = font.render(response2Var, True, BLACK)
    response3 = font.render(response3Var, True, BLACK)

    # Create the selection arrow
    arrow_pos = (selectRect.left + selectRect.width - 30, selectRect.top + 30)
    arrow_color = RED

    # Define the selection
    selection = 0

    # Create the scoreboard
    ScoreRect = pygame.Rect(400, 100, 300, 100)
    color2 = BLUE

    # Create the rectangle for question box
    PromptRect = pygame.Rect(100, 10, 600, 90)
    color3 = BLACK

    # Main loop
    running = True
    while numberOfLoops < 8:

        #Initilize Text
        if numberOfLoops == 0:
            promptVar = "opponent gets you in front headlock"
            response1Var = "Control Elbow, Circle Up"
            response2Var = "Reach Up, Headlock Opponent"
            response3Var = "Cartwheel to switch"

        elif numberOfLoops == 1:
            promptVar = "Opponent sprawls on your single leg"
            response1Var = "Elbow down and run backside"
            response2Var = "Crossface Cradle"
            response3Var = "Short sit and turn in"

        elif numberOfLoops == 2:
            promptVar = "Opponent sprawls"
            response1Var = "Elbow down and run backside"
            response2Var = "Crossface Cradle"
            response3Var = "Short sit and turn in"

        elif numberOfLoops == 3:
            promptVar = "Opponent sprawls"
            response1Var = "Elbow down and run backside"
            response2Var = "Crossface Cradle"
            response3Var = "Short sit and turn in"

        elif numberOfLoops == 4:
            promptVar = "Opponent sprawls"
            response1Var = "Elbow down and run backside"
            response2Var = "Crossface Cradle"
            response3Var = "Short sit and turn in"

        elif numberOfLoops == 5:
            promptVar = "Opponent sprawls"
            response1Var = "Elbow down and run backside"
            response2Var = "Crossface Cradle"
            response3Var = "Short sit and turn in"

        elif numberOfLoops == 6:
            promptVar = "Opponent sprawls"
            response1Var = "Elbow down and run backside"
            response2Var = "Crossface Cradle"
            response3Var = "Short sit and turn in"

        elif numberOfLoops == 7:
            promptVar = "Opponent sprawls"
            response1Var = "Elbow down and run backside"
            response2Var = "Crossface Cradle"
            response3Var = "Short sit and turn in"


        # if

        #print responces
        response1 = font.render(response1Var, True, BLACK)
        response2 = font.render(response2Var, True, BLACK)
        response3 = font.render(response3Var, True, BLACK)

        #print scores
        playerScore = font.render(str(scoreP), True, WHITE)
        opponentScore = font.render(str(scoreO), True, WHITE)

        #print question font
        prompt = font.render(promptVar, True, WHITE)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if the mouse clicked inside the rectangle
                if selectRect.collidepoint(mouse_pos):
                    # Check which line of font was clicked
                    if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(mouse_pos):
                        selection = 0
                    elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(mouse_pos):
                        selection = 1
                    elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(mouse_pos):
                        selection = 2

        # Fill the background
        bGimage = pygame.image.load("Assets/wrestlingMat.jpg")
        background_image = pygame.transform.scale(bGimage, screen.get_size())
        screen.blit(background_image, (0, 0))

        # Draw the selectRect for option box
        pygame.draw.rect(screen, color, selectRect)

        # Draw the lines of font
        screen.blit(response1, response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)))
        screen.blit(response2, response2.get_rect(center=(selectRect.centerx, selectRect.centery)))
        screen.blit(response3, response3.get_rect(center=(selectRect.centerx, selectRect.centery + 32)))

        # Draw the selection arrow
        if selection == 0:
            arrow_pos = (selectRect.left + selectRect.width - 30, selectRect.top + 15)
            arrow_color = RED
        elif selection == 1:
            arrow_pos = (selectRect.left + selectRect.width - 30, selectRect.top + 45)
            arrow_color = GREEN
        elif selection == 2:
            arrow_pos = (selectRect.left + selectRect.width - 30, selectRect.top + 80)
            arrow_color = BLUE

        pygame.draw.polygon(screen, arrow_color, [(arrow_pos[0], arrow_pos[1]), (arrow_pos[0] + 10, arrow_pos[1] + 5),
                                                  (arrow_pos[0] + 10, arrow_pos[1] - 5)])

        # Draw the selectRect for scoreboard
        pygame.draw.rect(screen, color2, ScoreRect)

        # Draw the lines of font for scoreboard
        screen.blit(playerScore, playerScore.get_rect(center=(ScoreRect.centerx-60, ScoreRect.centery)))
        screen.blit(opponentScore, opponentScore.get_rect(center=(ScoreRect.centerx+60, ScoreRect.centery)))

        # Draw the selectRect for question box
        pygame.draw.rect(screen, color3, PromptRect)

        # Draw the lines of font for scoreboard
        screen.blit(prompt, prompt.get_rect(center=(PromptRect.centerx, PromptRect.centery)))

        # Update the display
        pygame.display.flip()

    # # Quit pygame
    pygame.quit()

    # #add ground
    # ground_rect = pygame.Rect(0, screen.get_height() - 50, screen.get_width(), 50)
    #
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()