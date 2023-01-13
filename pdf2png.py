import glob, sys, fitz

# To get better resolution
zoom_x = 4.0  # horizontal zoom
zoom_y = 4.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension


doc = fitz.open("hp48g-pg-en.pdf")  # open document
for page in doc:  # iterate through the pages
    pix = page.get_pixmap(matrix=mat)  # render page to an image
    pix.save("page-%i.png" % page.number)  # store image as a PNG