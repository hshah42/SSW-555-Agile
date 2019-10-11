#!/usr/bin/env python
# coding: utf-8

# In[504]:


import pytest
import unittest
import mock
import Project


# In[505]:


def test_dates_pass():
    
    family_dic={'@F8@': {'FAM': '@F8@',
  'HUSB_NAME': 'George /Nickson/',
  'HUSB': '@I18@',
  'WIFE_NAME': 'Kitty /Nilson/',
  'WIFE': '@I13@',
  'FAM_CHILD': ['@I19@'],
  'CHIL': '@I19@',
  'MARR': '2018-3-24',
  'DIV': '2010-3-24'}}
    
    
    individuals={'@I1@': {'INDI': '@I1@',
  'NAME': 'Jimmy /Colon/',
  'SEX': 'M',
  'BIRT': '2008-12-10',
  'INDI_CHILD': ['@F2@'],
  'SPOUSE': ['@F1@'],
  'DEAT': 'NA',
  'AGE': '9',
  'ALIVE': True},
 '@I2@': {'INDI': '@I2@',
  'NAME': 'Helen /Colon/',
  'SEX': 'F',
  'BIRT': '1089-12-10',
  'DEAT': '2002-6-2',
  'INDI_CHILD': 'NA',
  'SPOUSE': ['@F1@'],
  'AGE': '13',
  'ALIVE': False}}
    
    Project.family_dic = family_dic
    Project.individuals=individuals
    Project.error_array = []
    Project.validate_dates()

    return len(Project.error_array)==0


# In[506]:


def test_dates_error():
    
    family_dic={'@F8@': {'FAM': '@F8@',
  'HUSB_NAME': 'George /Nickson/',
  'HUSB': '@I18@',
  'WIFE_NAME': 'Kitty /Nilson/',
  'WIFE': '@I13@',
  'FAM_CHILD': ['@I19@'],
  'CHIL': '@I19@',
  'MARR': '2020-3-24',
  'DIV': '2021-3-24'}}
    
    
    individuals={'@I1@': {'INDI': '@I1@',
  'NAME': 'Jimmy /Colon/',
  'SEX': 'M',
  'BIRT': '2030-12-10',
  'INDI_CHILD': ['@F2@'],
  'SPOUSE': ['@F1@'],
  'DEAT': 'NA',
  'AGE': '9',
  'ALIVE': True},
 '@I2@': {'INDI': '@I2@',
  'NAME': 'Helen /Colon/',
  'SEX': 'F',
  'BIRT': '2000-12-10',
  'DEAT': '2020-6-2',
  'INDI_CHILD': 'NA',
  'SPOUSE': ['@F1@'],
  'AGE': '81',
  'ALIVE': False}}
    
    Project.family_dic = family_dic
    Project.individuals=individuals
    Project.error_array = []
    Project.validate_dates()

    return Project.error_array==['ERROR: FAMILY: US01: @F8@: Family has marrige date 2020-3-24 later than today',
                                 'ERROR: FAMILY: US01: @F8@: Family has divorce date 2021-3-24 later than today',
                                 'ERROR: INDIVIDUAL: US01: @I1@: Individual has birth date 2030-12-10 later than today',
                                 'ERROR: INDIVIDUAL: US01: @I2@: Individual has death date 2020-6-2 later than today']


# In[507]:


def test_dates_pass():
    
    family_dic={'@F1@': {'FAM': '@F1@',
  'HUSB_NAME': 'Samuel /Venzon/',
  'HUSB': '@I6@',
  'WIFE_NAME': 'Willodean /Malagon/',
  'WIFE': '@I1@',
  'FAM_CHILD': ['@I7@', '@I13@'],
  'CHIL': '@I13@',
  'MARR': '1970-7-7',
  'DIV': 'NA'}}
    
    
    individuals={'@I9@': {'INDI': '@I9@',
  'NAME': 'Jerrell /Finklea/',
  'SEX': 'M',
  'BIRT': '1965-9-8',
  'INDI_CHILD': 'NA',
  'SPOUSE': ['@F6@'],
  'DEAT': 'NA',
  'AGE': '54',
  'ALIVE': True}}
    
    Project.family_dic = family_dic
    Project.individuals=individuals
    Project.error_array = []
    Project.validate_dates()

    return len(Project.error_array)==0


# In[508]:


def test_birth_before_marraige_do_nothing():
    family_dic = {'@F1@':{'MARR':'1968-6-4','husband_object':{'INDI':'@I1@','BIRT':'1950-11-8'},'wife_object':{'INDI':'@I2@','BIRT':'1960-11-8'}}}
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.is_birth_before_marraige()
    
    assert len(Project.error_array) == 0
    return True


# In[509]:


def test_birth_after_marraige_appended_to_error():
    family_dic = {'@F1@':{'MARR':'1968-6-4','husband_object':{'INDI':'@I1@','BIRT':'1970-11-8'},'wife_object':{'INDI':'@I2@','BIRT':'1960-11-8'}}}
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.is_birth_before_marraige()
    
    assert Project.error_array[0] == "ERROR: INDIVIDUAL: US02: @I1@: Person has marriage date 1968-6-4 before birth date 1970-11-8"
    return True


# In[510]:


def test_not_legal_marriage():
    family_dic =  {'@F8@': {'FAM': '@F8@',
  'HUSB_NAME': 'George /Nickson/',
  'HUSB': '@I18@',
  'WIFE_NAME': 'Kitty /Nilson/',
  'WIFE': '@I13@',
  'FAM_CHILD': ['@I19@'],
  'CHIL': '@I19@',
  'MARR': '1991-3-24',
  'DIV': 'NA',
  'husband_object': {'INDI': '@I18@',
   'NAME': 'George /Nickson/',
   'SEX': 'M',
   'BIRT': '1980-3-17',
   'INDI_CHILD': 'NA',
   'SPOUSE': ['@F8@'],
   'DEAT': 'NA',
   'AGE': '45',
   'ALIVE': True},
  'wife_object': {'INDI': '@I13@',
   'NAME': 'Kitty /Nilson/',
   'SEX': 'F',
   'BIRT': '1980-7-10',
   'INDI_CHILD': ['@F5@'],
   'SPOUSE': ['@F8@'],
   'DEAT': 'NA',
   'AGE': '39',
   'ALIVE': True}}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.is_marriage_legal()

    return Project.anomaly_array==["ANOMALY: INDIVIDUAL: US10: @I18@: Father of family @F8@ is younger than 14 years old - Birth Date 1980-3-17",
"ANOMALY: INDIVIDUAL: US10: @I13@: Wife of family @F8@ is younger than 14 years old - Birth Date 1980-7-10"]


# In[511]:


def test_legal_marriage():
    family_dic =  {'@F8@': {'FAM': '@F8@',
  'HUSB_NAME': 'George /Nickson/',
  'HUSB': '@I18@',
  'WIFE_NAME': 'Kitty /Nilson/',
  'WIFE': '@I13@',
  'FAM_CHILD': ['@I19@'],
  'CHIL': '@I19@',
  'MARR': '2000-3-24',
  'DIV': 'NA',
  'husband_object': {'INDI': '@I18@',
   'NAME': 'George /Nickson/',
   'SEX': 'M',
   'BIRT': '1973-3-17',
   'INDI_CHILD': 'NA',
   'SPOUSE': ['@F8@'],
   'DEAT': 'NA',
   'AGE': '45',
   'ALIVE': True},
  'wife_object': {'INDI': '@I13@',
   'NAME': 'Kitty /Nilson/',
   'SEX': 'F',
   'BIRT': '1980-7-10',
   'INDI_CHILD': ['@F5@'],
   'SPOUSE': ['@F8@'],
   'DEAT': 'NA',
   'AGE': '39',
   'ALIVE': True}}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.is_marriage_legal()

    return len(Project.anomaly_array) == 0


# In[512]:


def test_over_age_150():
    individuals={'@I1@': {'INDI': '@I1@',
  'NAME': 'Jimmy /Colon/',
  'SEX': 'M',
  'BIRT': '1860-6-5',
  'INDI_CHILD': ['@F2@'],
  'SPOUSE': ['@F1@'],
  'DEAT': 'NA',
  'AGE': '159',
  'ALIVE': True},
 '@I2@': {'INDI': '@I2@',
  'NAME': 'Helen /Colon/',
  'SEX': 'F',
  'BIRT': '1850-12-10',
  'DEAT': '2009-6-2',
  'INDI_CHILD': 'NA',
  'SPOUSE': ['@F1@'],
  'AGE': '159',
  'ALIVE': False}}
                 
    Project.individuals = individuals
    Project.anomaly_array = []
    Project.is_age_legal()
    return Project.anomaly_array==['ANOMALY: INDIVIDUAL: US07: @I1@: More than 150 years old - Birth Date 1860-6-5',
 'ANOMALY: INDIVIDUAL: US07: @I2@: More than 150 years old at death - Birth Date 1850-12-10: Death Date 2009-6-2']


# In[513]:


def test_less_age_150():
    individuals={'@I3@': {'INDI': '@I3@',
  'NAME': 'Dora /Colon/',
  'SEX': 'F',
  'BIRT': '1951-4-5',
  'INDI_CHILD': ['@F1@'],
  'SPOUSE': ['@F3@', '@F4@'],
  'DEAT': 'NA',
  'AGE': '68',
  'ALIVE': True},
 '@I4@': {'INDI': '@I4@',
  'NAME': 'Rurra /Colon/',
  'SEX': 'F',
  'BIRT': '1952-9-8',
  'INDI_CHILD': ['@F1@'],
  'SPOUSE': ['@F5@'],
  'DEAT': 'NA',
  'AGE': '66',
  'ALIVE': True}}
                 
    Project.individuals = individuals
    Project.anomaly_array = []
    Project.is_age_legal()
    
    return len(Project.anomaly_array) == 0


# In[514]:


# User_Story_29: List all deceased individuals in a GEDCOM file
# Success test 
@mock.patch("Project.printTable")
def test_list_deceased_individuals_success(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    current_dic = {'@I6@': {'INDI': '@I6@', "INDI_LINE": '10', 'NAME': 'Stephen /Chang/', 'NAME_LINE': '15', 'SEX': 'M', 'SEX_LINE': '20', 'BIRT': '1935-12-5', 'BIRT_LINE': '22', 'DEAT': '2005-4-15', 'DEAT_LINE': '25', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'SPOUSE_LINE': '27', 'AGE': '70', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listDeceased()
    mock_printTable.assert_called_with("US29: Deceased People Table", allFields, tagNames, current_dic)
    return True


# In[515]:


# User_Story_29: List all deceased individuals in a GEDCOM file
# Failed test: Person is dead but has no Death Date
@mock.patch("Project.printTable")
def test_list_deceased_individuals_error(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    current_dic = {'@I6@': {'INDI': '@I6@', "INDI_LINE": '10', 'NAME': 'David /Chang/', 'NAME_LINE': '15', 'SEX': 'M', 'SEX_LINE': '20', 'BIRT': '2002-12-5', 'BIRT_LINE': '22', 'DEAT': 'NA', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F7@'], 'SPOUSE_LINE': '27', 'AGE': '79', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listDeceased()
    assert mock_printTable.called == False
    return True


# In[516]:


# User_Story_30: List all living married people in a GEDCOM file
# Success test
@mock.patch("Project.printTable")
def test_list_living_married_individuals_success(mock_printTable):

    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
    current_dic = {'@I1@': {'INDI': '@I1@', 'NAME': 'Johnny /Chang/', 'SEX': 'M', 'BIRT': '1958-9-6', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'AGE': '61', 'ALIVE': True}}
    Project.individuals = current_dic
    Project.listLivingMarried()
    mock_printTable.assert_called_with("US30: Living & Married People Table", allFields, tagNames, current_dic)
    return True


# In[517]:


# User_Story_30: List all living married people in a GEDCOM file
# Failed test
@mock.patch("Project.printTable")
def test_list_living_married_individuals_error(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
    current_dic = {'@I4@': {'INDI': '@I1@', 'INDI_LINE': '10', 'NAME': 'Michael /Chang/', 'NAME_LINE': '12', 'SEX': 'M', 'SEX_LINE': '15', 'BIRT': '1958-9-6', 'BIRT_LINE': '17', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'SPOUSE_LINE': '18', 'DEAT': '2002-9-6', 'DEAT_LINE': '22', 'AGE': '61', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listLivingMarried()
    
    assert mock_printTable.called == False
    return True


# In[518]:


def test_more_than_15_siblings():
    family_dic = {'@F1@':{'FAM_CHILD':['@I1@','@I10@','@I11@','@I12@','@I13@','@I14@','@I15@','@I16@','@I17@','@I18@','@I19@','@I20@','@I21@','@I22@','@I23@','@I24@','@I24@']}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_sibling_count()

    assert Project.anomaly_array[0] == 'ANOMALY: FAMILY: US16: @F1@: Family has 17 siblings which is more than 15 siblings'
    return True


# In[519]:


def test_less_than_15_siblings():
    family_dic = {'@F1@':{'FAM_CHILD':['@I1@']}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_sibling_count()

    assert len(Project.anomaly_array) == 0
    return True
    


# In[520]:


def test_different_male_last_name():
    family_dic = {'@F1@':{'HUSB_NAME':'Harry /Potter/','FAM_CHILD':['@I1@','@I10@'],'children_objects':[{'INDI':'@I1@', 'SEX':'M','NAME':'Chandler /Bing/'},{'INDI':'@I10@', 'SEX':'M','NAME':'Chandler /Potter/'}]}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_last_names()
    assert Project.anomaly_array[0] == 'ANOMALY: INDIVIDUAL: US16: @I1@: Individual has different last name Bing than family Potter'
    return True


# In[521]:


def test_same_male_last_name():
    family_dic = {'@F1@':{'HUSB_NAME':'Harry /Potter/','FAM_CHILD':['@I1@','@I10@'],'children_objects':[{'INDI':'@I1@', 'SEX':'M','NAME':'Joey /Potter/'},{'INDI':'@I10@', 'SEX':'M','NAME':'Chandler /Potter/'}]}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_last_names()

    assert len(Project.anomaly_array) == 0
    return True


# In[522]:


def test_unique_name_and_birth_error():
    individuals={'@I31@': {'INDI': '@I31@',
      'NAME': 'Sock /Malagon/',
      'SEX': 'F',
      'BIRT': '1955-10-17',
      'INDI_CHILD': ['@F3@'],
      'SPOUSE': 'NA',
      'DEAT': 'NA',
      'AGE': '63',
      'ALIVE': True},
     '@I35@': {'INDI': '@I35@',
      'NAME': 'Sock /Malagon/',
      'SEX': 'F',
      'BIRT': '1955-10-17',
      'INDI_CHILD': ['@F9@'],
      'SPOUSE': 'NA',
      'DEAT': 'NA',
      'AGE': '63',
      'ALIVE': True}}
        

    Project.individuals = individuals
    Project.anomaly_array = []
    
    Project.unique_name_and_birth()

    return Project.anomaly_array==['ANOMALY: INDIVIDUAL: US23: @I35@: @I31@: Individuals have the same name Sock /Malagon/ and birth date 1955-10-17']


# In[523]:


def test_unique_name_and_birth_pass():
    individuals={'@I3@': {'INDI': '@I3@',
      'NAME': 'Dora /Colon/',
      'SEX': 'F',
      'BIRT': '1951-4-5',
      'INDI_CHILD': ['@F1@'],
      'SPOUSE': ['@F3@', '@F4@'],
      'DEAT': 'NA',
      'AGE': '68',
      'ALIVE': True},
     '@I4@': {'INDI': '@I4@',
      'NAME': 'Rurra /Colon/',
      'SEX': 'F',
      'BIRT': '1952-9-8',
      'INDI_CHILD': ['@F1@'],
      'SPOUSE': ['@F5@'],
      'DEAT': 'NA',
      'AGE': '66',
      'ALIVE': True}}
    
    Project.individuals = individuals
    Project.anomaly_array = [] 
    Project.unique_name_and_birth()
    
    return len(Project.anomaly_array)==0


# In[524]:


def test_unique_family_name_and_birth_error():
    family_dic = {'@F1@': {'FAM': '@F1@',
  'HUSB_NAME': 'Samuel /Venzon/',
  'HUSB': '@I6@',
  'WIFE_NAME': 'Willodean /Malagon/',
  'WIFE': '@I1@',
  'FAM_CHILD': ['@I7@', '@I13@'],
  'CHIL': '@I13@',
  'MARR': '1970-7-7',
  'DIV': 'NA',
  'children_objects': [{'INDI': '@I7@',
    'NAME': 'Beth /Venzon/',
    'SEX': 'M',
    'BIRT': '1973-7-8',
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': ['@F5@'],
    'DEAT': 'NA',
    'AGE': '46',
    'ALIVE': True},
   {'INDI': '@I13@',
    'NAME': 'Beth /Venzon/',
    'SEX': 'F',
    'BIRT': '1973-7-8',
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': 'NA',
    'DEAT': 'NA',
    'AGE': '44',
    'ALIVE': True}]}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.unique_family_name_and_birth()

    return Project.anomaly_array==['ANOMALY: INDIVIDUAL: US25: @I13@: @I7@: Individuals share the same first name Beth /Venzon/ and birth date 1973-7-8 from family @F1@']


# In[525]:


def test_unique_family_name_and_birth_pass():
    family_dic =  {'children_objects': [{'INDI': '@I30@',
        'NAME': 'Chet /Malagon/',
        'SEX': 'M',
        'BIRT': '1943-8-18',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'DEAT': 'NA',
        'AGE': '76',
        'ALIVE': True},
       {'INDI': '@I31@',
        'NAME': 'Sock /Malagon/',
        'SEX': 'F',
        'BIRT': '1955-10-17',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'DEAT': 'NA',
        'AGE': '63',
        'ALIVE': True}]}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.unique_family_name_and_birth()

    return len(Project.anomaly_array) == 0


# In[526]:


# US20 Aunts and uncles - success
def aunts_and_uncles_success():
    individuals = {'@I1@': {'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F1@'], 'SPOUSE': 'NA', 'FAMC_LINE': 22, 'DEAT': 'NA', 'BIRT_LINE': 22, 'AGE': '31', 'ALIVE': True}, '@I2@': {'INDI': '@I2@', 'INDI_LINE': 23, 'NAME': 'Johny /Chang/', 'NAME_LINE': 24, 'SEX': 'M', 'SEX_LINE': 28, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 31, 'DEAT': 'NA', 'BIRT_LINE': 31, 'AGE': '61', 'ALIVE': True}, '@I3@': {'INDI': '@I3@', 'INDI_LINE': 32, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 33, 'SEX': 'F', 'SEX_LINE': 37, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 40, 'DEAT': 'NA', 'BIRT_LINE': 40, 'AGE': '59', 'ALIVE': True}}
    family_dic = {'@F1@': {'FAM': '@F1@', 'FAM_LINE': 47, 'HUSB_NAME': 'Johny /Chang/', 'HUSB_LINE': 42, 'HUSB': '@I2@', 'WIFE_NAME': 'Nancy /Tsai/', 'WIFE_LINE': 43, 'WIFE': '@I3@', 'FAM_CHILD': ['@I1@'], 'CHIL_LINE': 44, 'CHIL': '@I1@', 'MARR': '1980-3-2', 'DIV': 'NA', 'husband_object': {'INDI': '@I2@', 'INDI_LINE': 23, 'NAME': 'Johny /Chang/', 'NAME_LINE': 24, 'SEX': 'M', 'SEX_LINE': 28, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 31, 'DEAT': 'NA', 'BIRT_LINE': 31, 'AGE': '61', 'ALIVE': True}, 'wife_object': {'INDI': '@I3@', 'INDI_LINE': 32, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 33, 'SEX': 'F', 'SEX_LINE': 37, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 40, 'DEAT': 'NA', 'BIRT_LINE': 40, 'AGE': '59', 'ALIVE': True}, 'children_objects': [{'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F1@'], 'SPOUSE': 'NA', 'FAMC_LINE': 22, 'DEAT': 'NA', 'BIRT_LINE': 22, 'AGE': '31', 'ALIVE': True}]}}
    
    Project.individuals = individuals
    Project.family_dic = family_dic
    
    assert Project.is_uncle_aunt_marriage_legal() == True
    return True


# In[527]:


# US20 Aunts and uncles - error
def aunts_and_uncles_error():
    individuals = {'@I1@': {'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 22, 'FAMC_LINE': 23, 'DEAT': 'NA', 'BIRT_LINE': 23, 'AGE': '31', 'ALIVE': True}, '@I2@': {'INDI': '@I2@', 'INDI_LINE': 24, 'NAME': 'Johny /Chang/', 'NAME_LINE': 25, 'SEX': 'M', 'SEX_LINE': 29, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'FAMS_LINE': 32, 'DEAT': 'NA', 'BIRT_LINE': 32, 'AGE': '61', 'ALIVE': True}, '@I3@': {'INDI': '@I3@', 'INDI_LINE': 33, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 34, 'SEX': 'F', 'SEX_LINE': 38, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'FAMS_LINE': 41, 'DEAT': 'NA', 'BIRT_LINE': 41, 'AGE': '59', 'ALIVE': True}, '@I4@': {'INDI': '@I4@', 'INDI_LINE': 42, 'NAME': 'Dylan /Chang/', 'NAME_LINE': 43, 'SEX': 'M', 'SEX_LINE': 47, 'BIRT': '1990-6-20', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'FAMS_LINE': 50, 'FAMC_LINE': 51, 'DEAT': 'NA', 'BIRT_LINE': 51, 'AGE': '29', 'ALIVE': True}, '@I5@': {'INDI': '@I5@', 'INDI_LINE': 52, 'NAME': 'Diana /Liu/', 'NAME_LINE': 53, 'SEX': 'F', 'SEX_LINE': 57, 'BIRT': '1990-8-26', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F3@'], 'FAMS_LINE': 60, 'DEAT': 'NA', 'BIRT_LINE': 60, 'AGE': '29', 'ALIVE': True}, '@I6@': {'INDI': '@I6@', 'INDI_LINE': 61, 'NAME': 'Felicia /Chang/', 'NAME_LINE': 62, 'SEX': 'F', 'SEX_LINE': 66, 'BIRT': '2010-9-8', 'INDI_CHILD': ['@F3@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 69, 'FAMC_LINE': 70, 'DEAT': 'NA', 'BIRT_LINE': 70, 'AGE': '9', 'ALIVE': True}}
    family_dic = {'@F1@': {'FAM': '@F1@', 'FAM_LINE': 77, 'HUSB_NAME': 'David /Chang/', 'HUSB_LINE': 72, 'HUSB': '@I1@', 'WIFE_NAME': 'Felicia /Chang/', 'WIFE_LINE': 73, 'WIFE': '@I6@', 'MARR': '2012-6-12', 'DIV': 'NA', 'FAM_CHILD': 'NA', 'husband_object': {'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 22, 'FAMC_LINE': 23, 'DEAT': 'NA', 'BIRT_LINE': 23, 'AGE': '31', 'ALIVE': True}, 'wife_object': {'INDI': '@I6@', 'INDI_LINE': 61, 'NAME': 'Felicia /Chang/', 'NAME_LINE': 62, 'SEX': 'F', 'SEX_LINE': 66, 'BIRT': '2010-9-8', 'INDI_CHILD': ['@F3@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 69, 'FAMC_LINE': 70, 'DEAT': 'NA', 'BIRT_LINE': 70, 'AGE': '9', 'ALIVE': True}}, '@F2@': {'FAM': '@F2@', 'FAM_LINE': 85, 'HUSB_NAME': 'Johny /Chang/', 'HUSB_LINE': 79, 'HUSB': '@I2@', 'WIFE_NAME': 'Nancy /Tsai/', 'WIFE_LINE': 80, 'WIFE': '@I3@', 'FAM_CHILD': ['@I1@', '@I4@'], 'CHIL_LINE': 82, 'CHIL': '@I4@', 'MARR': '1980-3-2', 'DIV': 'NA', 'husband_object': {'INDI': '@I2@', 'INDI_LINE': 24, 'NAME': 'Johny /Chang/', 'NAME_LINE': 25, 'SEX': 'M', 'SEX_LINE': 29, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'FAMS_LINE': 32, 'DEAT': 'NA', 'BIRT_LINE': 32, 'AGE': '61', 'ALIVE': True}, 'wife_object': {'INDI': '@I3@', 'INDI_LINE': 33, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 34, 'SEX': 'F', 'SEX_LINE': 38, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'FAMS_LINE': 41, 'DEAT': 'NA', 'BIRT_LINE': 41, 'AGE': '59', 'ALIVE': True}, 'children_objects': [{'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 22, 'FAMC_LINE': 23, 'DEAT': 'NA', 'BIRT_LINE': 23, 'AGE': '31', 'ALIVE': True}, {'INDI': '@I4@', 'INDI_LINE': 42, 'NAME': 'Dylan /Chang/', 'NAME_LINE': 43, 'SEX': 'M', 'SEX_LINE': 47, 'BIRT': '1990-6-20', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'FAMS_LINE': 50, 'FAMC_LINE': 51, 'DEAT': 'NA', 'BIRT_LINE': 51, 'AGE': '29', 'ALIVE': True}]}, '@F3@': {'FAM': '@F3@', 'FAM_LINE': 90, 'HUSB_NAME': 'Dylan /Chang/', 'HUSB_LINE': 87, 'HUSB': '@I4@', 'WIFE_NAME': 'Diana /Liu/', 'WIFE_LINE': 88, 'WIFE': '@I5@', 'FAM_CHILD': ['@I6@'], 'CHIL_LINE': 89, 'CHIL': '@I6@', 'DIV': 'NA', 'MARR': 'NA', 'husband_object': {'INDI': '@I4@', 'INDI_LINE': 42, 'NAME': 'Dylan /Chang/', 'NAME_LINE': 43, 'SEX': 'M', 'SEX_LINE': 47, 'BIRT': '1990-6-20', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'FAMS_LINE': 50, 'FAMC_LINE': 51, 'DEAT': 'NA', 'BIRT_LINE': 51, 'AGE': '29', 'ALIVE': True}, 'wife_object': {'INDI': '@I5@', 'INDI_LINE': 52, 'NAME': 'Diana /Liu/', 'NAME_LINE': 53, 'SEX': 'F', 'SEX_LINE': 57, 'BIRT': '1990-8-26', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F3@'], 'FAMS_LINE': 60, 'DEAT': 'NA', 'BIRT_LINE': 60, 'AGE': '29', 'ALIVE': True}, 'children_objects': [{'INDI': '@I6@', 'INDI_LINE': 61, 'NAME': 'Felicia /Chang/', 'NAME_LINE': 62, 'SEX': 'F', 'SEX_LINE': 66, 'BIRT': '2010-9-8', 'INDI_CHILD': ['@F3@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 69, 'FAMC_LINE': 70, 'DEAT': 'NA', 'BIRT_LINE': 70, 'AGE': '9', 'ALIVE': True}]}}
    Project.individuals = individuals
    Project.family_dic = family_dic
    
    assert Project.is_uncle_aunt_marriage_legal() == False
    
    return True


# In[528]:


# US40 Include input line numbers
# Create a small mock input with only one individual (detailed data)
def input_line_numbers():
    Project.input_file = "./Romeo_Juliet_Family.ged"
    document = Project.read_in("./Romeo_Juliet_Family.ged")
    person01 = document["INDI"][0]
    person02 = document["INDI"][1]
    fam = document["FAM"][0]
    
    #Test Romeo
    assert person01["INDI_LINE"] == 14
    assert person01["NAME_LINE"] == 15
    assert person01["SEX_LINE"] == 19
    assert person01["BIRT_LINE"] == 20
    assert person01["DEAT_LINE"] == 22
    assert person01["FAMS_LINE"] == 24
    #Test Juliet
    assert person02["INDI_LINE"] == 25
    assert person02["NAME_LINE"] == 26
    assert person02["SEX_LINE"] == 30
    assert person02["BIRT_LINE"] == 31
    assert person02["FAMS_LINE"] == 33
    #Test Romeo & Juliet's family
    assert fam["FAM_LINE"] == 34
    assert fam["HUSB_LINE"] == 35
    assert fam["WIFE_LINE"] == 36
    assert fam["MARR_LINE"] == 37
                           
    return True


# In[529]:


import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_Dates_After_Today_error(self):
        self.assertTrue(test_dates_error())
    def test_Dates_After_Today_pass(self):
        self.assertTrue(test_dates_pass())
    def test_Marriqge_Ater_14_error(self):
        self.assertTrue(test_not_legal_marriage())
    def test_Marriqge_Ater_14_pass(self):
        self.assertTrue(test_legal_marriage())
    def test_Less_Then_150_Years_Old_error(self):
        self.assertTrue(test_over_age_150())
    def test_Less_Then_150_Years_Old_pass(self):
        self.assertTrue(test_less_age_150())
    def test_List_Deceased_success(self):
        self.assertTrue(test_list_deceased_individuals_success())
    def test_List_Deceased_fail(self):
        self.assertTrue(test_list_deceased_individuals_error())
    def test_List_Living_Married_success(self):
        self.assertTrue(test_list_living_married_individuals_success())
    def test_List_Living_Married_fail(self):
        self.assertTrue(test_list_living_married_individuals_error())
    def test_More_Than_15_Siblings(self):
        self.assertTrue(test_more_than_15_siblings())
    def test_Less_Than_15_Siblings(self):
        self.assertTrue(test_less_than_15_siblings())
    def test_Different_Male_Last_Name(self):
        self.assertTrue(test_different_male_last_name())
    def test_Same_Male_Last_Name(self):
        self.assertTrue(test_same_male_last_name());
    def test_Birth_After_Marraige_Appended_To_Error(self):
        self.assertTrue(test_birth_after_marraige_appended_to_error());
    def test_Birth_Before_Marraige_Do_Nothing(self):
        self.assertTrue(test_birth_before_marraige_do_nothing());
    def test_unique_name_and_birth_pass(self):
        self.assertTrue(test_unique_name_and_birth_pass());
    def test_unique_name_and_birth_error(self):
        self.assertTrue(test_unique_name_and_birth_error());
    def test_unique_family_name_and_birth_pass(self):
        self.assertTrue(test_unique_family_name_and_birth_pass());
    def test_unique_family_name_and_birth_error(self):
        self.assertTrue(test_unique_family_name_and_birth_error());
    def test_aunts_and_uncles_pass(self):
        self.assertTrue(aunts_and_uncles_success());
    def test_aunts_and_uncles_fail(self):
        self.assertTrue(aunts_and_uncles_error());
    def test_input_line_numbers_pass(self):
        self.assertTrue(input_line_numbers());

        
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)


# In[ ]:




