from PIL import Image, ImageEnhance

# Open image file
image = Image.open("text2.jpeg")

# Apply contrast enhancement
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(1.5)

# Apply brightness enhancement
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(1.2)

# Save enhanced image
image.save("text2_n.jpeg")
