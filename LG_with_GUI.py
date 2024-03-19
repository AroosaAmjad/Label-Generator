import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class LabelGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Label Generator")
        
        # Ingredient input
        self.ingredient_label = tk.Label(master, text="Enter Ingredients (one per line):")
        self.ingredient_label.pack()
        self.ingredient_entry = tk.Text(master, height=5, width=30)
        self.ingredient_entry.pack()
        
        # Generate button
        self.generate_button = tk.Button(master, text="Generate Label", command=self.generate_label)
        self.generate_button.pack()
        
        # Output label
        self.output_label = tk.Label(master, text="")
        self.output_label.pack()
        
    def generate_label(self):
        ingredients = self.ingredient_entry.get("1.0", tk.END).strip().split("\n")
        if not ingredients:
            self.output_label.config(text="No ingredients provided.")
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not output_file:
            self.output_label.config(text="Label generation canceled.")
            return
        
        generate_label(ingredients, output_file)
        self.output_label.config(text=f"Label generated and saved as {output_file}")

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
        bold_font = ImageFont.truetype(font_path, font_size+6)  # Larger and bold font for the heading
    except IOError:
        font = ImageFont.load_default()
        bold_font = ImageFont.load_default()
        print("Font file not found. Using default font.")
    
    # Define starting position for the ingredients
    x, y = 10, 10
    
    # Write heading
    heading = "Ingredients:"
    draw.text((x, y), heading, fill='black', font=bold_font)
    heading_size = draw.textsize(heading, font=bold_font)
    y += heading_size[1] + 5  # Move down for the ingredients
    
    # Write ingredients on the image
    for ingredient in ingredients:
        draw.text((x, y), ingredient, fill='black', font=font)
        y += font_size + 2  # Move down for the next ingredient
    
    # Save the image
    image.save(output_file)

def main():
    root = tk.Tk()
    app = LabelGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
