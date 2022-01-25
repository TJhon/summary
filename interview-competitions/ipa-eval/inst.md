

# Replacement Workflow/Basic Data Cleaning

Files: hh_round1.dta
Instructions: hh_round1.dta is the new wave of data collection that you have just received. There are a few issues with the data that you need to resolve before running checks. 
1.	Variables read and write need to be in numeric format. Replace these variables with a numeric variable.
2.	What percent of respondents have a female head of household?
3.	Recode head_gender so that female = 0. Adjust the value label as well.
4.	After talking to your team leaders, you learn that an enumerator made a few mistakes when entering in the data. They send you an email with these changes:
a.	For hhid 15064, the household head gender should be female.
b.	For hhid 29038, the household head education should be none.
c.	For hhid 53024, the number of members who can read should be 3. 
5.	Change the label of the variable “hhid” to “Household ID”. 
6.	Rename the variable “size” to “hh_size”. 
7.	The Principal Investigator wants to see if there is a relationship between household head gender and household size. Find the average household size by household head gender. 
8.	Save this new dataset as “hh_round1_clean.dta”.

# Import and Export Excel

Files: round2.xlsx
Instructions: A new round of data collection has just been sent to you. Import the data into Stata and export an excel document with two sheets using Stata: one that contains a list of responses with duplicate household IDs (hhid) and another that contains a list of enumerators that recorded duplicate IDs and how many duplicates each enumerator had.

# Survey Design Reconciliation

Files: hh_nr_round1.dta, hh_round1.dta 
The survey data for the Northern region of the survey area used a different variable format in the agriculture module. All respondents in both areas were asked if they grew the following crops, or if they grew any other crop:
1.	Rice
2.	Cassava
3.	Millet
4.	Groundnut
5.	Sweet Potato
6.	Wheat
7.	Sorghum
Please combine these datasets in a consistent manner. The affected variables are crop_l1 through crop_l9 in the hh_round1.dta file and crop_l in hh_nr_round1.dta file.
Note: The hh_nr_round1.dta has been cleaned by another RA and may not be fully clean. In addition, please provide justifications for any decisions you need to make about the data to perform the task. 
