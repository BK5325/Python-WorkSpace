import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

# Specify the barcode format
barcode_format = barcode.get_barcode_class('ean13')

# Define the barcode number
barcode_number = '1234567895741'

# Generate the barcode image
barcode_image = barcode_format(barcode_number, writer=ImageWriter())

# Specify the filename
barcode_filename = 'barcode_image'

# Save the barcode image
barcode_image.save(barcode_filename)

# Display the barcode image
display(Image(filename=f'{barcode_filename}.png'))
