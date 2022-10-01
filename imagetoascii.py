from PIL import Image

mode = "black" # "white" or "black" - chooses either to use pure white or pure black to determine wheither or not a pixel should be a ## or --

image = Image.open("happyman.png")
pixels = image.load()

asciioutput = ""

for i in range(image.height):
    for o in range(image.width):
        if mode == "white":
            if pixels[o, i] != (255, 255, 255):
                asciioutput += "--"
            else:
                asciioutput += "##"
        elif mode == "black":
            if pixels[o, i] != (0, 0, 0):
                asciioutput += "##"
            else:
                asciioutput += "--"
    asciioutput += "\n"

textfile = open("asciioutput.txt", "w")
textfile.write(asciioutput)
textfile.close()