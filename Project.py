#!/usr/bin/env python
# coding: utf-8

# In[112]:


#Data Structure 
tag_sp=["INDI", "FAM"]
#Level Zero Tags
tag_zero=["HEAD", "TRLR", "NOTE"]
#Level One Tags
tag_one=["NAME", "SEX", "BIRT", "DEAT","FAMC","FAMS","MARR", "DIV","HUSB","WIFE","CHIL"]
#Level Zero Tags
tag_fam={"INDI":["NAME", "SEX","BIRT", "DEAT","FAMC","FAMS"],
             "FAM":["MARR", "DIV","HUSB","WIFE","CHIL"], 
             "DATE":["BIRT", "DEAT", "DIV", "MARR"]}
family_dic=None
individuals=None


# In[113]:


def isDateParent(A):
    return A[1] in tag_fam["DATE"]


# In[114]:


# Convert month string to month number
# :param month for which we need the number
def month_to_num(shortMonth):
    return{
        'JAN' : "1",
        'FEB' : "2",
        'MAR' : "3",
        'APR' : "4",
        'MAY' : "5",
        'JUN' : "6",
        'JUL' : "7",
        'AUG' : "8",
        'SEP' : "9", 
        'OCT' : "10",
        'NOV' : "11",
        'DEC' : "12"
    }[shortMonth]


# In[115]:


# Convert input date to standard format
# :param date array in input
def convert_date(date_arr):
    return "{}-{}-{}".format(date_arr[2], month_to_num(date_arr[1]), date_arr[0])


# In[116]:


from datetime import datetime

# Determine age based on birthdate and death date
# If death date is not present then function uses the current date as a comparison
def determine_age(birth_date, death_date):
    if death_date:
        return int(death_date.split('-')[0]) - int(birth_date.split('-')[0])
    else:
        today = datetime.today()
        return today.year - int(birth_date.split('-')[0])


# In[117]:


def find_name(arr, _id):
    #takes array of dict objects
    for indi in arr:
        if _id == indi["INDI"]:
            return indi["NAME"]


# In[118]:


# Returns the lastname of the name
# Last name is surrounded by '/' in the name
# :param name is the full name of the person
def get_last_name(name):
    return name.split('/')[1];


# In[119]:


# create dictionary entry for the passed tag
# :param current_arr is the current array line being processed
# :param tag can will be either FAM or INDI
def create_dic_entry(current_arr, tag):
    current_tag=tag
    dic={}
    dic[tag]=current_arr[1]
    return dic, current_tag


# In[120]:


# Adds missing tags with "NA"
def add_missing_entries(dic):
    if "DIV" not in dic:
        dic["DIV"] = "NA"
    if "HUSB" not in dic:
        dic["HUSB"] = "NA"
    if "HUSB_NAME" not in dic:
        dic["HUSB_NAME"] = "NA"
    if "WIFE" not in dic:
        dic["WIFE"] = "NA"
    if "WIFE_NAME" not in dic:
        dic["WIFE_NAME"] = "NA"
    if "FAM_CHILD" not in dic:
        dic["FAM_CHILD"] = "NA"
    if "MARR" not in dic:
        dic["MARR"] = "NA"   


# In[121]:


# Checking if one date is after another
# :param date_one is the date being compared with
# :param date_two is the date being compared t0
def is_date_after(date_one, date_two):
    return date_one < date_two


# In[122]:


# Create map of individuals where key is the individual id and
# individual object is the  value
def create_individuals_map():
    global individuals
    individuals = {}
    for individual in document["INDI"]:
        individuals[individual["INDI"]] = individual


# In[123]:


# Creating a family dictionary with the key as the family id and the value as the
# information about the family and the objects corresponding to husband, wife and children
def create_family_dic():
    global family_dic
    family_dic = {}
    for family in document["FAM"]:
        if family["HUSB"] != "NA" and family["HUSB"] in individuals:
            family["husband_object"] = individuals[family["HUSB"]]
        if family["WIFE"] != "NA" and family["WIFE"] in individuals:
            family["wife_object"] = individuals[family["WIFE"]]
        if family["FAM_CHILD"] != "NA":
            children = []
            for child in family["FAM_CHILD"]:
                children.append(individuals[child])
            family["children_objects"] = children
        family_dic[family["FAM"]] = family
            


# In[124]:


# User story: US16
# This function goes over the family dictionary and 
# returns the array of family ids which contain males with different last name
# It uses the last name of the husband in the family as the initial reference
# 
# :returns array of family ids
def check_last_names():
    for family_id in family_dic:
        family = family_dic[family_id]
        last_name = None
        if "HUSB_NAME" in family:
            last_name = get_last_name(family["HUSB_NAME"])
        for child in family["children_objects"]:
            if child["SEX"] == "M":
                if last_name is None:
                    last_name = get_last_name(child["NAME"])
                else:
                    if last_name != get_last_name(child["NAME"]):
                        print("ANOMOLY: INDIVIDUAL: US16: {}: Individual has different last name {} than family {}"                                   .format(child["INDI"], get_last_name(child["NAME"]), last_name))


# In[125]:


# User Story: US15
def check_sibling_count():
    for family_id in family_dic:
        family = family_dic[family_id]
        if (len(family["FAM_CHILD"]) > 15):
           print("ANOMOLY: FAMILY: US16: {}: Family has {} siblings which is more than 15 siblings".format(family_id, len(family["FAM_CHILD"])))


# In[126]:


def read_in(file):
    doc={"INDI":[], "FAM":[]}
    dic={}
    flag=False #indicates whether the correct tag has appeared before DATE tag
    with open(file) as f:
        all_lines=f.readlines()
        for line, next_line in zip(all_lines, all_lines[1:]):
            current_arr=line.strip().split(" ")
            next_arr=next_line.strip().split(" ")
            #if the current tag is individual
            if len(current_arr)==3 and current_arr[0]=='0' and current_arr[2]== "INDI":
                #inserts individual's ID into the dictionary
                dic, current_tag=create_dic_entry(current_arr, "INDI") 
            elif len(current_arr)==3 and current_arr[0]=='0' and current_arr[2]=="FAM": 
                dic, current_tag=create_dic_entry(current_arr, "FAM")
            elif (current_arr[1]=="DATE" and flag):
                flag=False
                date_arr = current_arr[2:] #extracts the date argument from the line
                dic[tmp]= convert_date(date_arr) #converts the date into correct format
            elif current_arr[0]=='1' and current_arr[1] in tag_one:
                if (isDateParent(current_arr)): #determines whether the current tag is parent of DATE tag
                    tmp=current_arr[1] #extracts the tag name
                    flag=True
                else: 
                    #current tag is not the parent tag of DATE tag
                    if current_arr[1] == "HUSB":
                        dic["HUSB_NAME"]=find_name(doc["INDI"], current_arr[2])
                    if current_arr[1] == "WIFE":
                        dic["WIFE_NAME"]=find_name(doc["INDI"], current_arr[2])
                    if current_arr[1] == 'CHIL':
                        #INDI_CHILD indicates all the children within a family
                        children = dic["FAM_CHILD"] if "FAM_CHILD" in dic else []
                        children.append(current_arr[2])
                        dic["FAM_CHILD"] = children
                    if current_arr[1] == 'FAMC' or current_arr[1] == 'FAMS':
                        child = dic["INDI_CHILD"] if "INDI_CHILD" in dic else []
                        spouse = dic["SPOUSE"] if "SPOUSE" in dic else []
                        child.append(current_arr[2]) if current_arr[1] == 'FAMC' else spouse.append(current_arr[2])
                        dic['INDI_CHILD'] = child #FAM_CHILD indicates which family this individual belongs to
                        dic['SPOUSE'] = spouse
                    else: #other type of tag
                        dic[current_arr[1]]=' '.join(current_arr[2:])
            if (len(next_arr)==3 and next_arr[0]=='0' and next_arr[2] in tag_sp) or next_arr[1]=="TRLR":
                if dic:
                    if current_tag == 'INDI':
                        if 'DEAT' in dic:
                            age = determine_age(dic['BIRT'], dic['DEAT'])
                            alive = False
                        else:
                            age = determine_age(dic['BIRT'], None)
                            alive = True
                            dic['DEAT'] = 'NA'
                        dic["AGE"] = str(age)
                        dic['ALIVE']= alive
                        #print(current_tag
                        if not dic["SPOUSE"]:
                            dic["SPOUSE"] = "NA"
                        elif not dic["INDI_CHILD"]:
                            dic["INDI_CHILD"] = "NA"
                    if current_tag == 'FAM':
                        add_missing_entries(dic)
                    doc[current_tag].append(dic)
        return doc
                  


# In[127]:


# Uses the prettyTable module and print out the passed-in dictionary data
# :param fields the table column title
# :param tag_names the tag names used to access the dictionary elements
# :param dictionary the dictionary with the data needed to be printed
def printTable(fields, tag_names, dictionary):
    table = PrettyTable()
    table.field_names = fields
    for element in dictionary.values():    
        count = 1
        row_data = "" #string uses to store each tag within the current element
        for name in tag_names:
            if (count < int(len(tag_names))): #not the last element
                row_data += (str(element[name]) + ", ")
            elif (count == int(len(tag_names))): #last element
                row_data += str(element[name])
                break
            count+= 1;
        table.add_row(row_data.split(','))
    print(table)


# In[128]:


document = read_in("./myTest.ged")
create_individuals_map()
create_family_dic()
check_last_names()
check_sibling_count()


# In[129]:


from prettytable import PrettyTable

for family in document["FAM"]:
    husband=family["HUSB"] if "HUSB" in family else []
    
    
indi_table = PrettyTable() #individual table
indi_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
fam_table = PrettyTable() #family table
fam_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
for individual in document["INDI"]:
    indi_table.add_row([individual["INDI"], individual["NAME"], individual["SEX"], individual["BIRT"], individual["AGE"], 
                       individual["ALIVE"], individual["DEAT"], ("".join(individual["INDI_CHILD"])), ("".join(individual["SPOUSE"]))])
    
for family in document["FAM"]:
    fam_table.add_row([family["FAM"], family["MARR"], family["DIV"], family["HUSB"], family["HUSB_NAME"], family["WIFE"], family["WIFE_NAME"], ("".join(family["FAM_CHILD"]))])
    
print(indi_table)
print(fam_table)


# In[ ]:




