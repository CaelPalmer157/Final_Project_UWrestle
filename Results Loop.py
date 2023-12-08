elif numberOfLoops == 8:
# if player wins
if scoreP > scoreO:
    resultVar = "Congratulations!!! You Win!!!"
elif scoreP < scoreO:
    resultVar = "You lose. Put in the work and try again!!!"
elif scoreP == scoreO:
    resultVar = "Tie. Play again to win overtime"
# print result font
result = font.render(resultVar, True, WHITE)
# Draw the rectangle for results box
pygame.draw.rect(screen, colorResultRect, ResultRect)
# Draw the lines of font for results box
screen.blit(result, result.get_rect(center=(ResultRect.centerx, ResultRect.centery)))