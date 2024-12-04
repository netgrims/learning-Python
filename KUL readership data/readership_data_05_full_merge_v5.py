import os
import pandas as pd
from datetime import date

# path settings
current_year = date.today().year
last_year = current_year - 1
homedir = os.path.expanduser('~')
path_script = os.path.join(os.path.dirname(__file__))
path_year = os.path.join(os.path.dirname(__file__), str(last_year) + "_oapen")
path_input_output = os.path.join(path_script, 'input-output')

print()
print(f"The current script will combine the readership data from Oapen, Jstor, and Project Muse.")
print()
print("Please make sure that the following files are present in the input-output folder:")
print(" - titles_merged.csv")
print(" - countries_combined.csv")
print(" - rd_oapen.csv")
print(" - rd_jstor.xlsx")
print(" - rd_muse.xlsx")
print(" - master_merge.xlsx (i.e. the output file of last year)")
print()
print(f"The input-output file is located here: \n{path_input_output}")
print()
print("If you have any of these files opened (e.g. in Excel), please close them before continuing.")
print("Make sure that you did not have any filters activated last time these files were open.")
print()
print("Also make sure that each of these has the proper column names: 'title', 'country', and 'total'.")
print()
print("FYI: last year's master_merge file will be saved to a backup file.")
print()
input("If you are ready, press Enter to continue.")

# open the merged country list (see previous script) as a pandas dataframe
country_list_file = "countries_combined.csv"
country_list_file = os.path.join(path_input_output, country_list_file)
with open(country_list_file, encoding='UTF-16') as infile:
    countries_df = pd.read_csv(infile, header=0)

# with open(country_list_file, 'r') as infile:
#     reader = csv.reader(infile)

# open the merged titles list (see previous script) as a pandas dataframe
merged_titles_file = "book_titles_merged.csv"
merged_titles_file = os.path.join(path_input_output, merged_titles_file)
with open(merged_titles_file, encoding='UTF-16') as infile:
    titles_df = pd.read_csv(infile, header=0)

# open oapen spreadsheet as pandas dataframe
oapen_spreadsheet = os.path.join(path_input_output, 'rd_oapen.csv')
with open(oapen_spreadsheet, encoding='UTF-16') as infile:
    oapen_df = pd.read_csv(infile, header=0)

# open jstor spreadsheet as pandas dataframe
jstor_spreadsheet = os.path.join(path_input_output, 'rd_jstor.xlsx')
jstor_df = pd.read_excel(jstor_spreadsheet, skiprows=0, header=0)

# open muse spreadsheet as pandas dataframe
muse_spreadsheet = os.path.join(path_input_output, 'rd_muse.xlsx')
muse_df = pd.read_excel(muse_spreadsheet, skiprows=0, header=0)

# open the master spreadsheet of last year as pandas dataframe
master_prev_spreadsheet = os.path.join(path_input_output, 'rd_master_merge.xlsx')
master_prev_df = pd.read_excel(master_prev_spreadsheet, skiprows=0, header=0)

# make a list of the oapen countries
countries_oapen = oapen_df['country'].to_list()
# get the unique countries by converting to a set and then back to a list
countries_oapen = list(set(countries_oapen))

# function to merge the countries based on the combined countries file
def uniformise_countries(input_df):
    # make a list of the countries in the input dataframe (i.e. the dataframe to uniformise)
    input_list = input_df['country'].to_list()
    unique_list = list(set(input_list))
    # filter out None and non-strings (e.g. panda non-string 'nan', and string 'nan')
    unique_list = list(filter(None, unique_list))
    unique_list = [x for x in unique_list if type(x) == str]
    unique_list = [i for i in unique_list if i != float("nan")]
    # print(unique_list)
    # iterate through the list of countries and replace the matching countries in the input dataframe
    for item in unique_list:
        print()
        print(f"Checking: {item}")
        df = countries_df
        # search the countries (i.e. merged) dataframe for a match to the item in the unique list (from the input_df)
        replacer_index = df.loc[(df == item).any(axis=1)].index[0]
        replacer_value = countries_df["country_code"].iloc[replacer_index]
        # replace each matching country in the input_df with the match from the merged countries dataframe.
        print(f"Index: {replacer_index}")
        print(f"Replacing '{item}' with '{replacer_value}'")
        input_df = input_df.replace(item, replacer_value)
    return input_df

# function to uniformise the titles based on the merged titles file
def uniformise_titles(input_df, database):
    # make a list of the titles in the input dataframe (i.e. the dataframe to uniformise)
    # the database variable can be oapen, jstor, or muse (cf. the column names of the merged titles file)
    column = f"{database} title"
    index_list = titles_df[column].to_list()
    unique_list = list(set(index_list))
    # filtering out None and non-strings (e.g. panda non-string 'nan', and string 'nan')
    unique_list = list(filter(None, unique_list))
    unique_list = [x for x in unique_list if type(x) == str]
    # unique_list = [i for i in unique_list if i != float("nan")]
    # print(unique_list)
    replaced_count = 0
    # iterate through the list of titles and replace the matching titles in the input dataframe
    for item in unique_list:
        print()
        print(f"Checking: {item}")
        df = titles_df
        index = df.loc[(df == item).any(axis=1)].index[0]
        replacer_title = titles_df["full title"].iloc[index]
        print(f"Index in reference dataframe: {index}")
        print(f"Replacing '{item}' with '{replacer_title}'")
        input_df = input_df.replace(item, replacer_title)
        replaced_count += 1
    print(f"{replaced_count} titles in {database} dataframe replaced.")
    return input_df

# function to perform the two uniformisation functions together
def uniformise_full(input_df, database):
    input_df = uniformise_countries(input_df)
    input_df = uniformise_titles(input_df, database)
    return input_df

# execute the uniformisation of all dataframes
print()
print("==========Uniformising Oapen dataframe.==========")
oapen_df = uniformise_full(oapen_df, "oapen")
print()
print("==========Uniformising Jstor dataframe.==========")
jstor_df = uniformise_full(jstor_df, "jstor")
print()
print("==========Uniformising Project Muse Dataframe.==========")
muse_df = uniformise_full(muse_df, "muse")

# remove the obsolete columns from the dataframes, and fill NaNs with 0s.
oapen_df = oapen_df[['title', 'country', 'total']].fillna(0)
jstor_df = jstor_df[['title', 'country', 'total']].fillna(0)
muse_df = muse_df[['title', 'country', 'total']].fillna(0)

# function to merge two dataframes an sum up their values in the 'total' columns
def merge_dataframe(df_01, df_02):
    # perform a pandas merge of two dataframes on the 'title' and 'country' columns
    # the 'total' columns will be added with '_x' and '_y' appended
    merged_df = pd.merge(df_01, df_02, on=['title', 'country'], how='outer', suffixes=('_x', '_y'))
    # make a sum of the total_x and total_y columns in a new 'total' column
    merged_df['total'] = merged_df[['total_x', 'total_y']].sum(axis=1)
    # remove the total_x and total_y columns
    merged_df = merged_df.drop(columns=['total_x', 'total_y'])
    return merged_df

# merge oapen and jstor into master dataframe
print()
print("Merging Oapen and Jstor dataframes.")
master_merge_df = merge_dataframe(oapen_df, jstor_df)
# merge master dataframe and muse into new master dataframe
print()
print("Merging merged dataframe with Project Muse dataframe.")
master_merge_df = merge_dataframe(master_merge_df, muse_df)

# merge master dataframe with titles dataframe so that only relevant publications are kept
print()
print("Merging merged dataframe with matched titles dataframe.")
titles_df.columns = ['title', 'oapen title', 'jstor title', 'muse title']
master_merge_df = pd.merge(titles_df, master_merge_df, on='title', how='left')

# remove obsolete columns (i.e. oapen, jstor, and muse titles)
print()
print("Removing obsolete columns.")
master_merge_df = master_merge_df[['title', 'country', 'total']]

# write last year's master merge dataframe to excel
print()
print("Writing last year's merged output to a backup excel file.")
master_merge_prev_file_path = os.path.join(path_input_output, "rd_master_merge_last_year.xlsx")
master_prev_df.to_excel(master_merge_prev_file_path, index=False)

# remove the merged country code column from the master merge dataframe of last year
print()
print("Removing the merged column of the master merge of last year.")
master_prev_df = master_prev_df[['title', 'country', 'total']]

# merge the new master dataframe with the master dataframe of last year
print()
print("Merging with last year's data.")
master_merge_df = merge_dataframe(master_merge_df, master_prev_df)

# concatenate the country codes and totals to the required format for the website
print()
print("Concatenating country codes and totals into required format for website.")
master_merge_df["merge"] = master_merge_df["country"].astype(str) + ":" + master_merge_df["total"].astype(int).astype(str) + ","

# write master merge dataframe to excel
print()
print("Writing merged dataframe to an excel file.")
master_merge_file_path = os.path.join(path_input_output, "rd_master_merge.xlsx")
master_merge_df.to_excel(master_merge_file_path, index=False)

print(f"""
      
Script completed.
      
The merged readership data were written to: \n{master_merge_file_path}.

Make sure to filter out "UNKNOWN", "EU-ignore", blanks, and "0" values from the "country" column when copying to the website.
      
      """)
input("Press Enter to close. \n")