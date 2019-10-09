#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pytest
import unittest
import mock
import Project


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


def test_birth_before_marraige_do_nothing():
    family_dic = {'@F1@':{'MARR':'1968-6-4','husband_object':{'INDI':'@I1@','BIRT':'1950-11-8'},'wife_object':{'INDI':'@I2@','BIRT':'1960-11-8'}}}
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.is_birth_before_marraige()
    
    assert len(Project.error_array) == 0
    return True


# In[ ]:


def test_birth_after_marraige_appended_to_error():
    family_dic = {'@F1@':{'MARR':'1968-6-4','husband_object':{'INDI':'@I1@','BIRT':'1970-11-8'},'wife_object':{'INDI':'@I2@','BIRT':'1960-11-8'}}}
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.is_birth_before_marraige()
    
    assert Project.error_array[0] == "ERROR: INDIVIDUAL: US02: @I1@: Person has marriage date 1968-6-4 before birth date 1970-11-8"
    return True


# In[ ]:


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


# In[4]:


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


# In[5]:


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


# In[6]:


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


# In[7]:


# User_Story_29: List all deceased individuals in a GEDCOM file
# Success test 
@mock.patch("Project.printTable")
def test_list_deceased_individuals_success(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    current_dic = {'@I6@': {'INDI': '@I6@', 'NAME': 'Stephen /Chang/', 'SEX': 'M', 'BIRT': '1935-12-5', 'DEAT': '2005-4-15', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'AGE': '70', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listDeceased()
    mock_printTable.assert_called_with("US29: Deceased People Table", allFields, tagNames, current_dic)
    return True


# In[ ]:


# User_Story_29: List all deceased individuals in a GEDCOM file
# Failed test: Person is dead but has no Death Date
@mock.patch("Project.printTable")
def test_list_deceased_individuals_error(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    current_dic = {'@I6@': {'INDI': '@I6@', 'NAME': 'David /Chang/', 'SEX': 'M', 'BIRT': '2002-12-5', 'DEAT': 'NA', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F7@'], 'AGE': '79', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listDeceased()
    mock_printTable.assert_called_with("US29: Deceased People Table", allFields, tagNames, {}) #provide empty dictionary so that it won't overwrite
    return True


# In[ ]:


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


# In[ ]:


# User_Story_30: List all living married people in a GEDCOM file
# Failed test
@mock.patch("Project.printTable")
def test_list_living_married_individuals_error(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
    current_dic = {'@I4@': {'INDI': '@I1@', 'NAME': 'Michael /Chang/', 'SEX': 'M', 'BIRT': '1958-9-6', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'DEAT': '2002-9-6', 'AGE': '61', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listLivingMarried()
    mock_printTable.assert_called_with("US30: Living & Married People Table", allFields, tagNames, {}) #provide empty dictionary so that it won't overwrite
    return True


# In[ ]:


def test_more_than_15_siblings():
    family_dic = {'@F1@':{'FAM_CHILD':['@I1@','@I10@','@I11@','@I12@','@I13@','@I14@','@I15@','@I16@','@I17@','@I18@','@I19@','@I20@','@I21@','@I22@','@I23@','@I24@','@I24@']}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_sibling_count()

    assert Project.anomaly_array[0] == 'ANOMALY: FAMILY: US16: @F1@: Family has 17 siblings which is more than 15 siblings'
    return True


# In[ ]:


def test_less_than_15_siblings():
    family_dic = {'@F1@':{'FAM_CHILD':['@I1@']}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_sibling_count()

    assert len(Project.anomaly_array) == 0
    return True
    


# In[ ]:


def test_different_male_last_name():
    family_dic = {'@F1@':{'HUSB_NAME':'Harry /Potter/','FAM_CHILD':['@I1@','@I10@'],'children_objects':[{'INDI':'@I1@', 'SEX':'M','NAME':'Chandler /Bing/'},{'INDI':'@I10@', 'SEX':'M','NAME':'Chandler /Potter/'}]}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_last_names()
    assert Project.anomaly_array[0] == 'ANOMALY: INDIVIDUAL: US16: @I1@: Individual has different last name Bing than family Potter'
    return True


# In[ ]:


def test_same_male_last_name():
    family_dic = {'@F1@':{'HUSB_NAME':'Harry /Potter/','FAM_CHILD':['@I1@','@I10@'],'children_objects':[{'INDI':'@I1@', 'SEX':'M','NAME':'Joey /Potter/'},{'INDI':'@I10@', 'SEX':'M','NAME':'Chandler /Potter/'}]}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_last_names()

    assert len(Project.anomaly_array) == 0
    return True


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


def test_check_positive_for_bigamy():
    family_dic = {'@F1@': {'MARR': '2010-10-18','DIV': '2015-12-10'}, '@F2@': {'MARR': '2012-10-18','DIV': '2018-12-10'}}
    individuals = {'@I1': {'SPOUSE': ['@F1@', '@F2@']}, '@I2': {'SPOUSE': ['@F1@']}, '@I3': {'SPOUSE': ['@F2@']}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.individuals = individuals
    Project.check_for_bigamy()
    
    assert Project.anomaly_array[0] == 'ANOMALY: INDIVIDUAL: US11: @I1: Performing bigamy'
    
    return True


# In[ ]:


def test_check_negative_for_bigamy():
    family_dic = {'@F1@': {'MARR': '2010-10-18','DIV': '2015-12-10'}, '@F2@': {'MARR': '2016-10-18','DIV': '2018-12-10'}}
    individuals = {'@I1': {'SPOUSE': ['@F1@', '@F2@']}, '@I2': {'SPOUSE': ['@F1@']}, '@I3': {'SPOUSE': ['@F2@']}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.individuals = individuals
    Project.check_for_bigamy()
    
    assert len(Project.anomaly_array) == 0
    
    return True


# In[ ]:


def test_check_positive_parent_child_marriage():
    family_dic = {'@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@','FAM_CHILD': ['@I3@']},'@F2@': {'HUSB': '@I3@','WIFE': '@I2@'}}
    individuals = {'@I1@': {'SPOUSE': ['@F1@']}, '@I2@': {'SPOUSE': ['@F1@', '@F2@']},'@I3@': {'SPOUSE': ['@F2@']}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.individuals = individuals
    Project.check_parent_child_marriage()
    
    assert Project.anomaly_array[0] == "ANOMALY: INDIVIDUAL: US17: @I2@: Individual married to child @I3@"
    
    return True
    


# In[ ]:


def test_check_negative_parent_child_marriage():
    family_dic = {'@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@','FAM_CHILD': ['@I3@']},'@F2@': {'HUSB': '@I4@','WIFE': '@I2@'}}
    individuals = {'@I1@': {'SPOUSE': ['@F1@']}, '@I2@': {'SPOUSE': ['@F1@', '@F2@']},'@I3@': {'SPOUSE': 'NA'}, '@I4@': {'SPOUSE': ['@F2@']}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.individuals = individuals
    Project.check_parent_child_marriage()
    
    assert len(Project.anomaly_array) == 0
    
    return True


# In[ ]:


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
    def test_Check_Positive_For_Bigamy(self):
        self.assertTrue(test_check_positive_for_bigamy());
    def test_Check_Negative_For_Bigamy(self):
        self.assertTrue(test_check_negative_for_bigamy());
    def test_Check_Positive_Parent_Child_Marriage(self):
        self.assertTrue(test_check_positive_parent_child_marriage());
    def test_Check_Negative_Parent_Child_Marriage(self):
        self.assertTrue(test_check_negative_parent_child_marriage());

        
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)


# In[ ]:




