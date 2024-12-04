import csv, re, os
from datetime import date

# path settings
current_year = date.today().year
last_year = current_year - 1
homedir = os.path.expanduser('~')
path_script = os.path.join(os.path.dirname(__file__))
path_year = os.path.join(os.path.dirname(__file__), "oapen")
path_input_output = os.path.join(path_script, 'input-output')

print("To use this script, make sure the following files are present:")
print(" - The downloaded Oapen data .csv files per book (in the 'oapen' folder)")
print(" - The book_titles_merged.csv file in the input-output folder.")
print()
print(f"The path to the oapen folder is: \n{path_year}")
print()
input("If you are sure that these requirements are met, press Enter to continue. \n")
print()
print("Starting script.")

def clean_filename(filename):
    # str(file).replace(":","-")
    # clean_string = re.sub("[^0-9a-zA-Z\s]+", "", filename)
    # clean_string.lower()
    clean_string = ''.join(letter for letter in filename if letter.isalnum())
    return clean_string

# open the book titles file and get a list of the oapen books
oapen_titles = []
titles_file = os.path.join(path_input_output, "book_titles_merged.csv")
with open(titles_file, 'r', encoding='utf-16') as file:
    reader = csv.reader(file)
    reader = [[c.replace('\ufeff', '') for c in row] for row in reader]
    # make a list of the titles and their filename versions (i.e. 'cleaned' versions)
    for row in reader:
        # print(row)
        full_title = row[0]
        oapen_title = row[1]
        oapen_filename = clean_filename(oapen_title)
        oapen_titles.append([oapen_title, oapen_filename])
        print([oapen_title, oapen_filename])

# create the new oapen master file with headers
oapen_master_file = os.path.join(path_input_output, "rd_oapen.csv")
with open(oapen_master_file, 'w', newline='', encoding='utf-16') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(["title", "country", "country_code", "total"])
    file.close()

# make a new list for all the oapen data, to later write to the oapen master file
rd_oapen = []
# rd_oapen.append(['title', 'country', 'country_code', 'total'])

# define empty list for unmatched filenames
unmatched_filenames = []

# iterate through files in oapen downloads folder and write to a new .csv file
with open(oapen_master_file, 'a', newline='', encoding='utf-16') as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    print(f"Iterating through all files in {path_year}")
    for filename in os.listdir(path_year):
        # print(filename)
        file = os.path.join(path_year, filename)
        # if found is file and ends in ".csv", open it
        if os.path.isfile(file):
            file_name, file_extension = os.path.splitext(filename)
            if file_extension == ".csv":
                with open(file, 'r', encoding='utf-8-sig') as infile:
                    print()
                    print(f"Reading {filename}")
                    reader = csv.DictReader(infile)
                    # skip the header (first row)
                    # next(reader, None)
                    # print(reader[0])
                    # reader.remove(reader[0])
                    # match the filename to the correct oapen title
                    title_match = ""
                    print(f"Matching {file} to title.")
                    match_found = False
                    unmatched_counter = 1
                    for title in oapen_titles:
                        # print(title)
                        # file_name = str(filename).split(".")
                        #print(filename)
                        if str(file_name[:-2]) == str(title[1]):
                            title_match = title[0]
                            match_found = True
                            print(f"{filename} matched to {title_match}")
                    # append each remaining row to the new master file
                    if match_found == False:
                        print(f"{file_name} could not be matched. Please check manually after the script is done.")
                        unmatched_filenames.append(f"UNMATCHED_{unmatched_counter}: {file_name}")
                    print("Writing to new file.")
                    for row in reader:
                        # print(row)
                        if len(title_match) != 0:
                            new_row = [title_match]
                        else: 
                            new_row = [f"UNMATCHED_{unmatched_counter}"]
                        # new_row.append(row['\ufeff"country"'])
                        new_row.append(row['country'])
                        new_row.append(row['countryCode'])
                        new_row.append(row['total'])
                        rd_oapen.append(row)
                        writer.writerow(new_row)

# report on written file
print()
print("The Oapen data files have been merged to one .csv file: ")
print(oapen_master_file)

# report on unmatched filenames
if len(unmatched_filenames) > 0:
    print()
    print("Some filenames could not be matched. Please check these manually:")
    for item in unmatched_filenames:
        print(item)
    # write unmatched filenames to .txt file
    unmatched_file_path = os.path.join(path_input_output, "oapen_unmatched_files.txt")
    print()
    print(f"A list of the unmatched files has been written to {unmatched_file_path}")
    with open (unmatched_file_path, 'w') as file: 
        for item in unmatched_filenames:
            file.write(f"{item}\n")

print()
print("Script finished.")
input("Press Enter to close.")

# print("Results:")
# for row in rd_oapen:
#     print(row)
