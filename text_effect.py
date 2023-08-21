import pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Adventure")

# Initialize player
player = pygame.Rect(50, 50, 50, 50)
player_color = (255, 0, 0)

custom_font = pygame.font.Font("custom-font.otf", 48)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    screen.fill((0, 0, 0))
    
    # Create text with pulsating effect
    pulsating_text = custom_font.render("Pulsating Text", True, (0, 0, 255))

    # Calculate pulsation factor based on time
    pulsation_factor = 1 + abs((pygame.time.get_ticks() % 1000) - 500) / 500

    width = int(pulsating_text.get_width() * pulsation_factor)
    height = int(pulsating_text.get_height() * pulsation_factor)

    # Scale the text based on pulsation factor
    pulsating_text = pygame.transform.scale(pulsating_text,
                    (width, height))

    # Calculate text position to center it on the screen
    text_x = width // 2 - pulsating_text.get_width() // 2
    text_y = 200

    screen.blit(pulsating_text, (text_x, text_y))
    pygame.draw.rect(screen, player_color, player)
    pygame.display.flip()

pygame.quit()
