from PIL import Image, ImageDraw, ImageFont

def generate_label(ingredients, output_file='label.png', font_size=16, font_path='arial.ttf'):
    # Define image dimensions and background color
    width, height = 400, 200
    background_color = 'white'
    
    # Create a new image with white background
    image = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(image)
    
    # Load a font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Font file not found. Using default font.")
    
    # Define starting position for the ingredients
    x, y = 10, 10
    
    # Write ingredients on the image
    for ingredient in ingredients:
        draw.text((x, y), ingredient, fill='black', font=font)
        y += font_size + 2  # Move down for the next ingredient
    
    # Save the image
    image.save(output_file)
    print(f"Label generated and saved as {output_file}")

# Get user input for ingredients
def get_user_input():
    ingredients = []
    print("Enter the list of ingredients (one per line). Enter 'done' when finished:")
    while True:
        ingredient = input().strip()
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)
    return ingredients

# Example usage
ingredients = get_user_input()
if ingredients:
    generate_label(ingredients)
else:
    print("No ingredients provided. Exiting.")