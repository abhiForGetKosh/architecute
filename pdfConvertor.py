import img2pdf
from PIL import Image
import os
  
# storing image path
img_path = "C:/Users/Admin/Desktop/GfG_images/do_nawab.png"
  
# storing pdf path
pdf_path = "C:/Users/Admin/Desktop/GfG_images/file.pdf"
  
# opening image
image = Image.open(img_path)
  
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
  
# opening or creating pdf file
file = open(pdf_path, "wb")
  
# writing pdf files with chunks
file.write(pdf_bytes)
  
# closing image file
image.close()
  
# closing pdf file
file.close()
  
# output
print("Successfully made pdf file")


#c1 f3

#c1 f2
#c2 f2

#c1 f1
#c2 f1

