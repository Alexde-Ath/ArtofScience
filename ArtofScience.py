from PIL import Image, ImageDraw
import math

# Define the size of the image
width, height = 3000, 2000

# Create a new image with RGB 
image = Image.new('RGB',(width, height),'black')

# Create a draw object
draw = ImageDraw.Draw(image)

# Two UR colors
dandelion_yellow = '#FFD100' # '255, 209, 0'
rochester_blue = '#003C71' # '0,60,113'

def mandala():
    # Define the center and radius of the mandala
    center_x, center_y = width // 2, height // 2
    radius = min(width, height) 

    # Draw a series of lines to create a mandala effect
    for i in range(360):  # Increase the number of lines
        angle = i  # Decrease the angle between lines
        end_x = center_x + radius * math.cos(math.radians(angle))
        end_y = center_y + radius * math.sin(math.radians(angle))

        # Alternate colors
        color = dandelion_yellow if i % 2 == 0 else rochester_blue

        # Draw the line
        draw.line([(center_x, center_y), (end_x, end_y)], fill=color)

        # Draw additional lines to create a more intricate pattern
        if i % 30 == 0:  # Every 30 degrees
            for j in range(1, 6):  # Draw 5 additional lines
                inner_radius = radius * j / 6  # Decrease the radius for each additional line
                inner_end_x = center_x + inner_radius * math.cos(math.radians(angle))
                inner_end_y = center_y + inner_radius * math.sin(math.radians(angle))
                draw.line([(center_x, center_y), (inner_end_x, inner_end_y)], fill=color)

mandala()

# REQUIREMENT: Save the image with high resolution 
image.save('ArtofCS.jpeg', 'JPEG', quality=95, dpi=(300, 300)) 