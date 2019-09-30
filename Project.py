#!/usr/bin/env python
# coding: utf-8

# In[75]:


# All the file imports
get_ipython().system('pip install prettytable')
from datetime import datetime
from prettytable import PrettyTable


# In[76]:


def isDateParent(A):
    return A[1] in tag_fam["DATE"]


# In[77]:


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


# In[78]:


# Convert input date to standard format
# :param date array in input
def convert_date(date_arr):
    return "{}-{}-{}".format(date_arr[2], month_to_num(date_arr[1]), date_arr[0])


# In[79]:


# Determine age based on birthdate and death date
# If death date is not present then function uses the current date as a comparison
def determine_age(birth_date, death_date):
    birth_month= birth_date.split('-')[1]
    birth_day= birth_date.split('-')[0]
    
    if death_date:
        death_month=death_date.split('-')[1]
        death_day=death_date.split('-')[0]
        return int(death_date.split('-')[0]) - int(birth_date.split('-')[0])-((int(death_month), int(death_day))< (int(birth_month), int(birth_day)))
    else:
        today = datetime.today()
        return today.year - int(birth_date.split('-')[0]) - ((today.month, today.day) < (int(birth_month), int(birth_day)))


# In[80]:


def find_name(arr, _id):
    #takes array of dict objects
    for indi in arr:
        if _id == indi["INDI"]:
            return indi["NAME"]


# In[81]:


# create dictionary entry for the passed tag
# :param current_arr is the current array line being processed
# :param tag can will be either FAM or INDI
def create_dic_entry(current_arr, tag):
    current_tag=tag
    dic={}
    dic[tag]=current_arr[1]
    return dic, current_tag


# In[82]:


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


# In[83]:


# Checking if one date is after another
# :param date_one is the date being compared with
# :param date_two is the date being compared t0
def is_date_after(date_one, date_two):
    return date_one < date_two


# In[84]:


# Create map of individuals where key is the individual id and
# individual object is the  value
def create_individuals_map():
    global individuals
    individuals = {}
    for individual in document["INDI"]:
        individuals[individual["INDI"]] = individual


# In[85]:


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
            


# In[86]:


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
                  


# In[87]:


#User_Story_29: List all deceased individuals in a GEDCOM file
#Prints out a table with all the deceased people's information
def listDeceased():
    current_dic = {}
    print("User_Story_29: List all deceased individuals in a GEDCOM file")
    for value in individuals.values():
        if(str(value["DEAT"]) != "NA" and (value["ALIVE"])):
            error_array.append(("ERROR: INDIVIDUAL: US29 Person {} is alive but has Death Date {}").format(value["NAME"], value["DEAT"]))
        elif(str(value["DEAT"]) == "NA" and (not value["ALIVE"])):
            error_array.append(("ERROR: INDIVIDUAL: US29 Person {} is dead but has no Death Date").format(value["DEAT"]));
            print(("ERROR: INDIVIDUAL: US29 Person {} is dead but has no Death Date").format(value["DEAT"]))
        elif(not value["ALIVE"]):
            current_dic[value["INDI"]] = value
            
            
    #Use pretty table module to print out the results
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    printTable(allFields, tagNames, current_dic)


# In[88]:


#User_Story_30: List all living married people in a GEDCOM file
#Prints out a table with all the living married people's information
def listLivingMarried():
    current_dic = {}
    print("User_Story_30: List all living married people in a GEDCOM file")
    for value in individuals.values():
        if(value["ALIVE"] and value["SPOUSE"] != "NA"):
            current_dic[value["INDI"]] = value
        elif(not value["ALIVE"] and value["SPOUSE"] != "NA"):
            error_array.append("ERROR: INDIVIDUAL: US30 Deceased Person {} who is Married to {}".format(value["INDI"], "".join(value["SPOUSE"])))
    #Use pretty table module to print out the results
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
    printTable(allFields, tagNames, current_dic)


# In[89]:


# USID: 07
def is_marriage_legal():
    for family_id in family_dic:
        if "MARR" in family_dic[family_id] and family_dic[family_id]["MARR"]!="NA":
            married_date=family_dic[family_id]["MARR"]
        if "husband_object" in family_dic[family_id]:
            husband=family_dic[family_id]["husband_object"]
            if int(determine_age(husband["BIRT"], married_date)) < 14:
                print("ANOMOLY: INDIVIDUAL: US07: {}: Father {} of family {} is younger than 14.".format(husband["INDI"], husband["NAME"], family_id))
        if "wife_object" in family_dic[family_id]:
            wife=family_dic[family_id]["wife_object"]
            if int(determine_age(wife["BIRT"], married_date)) < 14:
                print("ANOMOLY: INDIVIDUAL: US07: {}: Wife {} of family {} is younger than 14.".format(wife["INDI"], wife["NAME"], family_id))


# In[90]:


#USID: 10
def is_age_legal():
    for indi_id in individuals:
        if "AGE" in individuals[indi_id]:
            age =individuals[indi_id]["AGE"]
            if int(age) > 150:
                print("ANOMOLY: INDIVIDUAL: US10: {}: Individual {} is older than 150.".format(indi_id, individuals[indi_id]["NAME"]))


# In[91]:


#User_Story_29: List all deceased individuals in a GEDCOM file
#Prints out a table with all the deceased people's information
def listDeceased():
    current_dic = {}
    print("User_Story_29: List all deceased individuals in a GEDCOM file")
    for value in individuals.values():
        if(str(value["DEAT"]) != "NA" and (value["ALIVE"])):
            error_array.append(("ERROR: INDIVIDUAL: US29 Person {} is alive but has Death Date {}").format(value["NAME"], value["DEAT"]))
            #print(("ERROR: INDIVIDUAL: US29 Person {} is alive but has Death Date {}").format(value["NAME"], value["DEAT"]))
        elif(str(value["DEAT"]) == "NA" and (not value["ALIVE"])):
            error_array.append(("ERROR: INDIVIDUAL: US29 Person {} is dead but has no Death Date").format(value["DEAT"]));
            #print(("ERROR: INDIVIDUAL: US29 Person {} is dead but has no Death Date").format(value["INDI"]))
        elif(not value["ALIVE"]):
            current_dic[value["INDI"]] = value
            
            
    #Use pretty table module to print out the results
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    printTable(allFields, tagNames, current_dic)


# In[92]:


#User_Story_30: List all living married people in a GEDCOM file
#Prints out a table with all the living married people's information
def listLivingMarried():
    current_dic = {}
    print("User_Story_30: List all living married people in a GEDCOM file")
    for value in individuals.values():
        if(value["ALIVE"] and value["SPOUSE"] != "NA"):
            current_dic[value["INDI"]] = value
        elif(not value["ALIVE"] and value["SPOUSE"] != "NA"):
            error_array.append("ERROR: INDIVIDUAL: US30 Deceased Person {} who is Married to {}".format(value["INDI"], "".join(value["SPOUSE"])))
            #print("ERROR: INDIVIDUAL: US30 Deceased Person {} who is Married to {}".format(value["INDI"], "".join(value["SPOUSE"])))
    #Use pretty table module to print out the results
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
    printTable(allFields, tagNames, current_dic)


# In[93]:


# Prints out the Individual Table
def printIndividualTable():
    print("People")
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "INDI_CHILD", "SPOUSE"]
    
    printTable(allFields, tagNames, individuals)


# In[94]:


# Prints out the Family Table
def printFamilyTable():
    print("Families")
    allFields = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    tagNames = ["FAM", "MARR", "DIV", "HUSB", "HUSB_NAME", "WIFE", "WIFE_NAME", "FAM_CHILD"]
    
    printTable(allFields, tagNames, family_dic)


# In[95]:


# Prints out the data in both error and anomaly arrays
def printError():
    if (len(error_array) > 0):
        print("------error messages------")
        for error in error_array:
            print(error)
    if(len(anomaly_array) > 0):
        print("-----anomaly messages-----")
        for anomaly in anomaly_array:
            print(anomaly)


# In[96]:


# Prints out a table of dictionary data with the passed-in arguments
# Parameters:
# fields: a list of fields for the table
# tag_names: tag names used to access each data field
# dictionary: a dictionary filled with data
def printTable(fields, tag_names, dictionary):
    table = PrettyTable()
    table.field_names = fields
    for element in dictionary.values():    
        count = 1
        row_data = "" #string uses to store each tag within the current element
        for name in tag_names:
            if (count < int(len(tag_names))): #not the last element
                if (isinstance(element[name], list)): #current element is an array
                    row_data += ("".join(element[name]) + "? ")
                else: #current element is not an array
                    row_data += (str(element[name]) + "? ")
            elif (count == int(len(tag_names))):
                if (isinstance(element[name], list)): #current element is an array
                    row_data += ("".join(element[name]))
                else: #current element is not an array
                    row_data += (str(element[name]))
                break
            count+= 1;
        table.add_row(row_data.split('?'))
    print(table)


# In[97]:


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
error_array=[]
anomaly_array=[]


# In[98]:


document = read_in("./myTest.ged")
create_individuals_map()
create_family_dic()
# Prints out all the people in GEDCOM file
printIndividualTable()
# Prints out all the families in GEDCO file
printFamilyTable()
#User_Story_29
listDeceased()
#User_Story_30
listLivingMarried()

is_marriage_legal()
is_age_legal()
listDeceased()
listLivingMarried()
# Prints out all the errors and anomalies of each function
printError()


# In[ ]:




