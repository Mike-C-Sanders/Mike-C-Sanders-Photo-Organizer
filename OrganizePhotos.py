import os

os.chdir("Photos")
originals = os.listdir()

print(originals)#printing to test my code. 

#My First atempt using the find method
def extract_place(filename):
    first = filename.find("_")
    partial = filename[first+1:]
    second = partial.find("_")
    full = partial[:second]
    return full
