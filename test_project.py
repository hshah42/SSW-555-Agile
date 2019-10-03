#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytest
import unittest
import mock
import Project


# In[2]:


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


# In[3]:


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


# In[4]:


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


# In[5]:


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


# In[6]:


import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_unique_name_and_birth_pass(self):
        self.assertTrue(test_unique_name_and_birth_pass());
    def test_unique_name_and_birth_error(self):
        self.assertTrue(test_unique_name_and_birth_error());
    def test_unique_family_name_and_birth_pass(self):
        self.assertTrue(test_unique_family_name_and_birth_pass());
    def test_unique_family_name_and_birth_error(self):
        self.assertTrue(test_unique_family_name_and_birth_error());

        
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)


# In[ ]:




