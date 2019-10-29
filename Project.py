#!/usr/bin/env python
# coding: utf-8

# In[1]:


# All the file imports
get_ipython().system('pip install prettytable')
from datetime import datetime
from prettytable import PrettyTable
import os


# In[2]:


def isDateParent(A):
    return A[1] in tag_fam["DATE"]


# In[3]:


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


# In[4]:


# Convert input date to standard format
# :param date array in input
def convert_date(date_arr):
    return "{}-{}-{}".format(date_arr[2], month_to_num(date_arr[1]), date_arr[0])


# In[5]:


# Determine age based on birthdate and death date
# If death date is not present then function uses the current date as a comparison
def determine_age(birth_date, death_date):
    birth_month= birth_date.split('-')[1]
    birth_day= birth_date.split('-')[2]
    
    if death_date:
        death_month=death_date.split('-')[1]
        death_day=death_date.split('-')[2]
        return int(death_date.split('-')[0]) - int(birth_date.split('-')[0])-((int(death_month), int(death_day))< (int(birth_month), int(birth_day)))
    else:
        today = datetime.today()
        return today.year - int(birth_date.split('-')[0]) - ((today.month, today.day) < (int(birth_month), int(birth_day)))


# In[6]:


# Determine days difference
# For US 08 and 09
def determine_days(date1, date2):
    year1=int(date1.split('-')[0])
    month1= int(date1.split('-')[1])
    day1= int(date1.split('-')[2])
    
    year2=int(date2.split('-')[0])
    month2= int(date2.split('-')[1])
    day2= int(date2.split('-')[2])
    
    return (year2 - year1) * 365 + (month2 - month1)* 30 + day2- day1


# In[7]:


def find_name(arr, _id):
    #takes array of dict objects
    for indi in arr:
        if _id == indi["INDI"]:
            return indi["NAME"]


# In[8]:


# create dictionary entry for the passed tag
# :param current_arr is the current array line being processed
# :param tag can will be either FAM or INDI
def create_dic_entry(current_arr, tag):
    current_tag=tag
    dic={}
    dic[tag]=current_arr[1]
    return dic, current_tag


# In[9]:


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


# In[10]:


# Checking if one date is after another
# :param date_one is the date being compared with
# :param date_two is the date being compared t0
def is_date_after(date_one, date_two):
    return date_one < date_two


# In[11]:


# Create map of individuals where key is the individual id and
# individual object is the  value
def create_individuals_map():
    global individuals
    individuals = {}
    for individual in document["INDI"]:
        individuals[individual["INDI"]] = individual


# In[12]:


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
            


# In[13]:


# Reads the input GEDCOM file line by line and store the data into the dictionary
def read_in(file):
    doc={"INDI":[], "FAM":[]}
    dic={}
    global ui
    ui=[]
    global uf
    uf=[]
    temp = ""
    flag=False #indicates whether the correct tag has appeared before DATE tag
    with open(file) as f:
        all_lines=f.readlines()
        line_num = 1; #line number of each 
        for line, next_line in zip(all_lines, all_lines[1:]):
            current_arr=line.strip().split(" ")
            next_arr=next_line.strip().split(" ")
            #if the current tag is individual
            if (len(current_arr)==3 and current_arr[0]=='0' and current_arr[2]== "INDI"):
                temp = current_arr[1]
                unique_indi_and_family(temp, "INDI", line_num)
                #inserts individual's ID into the dictionary
                dic, current_tag=create_dic_entry(current_arr, "INDI") 
                #inserts line number
                dic["INDI_LINE"] = line_num
            #if the current tag is family
            elif len(current_arr)==3 and current_arr[0]=='0' and current_arr[2]=="FAM": 
                temp = current_arr[1]
                unique_indi_and_family(temp, "FAM", line_num)
                dic, current_tag=create_dic_entry(current_arr, "FAM")
                #inserts line number
                dic["FAM_LINE"] = line_num
            #if the current tag is date
            elif current_arr[1]=="DATE" and flag:
                flag=False
                date_arr = current_arr[2:] #extracts the date argument from the line
                dic[tmp]= convert_date(date_arr) #converts the date into correct format
            #determines if the tag level is correct
            elif current_arr[0]=='1' and current_arr[1] in tag_one:
            #"NAME", "SEX", "BIRT", "DEAT","FAMC","FAMS","MARR", "DIV","HUSB","WIFE","CHIL"
                if (isDateParent(current_arr)): #determines whether the current tag is parent of DATE tag
                    tmp=current_arr[1] #extracts the tag name
                    flag=True
                    #inserts line number
                    dic[tmp + "_LINE"] = line_num
                else: 
                    #current tag is not the parent tag of DATE tag
                    if current_arr[1] == "HUSB":
                        dic["HUSB_NAME"]=find_name(doc["INDI"], current_arr[2])
                        #inserts line number
                        dic["HUSB_LINE"] = line_num
                    if current_arr[1] == "WIFE":
                        dic["WIFE_NAME"]=find_name(doc["INDI"], current_arr[2])
                        #inserts line number
                        dic["WIFE_LINE"] = line_num
                    if current_arr[1] == 'CHIL':
                        #INDI_CHILD indicates all the children within a family
                        children = dic["FAM_CHILD"] if "FAM_CHILD" in dic else []
                        children.append(current_arr[2])
                        dic["FAM_CHILD"] = children
                        #inserts line number
                        dic["CHIL_LINE_" + current_arr[2]] = line_num
                    if current_arr[1] == 'FAMC' or current_arr[1] == 'FAMS':
                        child = dic["INDI_CHILD"] if "INDI_CHILD" in dic else []
                        spouse = dic["SPOUSE"] if "SPOUSE" in dic else []
                        child.append(current_arr[2]) if current_arr[1] == 'FAMC' else spouse.append(current_arr[2])
                        dic['INDI_CHILD'] = child #FAM_CHILD indicates which family this individual belongs to
                        dic['SPOUSE'] = spouse
                        #inserts line number
                        dic[current_arr[1] + "_LINE"] = line_num
                    else: #other type of tag
                        dic[current_arr[1]]=' '.join(current_arr[2:])
                        #inserts line number
                        dic[current_arr[1] + "_LINE"] = line_num
            #TRLR ==> end of the GEDCOM file
            if (len(next_arr)==3 and next_arr[0]=='0' and next_arr[2] in tag_sp) or next_arr[1]=="TRLR":
                if dic: #if the dic exists or not
                    if current_tag == 'INDI': #under individual tag?
                        if 'DEAT' in dic:
                            age = determine_age(dic['BIRT'], dic['DEAT'])
                            alive = False
                        else:
                            age = determine_age(dic['BIRT'], None)
                            alive = True
                            dic['DEAT'] = "NA"
                        dic["AGE"] = str(age)
                        dic['ALIVE']= alive
                        if not dic["SPOUSE"]:
                            dic["SPOUSE"] = "NA"
                        elif not dic["INDI_CHILD"]:
                            dic["INDI_CHILD"] = "NA"
                    if current_tag == 'FAM':
                        add_missing_entries(dic)
                    doc[current_tag].append(dic) 
            line_num += 1 #increments the line counter by 
        return doc
                  


# In[14]:


# USID: 01
# The Dates we need to check includes: birth, marriage, divorce, death
# Birth always exists, the rests we need to check for NA
# Iteration through individuals and family
def validate_dates():
    for family in family_dic.values():
        if family["MARR"] !="NA":
            if(determine_age(family["MARR"], None) < 0):
                 error_array.append("ERROR: FAMILY: US01: {}: {}: Family has marrige date {} later than today".format(family["MARR_LINE"], family["FAM"], family["MARR"]))
        if family["DIV"] != "NA":
            if(determine_age(family["DIV"], None) < 0):
                 error_array.append("ERROR: FAMILY: US01: {}: {}: Family has divorce date {} later than today".format(family["DIV_LINE"], family["FAM"], family["DIV"]))     
    
    for indi in individuals.values():
        # for birthday simply check age
        if(determine_age(indi["BIRT"], None) < 0):
                error_array.append("ERROR: INDIVIDUAL: US01: {}: {}: Individual has birth date {} later than today".format(indi["BIRT_LINE"], indi["INDI"], indi["BIRT"]))     
        if indi["DEAT"] != "NA":
            if(determine_age(indi["DEAT"], None) < 0):
                error_array.append("ERROR: INDIVIDUAL: US01: {}: {}: Individual has death date {} later than today".format(indi["DEAT_LINE"], indi["INDI"], indi["DEAT"]))


# In[15]:


#USID: 02
#
# This function checks if the birth of the person is before their 
# marriage date
# If birth of the person is after the marriage date then the error
# is appended to the error array
def is_birth_before_marraige():
    for family_id in family_dic:
        family = family_dic[family_id]
        if "MARR" in family:
            marriage_date = family["MARR"];
            husband_birth_date = None;
            wife_birth_date = None;
            if "husband_object" in family and "BIRT" in family["husband_object"]:
                husband_birth_date = family["husband_object"]["BIRT"]
            else:
                continue;
            if "wife_object" in family and "BIRT" in family["wife_object"]:
                wife_birth_date = family["wife_object"]["BIRT"]
            else:
                continue;
            if is_date_after(marriage_date, husband_birth_date):
                error_array.append(("ERROR: INDIVIDUAL: US02: {}: {}: Person has marriage date {} before birth date {}")                                    .format(family['MARR_LINE'], family["husband_object"]["INDI"], marriage_date, husband_birth_date))
            if is_date_after(marriage_date, wife_birth_date):
                 error_array.append(("ERROR: INDIVIDUAL: US02: {}: {}: Person has marriage date {} before birth date {}")                                    .format(family['MARR_LINE'], family["wife_object"]["INDI"], marriage_date, wife_birth_date))


# In[16]:


# US04 - Marriage Before Divorce

def is_marriage_after_divorce():
    # Iterating through all individuals
    for currentIndividual in individuals.values():
        # Ignoring all individuals who weren't ever married
        if(currentIndividual['SPOUSE'] != 'NA'):
            # Iterating through all the families they were related to
            for currentFamily in currentIndividual['SPOUSE']:
                for checkingFamily in family_dic.values():
                    if(checkingFamily['FAM'] == currentFamily):
                        # Ignoring all the marriages without a divorce
                        if(checkingFamily['DIV'] != 'NA'):
                            # Checking if a divorce date is before a marriage date
                            if(checkingFamily['MARR'] > checkingFamily['DIV']):
                                anomaly_array.append("ANOMALY: INDIVIDUAL: US04: {}: {}: Marriage Before Divorce - Marriage Date {} - Divorce Date {}".format(checkingFamily["MARR_LINE"], currentIndividual['INDI'], checkingFamily['MARR'], checkingFamily['DIV']))


# In[17]:


# US05 - Marriage Before Death

def is_marriage_after_death():
    # Iterating through all individuals
    for currentIndividual in individuals.values():
        # Ignoring all individuals who weren't ever married
        if(currentIndividual['SPOUSE'] != 'NA'):
            # Iterating through all the families they were related to
            for currentFamily in currentIndividual['SPOUSE']:
                for checkingFamily in family_dic.values():
                    if(checkingFamily['FAM'] == currentFamily):
                        if(checkingFamily['MARR'] != 'NA'):
                            if(checkingFamily['MARR'] > currentIndividual['DEAT']):
                                anomaly_array.append("ANOMALY: INDIVIDUAL: US05: {}: {}: Marriage Before Death - Marriage Date {} - Death Date {}".format(checkingFamily["MARR_LINE"], currentIndividual['INDI'], checkingFamily['MARR'], currentIndividual['DEAT']))


# In[18]:


#USID: 06
def check_divorce_before_death():
     for family in family_dic.values():
            husband_flag=False
            wife_flag=False
            if "DIV" in family and family["DIV"]!="NA":
                divorce_date = family["DIV"]
                if "husband_object" in family and family["husband_object"] != 'NA':
                    husband=family["husband_object"]
                    if "DEAT" in husband and husband["DEAT"] != 'NA':
                        husband_flag=True
                        husband_death=husband["DEAT"]
                if "wife_object" in family and family["wife_object"] != 'NA':
                    wife=family["wife_object"]
                    if "DEAT" in wife and wife["DEAT"] != 'NA':
                        wife_flag=True
                        wife_death=wife["DEAT"]
                if husband_flag and wife_flag:
                    husband_invalid = False
                    wife_invalid = False
                    if determine_days(husband_death, divorce_date) < 0:
                        husband_invalid = True
                    if determine_days(wife_death, divorce_date) < 0:
                        wife_invalid = True
                    if husband_invalid and wife_invalid:
                        error_array.append("ERROR: FAMILY: US06: {}: {}: Divorce {} happened after the death of both spouses - Husband: {} Wife: {}.".format(family["DIV_LINE"], family["FAM"], family["DIV"], husband_death, wife_death))
                    elif husband_invalid:
                        error_array.append("ERROR: FAMILY: US06: {}: {}: Divorce {} happened after the death of father {}.".format(family["DIV_LINE"], family["FAM"], family["DIV"], husband_death, wife_death))
                    elif wife_invalid:
                        error_array.append("ERROR: FAMILY: US06: {}: {}: Divorce {} happened after the death of wife {}.".format(family["DIV_LINE"], family["FAM"], family["DIV"], husband_death, wife_death))
                        


# In[19]:


#USID: 07
def is_age_legal():
    for indi_id in individuals:
        indi=individuals[indi_id]
        if "AGE" in indi:
            age =indi["AGE"]
            if int(age) > 150:
                if indi["ALIVE"]:
                    anomaly_array.append("ANOMALY: INDIVIDUAL: US07: {}: {}: More than 150 years old - Birth Date {}".format(indi["BIRT_LINE"], indi_id, indi["BIRT"]))
                else:
                    anomaly_array.append("ANOMALY: INDIVIDUAL: US07: {}: {}: More than 150 years old at death - Birth Date {}: Death Date {}".format(indi["BIRT_LINE"], indi_id, indi["BIRT"], indi["DEAT"]))


# In[20]:


#Birth before marriage of parents USID: 08
def birth_before_marriage():
    for family in family_dic.values():
        if "children_objects" in family:
            marriage_date=family['MARR']
            divorce_date=family["DIV"]
            for child in family["children_objects"]:
                if(marriage_date!= "NA"):
                    if(determine_days(marriage_date, child["BIRT"]) < 0):
                         anomaly_array.append("ANOMALY: INDIVIDUAL: US08: {}: {}: Child was born at {} before marriage of parents {}".format(child["BIRT_LINE"], child["INDI"], child["BIRT"], marriage_date))
                if(divorce_date!= "NA"):
                    if(determine_days(divorce_date, child["BIRT"])/30 > 9):
                         anomaly_array.append("ANOMALY: INDIVIDUAL: US08: {}: {}: Child was born at {} after 9 month divorce of parents {}".format(child["BIRT_LINE"], child["INDI"], child["BIRT"], divorce_date))


# In[21]:


#Birth before death of parents USID: 09
def birth_before_death():
    for family in family_dic.values():
        if "children_objects" in family:
            if "husband_object" in family:
                husband_death=family["husband_object"]["DEAT"]
            if "wife_object" in family:
                wife_death=family["wife_object"]["DEAT"]
            for child in family["children_objects"]:
                if(wife_death!= "NA"):
                    if(determine_days(child["BIRT"], wife_death) < 0):
                        error_array.append("ERROR: INDIVIDUAL: US09: {}: {}: Child was born at {} after death of mother {}".format(child["BIRT_LINE"], child["INDI"], child["BIRT"], wife_death))
                if(husband_death!= "NA"):
                    if(determine_days(husband_death, child["BIRT"])/30 > 9):
                        error_array.append("ERROR: INDIVIDUAL: US09: {}: {}: Child was born at {} after 9 month death of father {}".format(child["BIRT_LINE"], child["INDI"], child["BIRT"], husband_death))


# In[22]:


# USID: 10
def is_marriage_legal():
    for family_id in family_dic:
        if "MARR" in family_dic[family_id] and family_dic[family_id]["MARR"]!="NA":
            married_date=family_dic[family_id]["MARR"]
        if "husband_object" in family_dic[family_id]:
            husband=family_dic[family_id]["husband_object"]
            if int(determine_age(husband["BIRT"], married_date)) < 14:
                anomaly_array.append("ANOMALY: INDIVIDUAL: US10: {}: {}: Father of family {} is younger than 14 years old - Birth Date {}".format(husband["BIRT_LINE"], husband["INDI"], family_id,husband["BIRT"]))
        if "wife_object" in family_dic[family_id]:
            wife=family_dic[family_id]["wife_object"]
            if int(determine_age(wife["BIRT"], married_date)) < 14:
                anomaly_array.append("ANOMALY: INDIVIDUAL: US10: {}: {}: Wife of family {} is younger than 14 years old - Birth Date {}".format(wife["BIRT_LINE"], wife["INDI"], family_id, wife["BIRT"]))


# In[23]:


# USID: 11
def check_for_bigamy():
    for individual_id in individuals:
        individual = individuals[individual_id]
        if "SPOUSE" in individual and individual["SPOUSE"] != 'NA':
            spouse_in_families = individual["SPOUSE"]
            if len(spouse_in_families) > 1:
                dates = []
                for family_id in spouse_in_families:
                    family = family_dic[family_id]
                    date = {}
                    if "MARR" in family and family["MARR"] != 'NA':
                        date["MARR"] = family["MARR"]
                    if "DIV" in family and family["DIV"] != 'NA':
                        date["DIV"] = family["DIV"]
                    elif "husband_object" in family and family["husband_object"] != 'NA':
                        if "DEAT" in family["husband_object"] and family["husband_object"]["DEAT"] != 'NA':
                            date["DIV"] = family["husband_object"]["DEAT"]
                    dates.append(date)
                if compare_marraige_dates(dates):
                    anomaly_array.append("ANOMALY: INDIVIDUAL: US11: {}: {}: Performing bigamy".format(individual["INDI_LINE"], individual["INDI"]))


# In[24]:


# USID: 12
def check_parents_not_too_old():
    for family in family_dic.values():
        husband_flag=False
        wife_flag=False
        if "husband_object" in family and family["husband_object"] != 'NA':
            husband_age = family["husband_object"]["AGE"]
            husband_flag=True
        if "wife_object" in family and family["wife_object"] != 'NA':
            wife_age = family["wife_object"]["AGE"]
            wife_flag=True
        if "children_objects" in family and family["children_objects"] != 'NA':
            for child in family["children_objects"]:
                child_age = child["AGE"]
                husband_to_child = int(husband_age) - int(child_age)
                wife_to_child = int(wife_age) - int(child_age)
                if husband_flag and husband_to_child >= 80:
                    error_array.append("ERROR: INDIVIDUAL: US12: {}: {}: Father is {} older than the child {}."                                               .format(family["husband_object"]["INDI_LINE"], family["FAM"], husband_to_child, child["INDI"]))
                if wife_flag and wife_to_child >= 60:
                     error_array.append("ERROR: FAMILY: US12: {}: {}: Wife is {} older than the child {}."                                               .format(family["wife_object"]["INDI_LINE"], family["FAM"], wife_to_child, child["INDI"]))


# In[25]:


def compare_marraige_dates(dates):
    for i in range(0, len(dates)):
        dateOne = dates[i]
        for j in range(i + 1, len(dates)):
            dateTwo = dates[j]
            if "MARR" in dateOne and "DIV" in dateOne:
                if "MARR" in dateTwo:
                    if dateOne["MARR"] <= dateTwo["MARR"] < dateOne["DIV"]:
                        return True
                if "DIV" in dateTwo:
                    if dateOne["MARR"] < dateTwo["DIV"] < dateOne["DIV"]:
                        return True
            elif "MARR" in dateOne:
                if "MARR" in dateTwo and "DIV" in dateTwo:
                    if dateTwo["MARR"] <= dateOne["MARR"] < dateTwo["DIV"]:
                        return True
                if "MARR" in dateTwo and dateOne["MARR"] <= dateTwo["MARR"]:
                    return True
                if "DIV" in dateTwo and dateOne["MARR"] < dateTwo["DIV"]:
                    return True
                if "MARR" in dateTwo and "DIV" not in dateTwo and dateTwo["MARR"] <= dateOne["MARR"]:
                    return True
            elif "DIV" in dateOne:
                if "MARR" in dateTwo and "DIV" in dateTwo:
                    if dateTwo["MARR"] <= dateOne["DIV"] < dateTwo["DIV"]:
                        return True
    return False


# In[26]:


# US13
def check_sibling_spacing():
    for family_id in family_dic:
        family = family_dic[family_id]
        if (len(family["FAM_CHILD"]) > 0) and family["FAM_CHILD"] != "NA":
            for child in family["FAM_CHILD"]:
                siblings = get_individual_siblings(child, False, True)
                child_object = individuals[child]
                for sibling in siblings:
                    if sibling != child:
                        sibling_object = individuals[sibling]
                        days = determine_days(child_object["BIRT"], sibling_object["BIRT"])
                        days = abs(days)
                        if 2 < days < (8 * 30):
                            error_array.append("ERROR: INDIVIDUAL: US13: {}: Child {} is born within 8 months and more than 2 days of sibling"                                               .format(child_object["INDI_LINE"], child))


# In[27]:


def get_individual_siblings(_id, include_husb, include_wife):
    individual = individuals[_id]
    siblings = []
    if "INDI_CHILD" in individual and individual["INDI_CHILD"] != "NA":
        for family_id in individual["INDI_CHILD"]:
            family = family_dic[family_id]
            if "FAM_CHILD" in family and family["FAM_CHILD"] != "NA":
                siblings.extend(family["FAM_CHILD"])
            if include_husb:
                if "husband_object" in family and family["husband_object"] != "NA":
                    siblings.extend(get_all_children(family["husband_object"]))
            if include_wife:
                if "wife_object" in family and family["wife_object"] != "NA":
                    siblings.extend(get_all_children(family["wife_object"]))
    siblings = list(set(siblings))
    return siblings


# In[28]:


def get_all_children(individual_object):
    spouses = individual_object["SPOUSE"]
    children = []
    for spouse_family_id in spouses:
        individual_family = family_dic[spouse_family_id]
        if (len(individual_family["FAM_CHILD"]) > 0) and individual_family["FAM_CHILD"] != "NA":
            children.extend(individual_family["FAM_CHILD"])
    return children


# In[29]:


# User Story: US15
def check_sibling_count():
    for family_id in family_dic:
        family = family_dic[family_id]
        if (len(family["FAM_CHILD"]) > 15):
            anomaly_array.append("ANOMALY: FAMILY: US15: {}: {}: Family has {} siblings which is more than 15 siblings"                 .format(family["FAM_LINE"], family_id, len(family["FAM_CHILD"])))


# In[30]:


# Returns the lastname of the name
# Last name is surrounded by '/' in the name
# :param name is the full name of the person
def get_last_name(name):
    return name.split('/')[1];


# In[31]:


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
            if family["HUSB_NAME"] != "NA":
                last_name = get_last_name(family["HUSB_NAME"])
            else:
                continue
        if "children_objects" in family:
            for child in family["children_objects"]:
                if child["SEX"] == "M":
                    if last_name is None:
                        last_name = get_last_name(child["NAME"])
                    else:
                        if last_name != get_last_name(child["NAME"]):
                            anomaly_array.append("ANOMALY: INDIVIDUAL: US16: {}: {}: Individual has different last name {} than family {}"                                   .format(child["NAME_LINE"], child["INDI"], get_last_name(child["NAME"]), last_name))


# In[32]:


# User Story 17
def check_parent_child_marriage():
    for family_id in family_dic:
        family = family_dic[family_id]
        if "HUSB" in family and family["HUSB"] != 'NA' and "WIFE" in family and family["WIFE"] != 'NA':
            if is_spouse_a_child(family["HUSB"], family["WIFE"]):
                anomaly_array.append("ANOMALY: INDIVIDUAL: US17: {}: {}: Individual married to child {}"                                     .format(family["HUSB_LINE"], family["HUSB"], family["WIFE"]))
            if is_spouse_a_child(family["WIFE"], family["HUSB"]):
                anomaly_array.append("ANOMALY: INDIVIDUAL: US17: {}: {}: Individual married to child {}"                                     .format(family["WIFE_LINE"], family["WIFE"], family["HUSB"]))


# In[33]:


def is_spouse_a_child(individual_id, spouse_id):
    individual_object = individuals[individual_id]
    if 'SPOUSE' in individual_object and individual_object['SPOUSE'] != 'NA':
        for spouse_fam in individual_object['SPOUSE']:
            if spouse_fam in family_dic:
                family = family_dic[spouse_fam]
                if "FAM_CHILD" in family and spouse_id in family["FAM_CHILD"]:
                    return True
        return False


# In[34]:


# User story 18
def check_sibling_marriage():
    for individual_id in individuals:
        individual = individuals[individual_id]
        if "SPOUSE" in individual and individual["SPOUSE"] != "NA":
            siblings = get_individual_siblings(individual_id, True, True)
            for spouse_family_id in individual["SPOUSE"]:
                spouse_family = family_dic[spouse_family_id]
                spouse_id = None
                if "WIFE" in spouse_family and spouse_family["WIFE"] != "NA":
                    if spouse_family["WIFE"] != individual_id:
                        spouse_id = spouse_family["WIFE"]
                if "HUSB" in spouse_family and spouse_family["HUSB"] != "NA":
                    if spouse_family["HUSB"] != individual_id:
                        spouse_id = spouse_family["HUSB"]
                if spouse_id is not None and spouse_id in siblings:
                    anomaly_array.append("ANOMALY: INDIVIDUAL: US18: {}: {}: Individual married to sibling {}"                                         .format(individual["INDI_LINE"], individual_id, spouse_id))


# In[35]:


#User_Story_20 Aunts and uncles
#Aunts and uncles should not marry their nieces or nephews
def is_uncle_aunt_marriage_legal():
    for indi in individuals.values(): #scans through each individual first
        current_sp = indi["SPOUSE"] #Array of spouse's family IDs
        current_fm = indi["INDI_CHILD"] #gets the family ID that the person belongs to
        if (current_sp != "NA" and current_fm != "NA"): #if the person has a spouse
            for fam_id in current_fm: #scans through uncle's families
                current_family = family_dic[fam_id]
                current_siblings = current_family["children_objects"] #get the uncle's siblings
                for child in current_siblings: #scans through all siblings
                    child_spouses = child["SPOUSE"]
                    if (child_spouses != "NA"):
                        for spouse in child_spouses:
                            spouse_family = family_dic[spouse]
                            for sp in current_sp:
                                if (family_dic[sp]["WIFE"] in spouse_family["FAM_CHILD"]):
                                    current_sp_family = family_dic[sp].values()
                                    anomaly_array.append("ANOMALY: FAMILY: US20: {}: {}: Person {} should not marry person {}".format(family_dic[sp]["HUSB_LINE"], family_dic[sp]["FAM"], family_dic[sp]["HUSB"], family_dic[sp]["WIFE"]))
                                    return False
                                elif(family_dic[sp]["HUSB"] in spouse_family["FAM_CHILD"]):
                                    anomaly_array.append("ANOMALY: FAMILY: US20: {}: {}: Person {} should not marry person {}".format(family_dic[sp]["WIFE_LINE"], family_dic[sp]["FAM"], family_dic[sp]["WIFE"], family_dic[sp]["HUSB"]))
                                    return False
    return True


# In[36]:


# US 22:
def unique_indi_and_family(value, flag, line_num):
    if flag == "INDI":
        if value in ui:
            error_array.append("ERROR: INDIVIDUAL: US22: {}: {}: Individuals have the same ID".format(line_num, value))
        else:
            ui.append(value)
    else:
        if value in uf:
            error_array.append("ERROR: FAMILY: US22: {}: {}: Family share the same ID ".format(line_num, value))
        else:
            uf.append(value)


# In[37]:


#USID: 23
def unique_name_and_birth():
    li = {}
    for value in individuals.values():
        temp = value["NAME"] + value["BIRT"]
        if temp in li:
            anomaly_array.append("ANOMALY: INDIVIDUAL: US23: {}: {}: {}: Individuals have the same name {} and birth date {}".format(value["INDI_LINE"], value["INDI"], li[temp], value["NAME"], value["BIRT"]))
        else:
            li[temp]=value["INDI"]


# In[38]:


#USID: 25
def unique_family_name_and_birth():
    li = {}
    for value in family_dic.values():
        if "children_objects" in value:
            for child in value["children_objects"]:
                temp = child["NAME"] + child["BIRT"]
                if temp in li:
                    anomaly_array.append("ANOMALY: INDIVIDUAL: US25: {}: {}: {}: Individuals share the same first name {} and birth date {} from family {}".format(value["FAM_LINE"], child["INDI"], li[temp], child["NAME"], child["BIRT"], value["FAM"]))
                else:          
                    li[temp]=child["INDI"]


# In[39]:


#User_Story_29: List all deceased individuals in a GEDCOM file
#Prints out a table with all the deceased people's information
def listDeceased():
    current_dic = {}
    deceased_count = 0
    for value in individuals.values():
        if(str(value["DEAT"]) != "NA" and (value["ALIVE"])):
            error_array.append(("ERROR: INDIVIDUAL: US29: {}: Person is alive but has Death Date {}").format(value["NAME_LINE"], value["NAME"], value["DEAT"]))
        #print(("ERROR: INDIVIDUAL: US29: {}: Person is alive but has Death Date {}").format(value["NAME_LINE"], value["NAME"], value["DEAT"]))
        elif(str(value["DEAT"]) == "NA" and (not value["ALIVE"])):
            error_array.append(("ERROR: INDIVIDUAL: US29: {}: Person {}: is dead but has no Death Date").format(value["INDI_LINE"], value["INDI"]));
        #print(("ERROR: INDIVIDUAL: US29: {}: Person {}: is dead but has no Death Date").format(value["INDI_LINE"], value["INDI"]))
        elif(not value["ALIVE"]):
            deceased_count += 1
            current_dic[value["INDI"]] = value    
    if deceased_count > 0:
        #print("User_Story_29: List all deceased individuals in a GEDCOM file")
        #Use pretty table module to print out the results
        allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
        tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
        printTable("US29: Deceased People Table", allFields, tagNames, current_dic)
    


# In[40]:


#User_Story_30: List all living married people in a GEDCOM file
#Prints out a table with all the living married people's information
def listLivingMarried():
    current_dic = {}
    living_count = 0
    for value in individuals.values():
        if(value["ALIVE"] and value["SPOUSE"] != "NA"):
            current_dic[value["INDI"]] = value
            living_count += 1
        elif(not value["ALIVE"] and value["SPOUSE"] != "NA"):
            error_array.append("ERROR: INDIVIDUAL: US30: {}: {}: Deceased Person is married to Person {}".format(value["INDI_LINE"], value["INDI"], "".join(value["SPOUSE"])))
#             print("ERROR: INDIVIDUAL: US30: {}: {}: Deceased Person is married to Person {}".format(value["INDI_LINE"], value["INDI"], "".join(value["SPOUSE"])))
    if living_count > 0:
#         print("User_Story_30: List all living married people in a GEDCOM file")
        #Use pretty table module to print out the results
        allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
        tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
        printTable("US30: Living & Married People Table", allFields, tagNames, current_dic)


# In[41]:


#US 32: List multiple births
def multiple_birth():
    for value in family_dic.values():
        li={}
        if "children_objects" in value:
            for child in value["children_objects"]:
                temp = str(child["INDI_CHILD"]) + child["BIRT"]
                if temp in li:
                    anomaly_array.append("ANOMALY: FAMILY: US32: {}: {}: The two or more individuals were born at the same time".format(value["FAM_LINE"], value["FAM"]))
                else:          
                    li[temp]=child["INDI"]


# In[42]:


#US 34: 
def large_age_diff():
    for value in family_dic.values():
#         for family_id in family_dic:
        family= value["FAM"]
        if "husband_object" in family_dic[family]:
            husband=family_dic[family]["husband_object"]
            hage = int(husband["AGE"])
        if "wife_object" in family_dic[family]:
            wife=family_dic[family]["wife_object"]
            wage = int(wife["AGE"])
            agediff = hage/wage
            if agediff>=2 or agediff<=0.5:
                anomaly_array.append("ANOMALY: FAMILY: US34: {}: {}: Family has a large spouse age difference".format(value["FAM_LINE"], value["FAM"]))
                


# In[43]:


#US 38 List upcoming birthdays
def list_upcoming_bday():
    today_month = int(datetime.today().strftime("%m"))
    today_date = int(datetime.today().strftime("%d"))
    current_dic = {}
    bday_count = 0
    for value in individuals.values():
        if (value["BIRT"] == 'NA'):
            error_array.append("ERROR: INDIVIDUAL: US38: {}: Person {} does not have birthday!".format(value["BIRT_LINE"], value["BIRT"]))
            return False
        else:
            current_birt = value["BIRT"]
            current_month = int(current_birt.split("-")[1])
            current_date = int(current_birt.split("-")[2])
            day_difference = (current_month - today_month)* 30 + current_date- today_date
            if (day_difference > 0 and day_difference <= 30):
                current_dic[value["INDI"]] = value
                bday_count += 1

    if bday_count > 0:
        #Use pretty table module to print out the results
        allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
        tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
        printTable("US38 List Upcoming Birthdays Table", allFields, tagNames, current_dic)
        
    return True


# In[44]:


#US 39 List upcoming anniversaries
def list_upcoming_anni():
    today_month = int(datetime.today().strftime("%m"))
    today_date = int(datetime.today().strftime("%d"))
    current_dic = {}
    marr_count = 0
    for value in family_dic.values():
        if (value["MARR"] == 'NA'):
            error_array.append("ERROR: FAMILY: US39: {}: Family {} does not have married date!".format(value["FAM_LINE"], value["FAM"]))
            return False
        #shouldn't we continue looking for other people's birthday without returning false?
        else:
            current_marr = value["MARR"]
            current_month = int(current_marr.split("-")[1])
            current_date = int(current_marr.split("-")[2])
            day_difference = (current_month - today_month)* 30 + current_date- today_date
            if (day_difference > 0 and day_difference <= 30):
                current_dic[value["FAM"]] = value
                marr_count += 1
    if marr_count > 0:
        #Use pretty table module to print out the results
        allFields = ["ID", "Married", "Husband ID", "Husband Name", "Wife ID", "Wife Name"]
        tagNames = ["FAM", "MARR", "HUSB", "HUSB_NAME", "WIFE", "WIFE_NAME"]
        
        printTable("US39: List Upcoming Anniversaries Table", allFields, tagNames, current_dic)
        
    return True


# In[45]:


def check_cousins_marriage():
    for individual_id in individuals:
        individual = individuals[individual_id]
        if "SPOUSE" in individual and individual["SPOUSE"] != "NA":
            siblings = get_individual_siblings(individual_id, True, True)
            for spouse_family_id in individual["SPOUSE"]:
                spouse_family = family_dic[spouse_family_id]
                spouse_id = None
                if "WIFE" in spouse_family and spouse_family["WIFE"] != "NA":
                    if spouse_family["WIFE"] != individual_id:
                        spouse_id = spouse_family["WIFE"]
                if "HUSB" in spouse_family and spouse_family["HUSB"] != "NA":
                    if spouse_family["HUSB"] != individual_id:
                        spouse_id = spouse_family["HUSB"]
                if spouse_id is not None and spouse_id in siblings:
                    anomaly_array.append("ANOMALY: INDIVIDUAL: US19: {}: {}: Individual married to cousins {}".format(individual["INDI_LINE"], individual_id, spouse_id))


# In[46]:


# Prints out the Individual Table
def printIndividualTable():
    #print("People Table")
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "INDI_CHILD", "SPOUSE"]
    
    printTable("People Table", allFields, tagNames, individuals)


# In[47]:


# Prints out the Family Table
def printFamilyTable():
    #print("Families Table")
    allFields = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    tagNames = ["FAM", "MARR", "DIV", "HUSB", "HUSB_NAME", "WIFE", "WIFE_NAME", "FAM_CHILD"]
    
    printTable("Families Table", allFields, tagNames, family_dic)


# In[48]:


# Prints out the data in both error and anomaly arrays
def printError():
    file = open("cs555_sprint_outputs.txt", "a")
    if (len(error_array) > 0):
        print("------error messages------")
        file.write("------error messages------" + "\n")
        for error in error_array:
            print(error)
            file.write(error + "\n")
    if(len(anomaly_array) > 0):
        print("-----anomaly messages-----")
        file.write("-----anomaly messages-----" + "\n")
        for anomaly in anomaly_array:
            print(anomaly)
            file.write(anomaly + "\n")
    file.close()
    


# In[49]:


# Prints out a table of dictionary data with the passed-in arguments
# Parameters:
# fields: a list of fields for the table
# tag_names: tag names used to access each data field
# dictionary: a dictionary filled with data
def printTable(table_name, fields, tag_names, dictionary):
    print(table_name)
    table = PrettyTable()
    table.field_names = fields
    for element in dictionary.values():    
        count = 1
        row_data = "" #string uses to store each tag within the current element
        for name in tag_names:
            if (count < int(len(tag_names))): #not the last element
                if (isinstance(element[name], list)): #current element is an array
                    row_data += (",".join(element[name]) + "? ")
                else: #current element is not an array
                    row_data += (str(element[name]) + "? ")
            elif (count == int(len(tag_names))):
                if (isinstance(element[name], list)): #current element is an array
                    row_data += (",".join(element[name]))
                else: #current element is not an array
                    row_data += (str(element[name]))
                break
            count+= 1;
        table.add_row(row_data.split('?'))
    # Stores outputs to a text file
    storeResults(table_name, table.get_string())
    print(table)


# In[50]:


# Stores all Project outputs into a single text file
# Parameters:
# result_name: name that will appear 
def storeResults(result_name, outputs):
    file = open("cs555_sprint_outputs.txt", "a")
    file.write(result_name + "\n")
    file.write(outputs + "\n\n")
    file.close()


# In[51]:


# Global variables initialization
tag_sp = ["INDI", "FAM"]
#Level Zero Tags
tag_zero = ["HEAD", "TRLR", "NOTE"]
#Level One Tags
tag_one = ["NAME", "SEX", "BIRT", "DEAT","FAMC","FAMS","MARR", "DIV","HUSB","WIFE","CHIL"]
#Level Zero Tags
tag_fam = {"INDI":["NAME", "SEX","BIRT", "DEAT","FAMC","FAMS"],
             "FAM":["MARR", "DIV","HUSB","WIFE","CHIL"], 
             "DATE":["BIRT", "DEAT", "DIV", "MARR"]}
family_dic = None
individuals = None
error_array = []
anomaly_array = []


# In[52]:


document = read_in("./acceptance_test_file_sprint2.ged")
if os.path.exists("cs555_sprint_outputs.txt"):
    os.remove("cs555_sprint_outputs.txt")

create_individuals_map()
create_family_dic()
# Prints out all the people in GEDCOM file
printIndividualTable()
# Prints out all the families in GEDCO file
printFamilyTable()
#User 01
validate_dates()
#User 02
is_birth_before_marraige()
#US04
is_marriage_after_divorce()
#US05
is_marriage_after_death()
#US06
check_divorce_before_death()
#User 07
is_age_legal()
#User 08
birth_before_marriage()
#User 09
birth_before_death()
#User 10
is_marriage_legal()
#User 11
check_for_bigamy()
#User 12
check_parents_not_too_old()
#User 13
check_sibling_spacing()
#User 15
check_sibling_count()
#User 16
check_last_names()
#User 17
check_parent_child_marriage()
#User 18
check_sibling_marriage()
#User 20
is_uncle_aunt_marriage_legal()
#User 22
# unique_indi_and_family()
#User 23
unique_name_and_birth()
#User 25
unique_family_name_and_birth()
#User 29
listDeceased()
#User 30
listLivingMarried()
#User 32
multiple_birth()
#User 34
large_age_diff()
#User 38
list_upcoming_bday()
# User 39
list_upcoming_anni()
check_cousins_marriage()


#Prints out all the errors and anomalies of each function
printError()


# In[ ]:




