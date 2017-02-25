# Notpil.py - Just make captcha image readable
# @author: tibOin
# @description : Try to remove noise and rebuild missing parts of extracted characters.

# Image matrix analysis --------------------------------------------------------
# Get the neighbourhood of pixel at (x, y) using image width and height as limit
def getNeighbourhood(x, y, w, h):
    supposedNeighbourhood = [
        (x-1, y+1),
        (x, y+1),
        (x+1, y+1),
        (x-1, y),
        (x+1, y),
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1)
    ]
    actualNeighbourhood = []

    for neighborCoords in supposedNeighbourhood:
        eqs, why = neighborCoords
        if eqs >= 0 and eqs < w and why >= 0 and why < h:
            actualNeighbourhood.append(neighborCoords)
    return actualNeighbourhood

# Tells us if current pixel is surrounded by a majority of black pixels
def majorityBlackNeighboursIn(neighbourhood, pix):
    poids = 0

    for neighbour in neighbourhood:
        x, y = neighbour
        if pix[x, y] == (0, 0, 0):
            poids += 1

    if poids > 4:
        return True
    else:
        return False

# Tells us if current pixel is surrounded by a majority of white pixels
def majorityWhiteNeighboursIn(neighbourhood, pix):
    poids = 0
    for neighbour in neighbourhood:
        x, y = neighbour
        if pix[x, y] == (255, 255, 255):
            poids += 1
    if poids > 5:
        return True
    else:
        return False
# ------------------------------------------------------------------------------

# Image manipulations ----------------------------------------------------------
# Transform all non-white pixels to black.
def binarize(image):
    width, height = image.size
    pix = image.load()
    for x in range(width):
        for y in range(height):
            if pix[x, y] != (255, 255, 255):
                pix[x, y] = (0, 0, 0)

# Remove all noise that is not our pattern color.
def cleanByColor(image):
    width, height = image.size
    pix = image.load()
    for x in range(width):
        for y in range(height):
            if pix[x, y] != (140, 140, 140): # Our pattern color
                pix[x, y] = (255, 255, 255)

# Remove noise that stay (which is now black)
def cleanNoise(image):
    width, height = image.size
    pix = image.load()
    for x in range(width):
        for y in range(height):
            neighbourhood = getNeighbourhood(x, y, width, height)
            if pix[x, y] == (0, 0, 0) and majorityWhiteNeighboursIn(neighbourhood, pix):
                pix[x, y] = (255, 255, 255) # On change la couleur du pixel en blanc.

# Fill wholes -> Try to rebuild missing parts (at least 2 times...)
def rebuild(image):
    width, height = image.size
    pix = image.load()
    for x in range(width):
        for y in range(height):
            neighbourhood = getNeighbourhood(x, y, width, height)
            if pix[x, y] != (0, 0, 0) and majorityBlackNeighboursIn(neighbourhood, pix):
                pix[x, y] = (0, 0, 0) # On change la couleur du pixel en noir.
# ------------------------------------------------------------------------------

# Main -------------------------------------------------------------------------
import time
import sys
from PIL import Image
start = time.time()
image = Image.open('images/securimage.png')
image.show()
cleanByColor(image)
image.show()
image.save("images/extracted_color.png")
binarize(image)
image.save("images/binarized.png")
image.show()
cleanNoise(image)
image.save("images/noise_cleaned.png")
image.show()
for i in range(10):
    rebuild(image)
image.save("images/rebuilt_and_waiting_next_step.png")
image.show()
end = time.time()
print("\nDone in {} seconds").format(round(end - start, -1))
# ------------------------------------------------------------------------------
