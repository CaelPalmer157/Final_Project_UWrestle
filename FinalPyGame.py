import pygame

# pygame setup
promptVar = "Hello World!"
resultVar = "Final Result"
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

    # Create the selection box rectangle
    selectRect = pygame.Rect(100, 100, 500, 100)
    colorSelectRec = WHITE

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
    ScoreRect = pygame.Rect(600, 100, 300, 100)
    colorScoreRect = BLUE

    # Create the rectangle for question box
    PromptRect = pygame.Rect(100, 10, 800, 90)
    colorPromptRect = BLACK

    #Create the rectangle for results box
    resultsRect = pygame.Rect(100, 200, 800, 90)
    colorResultsRect = BLACK

    # Main loop
    running = True
    while numberOfLoops < 9:

        # Initilize Text
        if numberOfLoops == 0:
            promptVar = "opponent gets you in front headlock"
            response1Var = "Control Elbow, Circle Up, Shoot"
            response2Var = "Reach Up, Headlock Opponent"
            response3Var = "Cartwheel to switch"

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # check if mouse clicks inside rectangle
                    if selectRect.collidepoint(mouse_pos):
                        # Check for response 1
                        if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(
                                mouse_pos):
                            # Change Score
                            selection = 0
                            scoreP += 3
                        # Check for response 2
                        elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 1
                            scoreO += 7
                        # Check for response 3
                        elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 2
                            scoreO += 3
                    numberOfLoops += 1


        elif numberOfLoops == 1:
            promptVar = "Opponent sprawls on your single leg"
            response1Var = "Elbow down and run backside"
            response2Var = "Crossface Cradle"
            response3Var = "Short sit and turn in"

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # check if mouse clicks inside rectangle
                    if selectRect.collidepoint(mouse_pos):
                        # Check for response 1
                        if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(
                                mouse_pos):
                            # Change Score
                            selection = 0
                            scoreP += 3
                        # Check for response 2
                        elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 1
                            scoreO += 3
                        # Check for response 3
                        elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 2
                            scoreO += 3
                        numberOfLoops += 1

        elif numberOfLoops == 2:
            promptVar = "Opponent sits the corner on your Hi-C"
            response1Var = "Let your shoulder slip"
            response2Var = "Arm Bar"
            response3Var = "Table the foot"

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # check if mouse clicks inside rectangle
                    if selectRect.collidepoint(mouse_pos):
                        # Check for response 1
                        if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(
                                mouse_pos):
                            # Change Score
                            selection = 0
                            scoreO += 3
                        # Check for response 2
                        elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(
                                mouse_pos):
                            # Change score (no change for this answer)
                            selection = 1
                        # Check for response 3
                        elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 2
                            scoreP += 3
                        numberOfLoops += 1

        elif numberOfLoops == 3:
            promptVar = "You and opponent are in ankle scramble"
            response1Var = "Turn away and kick"
            response2Var = "Get high and elevate opponents foot"
            response3Var = "Stay low with head towards the mat"

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # check if mouse clicks inside rectangle
                    if selectRect.collidepoint(mouse_pos):
                        # Check for response 1
                        if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(
                                mouse_pos):
                            # Change Score
                            selection = 0
                            scoreO += 3
                        # Check for response 2
                        elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 1
                            scoreP += 3
                        # Check for response 3
                        elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 2
                            scoreP += 3
                        numberOfLoops += 1


        elif numberOfLoops == 4:
            promptVar = "You are On Top, Opponent Stands Up"
            response1Var = "Pull opponent backwards"
            response2Var = "Lift opponent and mat return"
            response3Var = "Try to reach for single leg"

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # check if mouse clicks inside rectangle
                    if selectRect.collidepoint(mouse_pos):
                        # Check for response 1
                        if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(
                                mouse_pos):
                            # Change Score
                            selection = 0
                            scoreO += 2
                        # Check for response 2
                        elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 1
                            scoreP += 4
                        # Check for response 3
                        elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 2
                            scoreO += 1
                        numberOfLoops += 1

        elif numberOfLoops == 5:
            promptVar = "You have backside single leg"
            response1Var = "Run forward"
            response2Var = "Dive at opponents body"
            response3Var = "Keep shoulder tight and climb legs"

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # check if mouse clicks inside rectangle
                    if selectRect.collidepoint(mouse_pos):
                        # Check for response 1
                        if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(
                                mouse_pos):
                            # Change Score
                            selection = 0
                            scoreO += 3
                        # Check for response 2
                        elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(
                                mouse_pos):
                            # Change score (no change)
                            selection = 1
                        # Check for response 3
                        elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 2
                            scoreP += 3
                        numberOfLoops += 1

        elif numberOfLoops == 6:
            promptVar = "You are in short offense position"
            response1Var = "Beat shoulder and chase hamstring"
            response2Var = "Switch to elbow deep front headlock"
            response3Var = "Reach for opponents hip"

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # check if mouse clicks inside rectangle
                    if selectRect.collidepoint(mouse_pos):
                        # Check for response 1
                        if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(
                                mouse_pos):
                            # Change Score
                            selection = 0
                            scoreP += 3
                        # Check for response 2
                        elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(
                                mouse_pos):
                            # Change score (no change)
                            selection = 1
                            scoreO += 3
                        # Check for response 3
                        elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(
                                mouse_pos):
                            # Change score (no change)
                            selection = 2
                        numberOfLoops += 1

        elif numberOfLoops == 7:
            promptVar = "You have Hi-C, but are bent over"
            response1Var = "Continue to run into opponent"
            response2Var = "Force crack down position"
            response3Var = "Off balance opponent, pop and lift"

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # check if mouse clicks inside rectangle
                    if selectRect.collidepoint(mouse_pos):
                        # Check for response 1
                        if response1.get_rect(center=(selectRect.centerx, selectRect.centery - 32)).collidepoint(
                                mouse_pos):
                            # Change Score (no change)
                            selection = 0
                        # Check for response 2
                        elif response2.get_rect(center=(selectRect.centerx + 0, selectRect.centery)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 1
                            scoreO += 3
                        # Check for response 3
                        elif response3.get_rect(center=(selectRect.centerx + 0, selectRect.centery + 32)).collidepoint(
                                mouse_pos):
                            # Change score
                            selection = 2
                            scoreP += 3
                        numberOfLoops += 1

        elif numberOfLoops == 8:
            if scoreP > scoreO:
                resultVar = "Congratulations!!! You Win!!!"
            # if player loses
            elif scoreP < scoreO:
                resultVar = "You lose. Put in the work and try again!!!"
            # if score is tied
            elif scoreP == scoreO:
                resultVar = "Tie. Play again to win overtime"

        #print responces
        response1 = font.render(response1Var, True, BLACK)
        response2 = font.render(response2Var, True, BLACK)
        response3 = font.render(response3Var, True, BLACK)

        #print scores
        playerScore = font.render(str(scoreP), True, WHITE)
        opponentScore = font.render(str(scoreO), True, WHITE)

        #print question font
        prompt = font.render(promptVar, True, WHITE)

        # print result font
        result = font.render(resultVar, True, WHITE)

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
        pygame.draw.rect(screen, colorSelectRec, selectRect)

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
        pygame.draw.rect(screen, colorScoreRect, ScoreRect)

        # Draw the lines of font for scoreboard
        screen.blit(playerScore, playerScore.get_rect(center=(ScoreRect.centerx-60, ScoreRect.centery)))
        screen.blit(opponentScore, opponentScore.get_rect(center=(ScoreRect.centerx+60, ScoreRect.centery)))

        # Draw the rectangle for question box
        pygame.draw.rect(screen, colorPromptRect, PromptRect)

        # Draw the lines of font for question box
        screen.blit(prompt, prompt.get_rect(center=(PromptRect.centerx, PromptRect.centery)))

        # Draw the rectangle for results box
        pygame.draw.rect(screen, colorResultsRect, resultsRect)

        # Draw the lines of font for results box
        screen.blit(result, result.get_rect(center=(resultsRect.centerx, resultsRect.centery)))

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()

