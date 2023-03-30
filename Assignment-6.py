master_list = []
male = []
female = []
band = []
dj = []

for x in range(10):
    artist_name = input("Enter an artist name of choice >>> ")
    artist_type = input("Enter the type of artist. Use 'M' for male, 'F'' for female, 'B' for band, 'D' for DJs >>> ")
  
    master_list.append(artist_name)
    if artist_type == 'M' or 'm':
        male.append(artist_name)
    elif artist_type == 'F' or 'f':
        female.append(artist_name)
    elif artist_type == 'B' or 'b':
        band.append(artist_name)
    elif artist_type == 'D' or 'd':
        dj.append(artist_name)
    else:
        print("You entered an invalid artist type. Please try again and enter 'M', 'F', 'B', or 'D'.")

print("Male artists:", male)
print("Female arists:", female)
print("Bands:", band)
print("DJs:", dj)

print("All artists:", master_list)
