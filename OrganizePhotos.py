import os

os.chdir("Photos")
originals = os.listdir()

print(originals)#printing to test my code. 

#My Second atempt using the find method
def extract_place(filename):
    parts = filename.split("_") # Get a list containing all the parts
    place_name = parts[1] # Use the index operator to select the second list item
    return place_name"""
