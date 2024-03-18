from PIL import Image, ImageDraw, ImageFont

def generate_label(ingredients, output_file='label.png', font_size=14):
    # Define image dimensions and background color
    width, height = 400, 200
    background_color = 'white'
    
    # Create a new image with white background
    image = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.load_default()
    
    # Define starting position for the ingredients
    x, y = 10, 10
    
    # Write ingredients on the image
    for ingredient in ingredients:
        draw.text((x, y), ingredient, fill='black', font=font)
        y += font_size + 2  # Move down for the next ingredient
    
    # Save the image
    image.save(output_file)
    print(f"Label generated and saved as {output_file}")

# Example usage
ingredients = [
    "Flour",
    "Sugar",
    "Eggs",
    "Butter",
    "Milk",
    "Baking Powder",
    "Vanilla Extract"
]

generate_label(ingredients)
