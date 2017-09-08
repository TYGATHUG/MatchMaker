#!/usr/bin/python
import os, sys

usernames = ["Jerrell", "Stan", "Ross", "Cesar", "Fredric", "Henry", "Anderson", "Alec", "Jon", "Noel", "Fidel"
	, "Brady", "Wallace", "Gayle", "Neil", "Horacio", "Florencio", "Hassan", "Raphael", "Jay", "Ali", "Lynn"
	, "Gordon", "Waylon", "Randal", "Emilio", "Fletcher", "Brett", "Emerson", "Lindsey", "Homer", "Blake", "Jarred"
	, "Damian", "Paul", "Issac", "Alvaro", "Terry", "Bryan", "Hong", "Theo", "Les", "Mohamed", "Demetrius"
	, "Benjamin", "Elde", "Christoper", "Jospeh", "Dusty", "Edwardo", "Florance", "Nelly",  "Shanti", "Cristal"
	, "Meghann", "Shelley", "Tessa", "Amada", "Argentina", "Terina", "Karie", "Adriane", "Sarita", "Ofelia", "Mollie"
	, "Shawnda", "Alise", "Chantay", "Verda", "Delmy", "Claire", "Lakeisha", "Carolina", "Hilaria", "Fanny", "Sharon"
	, "Shavonda", "Millicent", "Yan", "Nanci", "Lecia", "Dinah", "Adele", "Mindy", "Tori", "Monica", "Agripina"
	, "Myesha", "Rebecka", "Crista", "Shu", "Kasandra", "Tierra", "Merly", "Evia", "Hae", "Yer", "Sun", "Dahlia", "Marianna"
		 ]
		
# store source/target folder path
source_path = os.getcwd() + "/profile_collection/"
target_path = os.getcwd() + "/profile_collection_converted/"

print "Source: ", source_path
print "Target: ", target_path

# change to source directory
os.chdir(source_path)

# photo files
photo_collection = os.listdir(os.getcwd())

for i in range(100):
	
	for j in photo_collection:
		filename_split = j.split('.')[0]
		
		if str(i) == filename_split:
			old_filename = j
			username = usernames[i].lower()
			
			# rename file & store in target directory
			os.rename(old_filename, target_path + username + ".jpg")
			break;
	
print "Successfully renamed"
	
