import fitz  # PyMuPDF
import sys
import os

currentDir = os.getcwd()
print(currentDir)
if not os.path.exists(os.path.join(currentDir, "input")):
    os.makedirs(os.path.join(currentDir, "input"))
if not os.path.exists(os.path.join(currentDir, "output")):
    os.makedirs(os.path.join(currentDir, "output"))

folderPath = os.path.join(currentDir, "input")

for file in os.listdir(folderPath):
    fullPath = os.path.join(folderPath, file)
    if os.path.isfile(fullPath):
        print(fullPath)
        fileName = file[:-4]
        doc = fitz.open(fullPath)
        for page in doc:
            count = page.number + 1
            pix = page.get_pixmap() #Render page to an image
            pix.save(os.path.join(currentDir, "output//" + fileName + " [page %i].png" % count)) #Save the image as a PNG
