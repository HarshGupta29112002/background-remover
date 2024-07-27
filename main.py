from rembg import remove
import easygui as eg
from PIL import Image

inputPath = eg.fileopenbox(title = 'select image file')
outPath = eg.filesavebox(title = 'Save file to.. ')

input = Image.open(inputPath)
output = remove(input)

output.save(outPath)



