#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pytest
import unittest
import mock
import Project
from io import StringIO
import sys


# In[36]:


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
    
    fake_out = StringIO()
    sys.stdout = fake_out
    
    Project.is_marriage_legal()

    sys.stdout = sys.__stdout__
    return fake_out.getvalue()=='ANOMOLY: INDIVIDUAL: US07: @I18@: Father George /Nickson/ of family @F8@ is younger than 14.\nANOMOLY: INDIVIDUAL: US07: @I13@: Wife Kitty /Nilson/ of family @F8@ is younger than 14.\n'


# In[37]:


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
    
    fake_out = StringIO()
    sys.stdout = fake_out
    
    Project.is_marriage_legal()

    sys.stdout = sys.__stdout__
    return fake_out.getvalue()==""


# In[38]:


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
    
    fake_out = StringIO()
    sys.stdout = fake_out
    
    Project.is_marriage_legal()

    sys.stdout = sys.__stdout__
    return fake_out.getvalue()==""


# In[39]:


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
  'BIRT': '1920-12-10',
  'DEAT': '2002-6-2',
  'INDI_CHILD': 'NA',
  'SPOUSE': ['@F1@'],
  'AGE': '81',
  'ALIVE': False}}
                 
    Project.individuals = individuals
    
    fake_out = StringIO()
    sys.stdout = fake_out
    
    Project.is_age_legal()

    sys.stdout = sys.__stdout__
    return fake_out.getvalue()=='ANOMOLY: INDIVIDUAL: US10: @I1@: Individual Jimmy /Colon/ is older than 150.\n'


# In[40]:


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
    
    fake_out = StringIO()
    sys.stdout = fake_out
    
    Project.is_age_legal()

    sys.stdout = sys.__stdout__
    return fake_out.getvalue()==""


# In[41]:


# User_Story_29: List all deceased individuals in a GEDCOM file
# Success test 
@mock.patch("Project.printTable")
def test_list_deceased_individuals_success(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    current_dic = {'@I6@': {'INDI': '@I6@', 'NAME': 'Stephen /Chang/', 'SEX': 'M', 'BIRT': '1935-12-5', 'DEAT': '2005-4-15', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'AGE': '70', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listDeceased()
    mock_printTable.assert_called_with(allFields, tagNames, current_dic)


# In[42]:


# User_Story_29: List all deceased individuals in a GEDCOM file
# Failed test: Person is dead but has no Death Date
@mock.patch("Project.printTable")
def test_list_deceased_individuals_error(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    current_dic = {'@I6@': {'INDI': '@I6@', 'NAME': 'David /Chang/', 'SEX': 'M', 'BIRT': '2002-12-5', 'DEAT': 'NA', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F7@'], 'AGE': '79', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listDeceased()
    mock_printTable.assert_called_with(allFields, tagNames, {}) #provide empty dictionary so that it won't overwrite


# In[43]:


# User_Story_30: List all living married people in a GEDCOM file
# Success test
@mock.patch("Project.printTable")
def test_list_living_married_individuals_success(mock_printTable):

    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
    current_dic = {'@I1@': {'INDI': '@I1@', 'NAME': 'Johnny /Chang/', 'SEX': 'M', 'BIRT': '1958-9-6', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F1@'], 'DEAT': 'NA', 'AGE': '61', 'ALIVE': True}}
    Project.individuals = current_dic
    Project.listLivingMarried()
    mock_printTable.assert_called_with(allFields, tagNames, current_dic)


# In[44]:


# User_Story_30: List all living married people in a GEDCOM file
# Failed test
@mock.patch("Project.printTable")
def test_list_living_married_individuals_error(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
    current_dic = {'@I4@': {'INDI': '@I1@', 'NAME': 'Michael /Chang/', 'SEX': 'M', 'BIRT': '1958-9-6', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'DEAT': '2002-9-6', 'AGE': '61', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listLivingMarried()
    mock_printTable.assert_called_with(allFields, tagNames, {}) #provide empty dictionary so that it won't overwrite


# In[45]:


# Tests user stories that list out items
test_list_deceased_individuals_success()
test_list_deceased_individuals_error()
test_list_living_married_individuals_success()
test_list_living_married_individuals_error()


# In[46]:


import unittest

class TestStringMethods(unittest.TestCase):

    def test_not_legal_marriage(self):
        self.assertTrue(test_not_legal_marriage())
    def test_legal_marriage(self):
        self.assertTrue(test_legal_marriage())
    def test_over_age_150(self):
        self.assertTrue(test_over_age_150())
    def test_less_age_150(self):
        self.assertTrue(test_less_age_150())
    

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)


# In[ ]:




