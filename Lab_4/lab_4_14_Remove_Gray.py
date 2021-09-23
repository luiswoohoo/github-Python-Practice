#Summary: Given integer values for red, green, and blue, subtract the gray from each value.
#Computers represent color by combining the sub-colors red, green, and blue (rgb).
# #Each sub-color's value can range from 0 to 255. Thus (255, 0, 0) is bright red,
# #(130, 0, 130) is a medium purple, (0, 0, 0) is black, (255, 255, 255) is white,
# #and (40, 40, 40) is a dark gray. (130, 50, 130) is a faded purple,
# #due to the (50, 50, 50) gray part. (In other words, equal amounts of red, green, blue yield gray).
#
#Given values for red, green, and blue, remove the gray part.
#
#Ex: If the input is:
#
#130 50 130
#
#the output is:
#
#80 0 80
#
#Find the smallest value, and then subtract it from all three values, thus removing the gray.
compareRGB = []
gray_RGB = []

print("Enter the RGB value for red (between 0 and 255):")
red = int(input())
compareRGB.append(red)

print("Enter the RGB value for green (between 0 and 255):")
green = int(input())
compareRGB.append(green)

print("Enter the RGB value for blue (between 0 and 255):")
blue = int(input())
compareRGB.append(blue)

print("These are the values you entered:", compareRGB)

compareRGB.sort()

smallest_value = compareRGB[0]

if ((red - smallest_value) < 0):
    new_red = 0
else:
    new_red = red - smallest_value

gray_RGB.append(new_red)

if ((green - smallest_value) < 0):
    new_green = 0
else:
    new_green = green - smallest_value

gray_RGB.append(new_green)

if ((blue - smallest_value) < 0):
    new_blue = 0
else:
    new_blue = blue - smallest_value

gray_RGB.append(new_blue)

print("RGB without gray is:")
print(gray_RGB)

print(gray_RGB[0], gray_RGB[1], gray_RGB[2])

