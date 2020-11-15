import os


#A simpler way to write the extract place function
def extract_place(filename):
    return filename.split('_')[1]

#Create a directory for each location
def make_place_directories(places):
    for place in places:
        os.mkdir(place)

def organize_photos(directory):
    #First, extract the place names.
    os.chdir(directory)
    originals = os.listdir()
    places = []
    #This loop creates the list needed to pass into the create directory function
    for filename in originals:
        place = extract_place(filename)
        #To ensure we don't pass make_place function duplicates add 
        # an if statement before appending
        if place not in places:
            places.append(place)
            
    #Second, make place directories.
    
    make_place_directories(places)

    #Third, move files to the directory.
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))

if __name__ == __'main'__:
    organize_photos("Photos")

