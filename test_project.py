
# coding: utf-8

# In[177]:


import pytest
import unittest
import mock
import Project
from unittest.mock import MagicMock


# In[178]:


def test_divorce_before_death_fail():
    family_dic = {
                  '@F1@': {'FAM': '@F1@',
                  'FAM_LINE': 433,
                  'HUSB_NAME': 'Samuel /Venzon/',
                  'HUSB_LINE': 434,
                  'HUSB': '@I6@',
                  'WIFE_NAME': 'Willodean /Malagon/',
                  'WIFE_LINE': 435,
                  'WIFE': '@I1@',
                  'FAM_CHILD': ['@I7@', '@I13@'],
                  'CHIL_LINE_@I7@': 436,
                  'CHIL': '@I13@',
                  'CHIL_LINE': 437,
                  'CHIL_LINE_@I13@': 437,
                  'MARR_LINE': 438,
                  'MARR': '1970-7-7',
                  'DIV': '1971-7-7',
                  "DIV_LINE": 530,
                  'husband_object': {'INDI': '@I6@',
                   'INDI_LINE': 67,
                   'NAME': 'Samuel /Venzon/',
                   'NAME_LINE': 68,
                   'SEX': 'M',
                   'SEX_LINE': 72,
                   'BIRT_LINE': 73,
                   'BIRT': '1958-12-6',
                   'INDI_CHILD': 'NA',
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 75,
                   'DEAT': '1971-7-1',
                   'AGE': '110',
                   'ALIVE': True},
                  'wife_object': {'INDI': '@I1@',
                   'INDI_LINE': 14,
                   'NAME': 'Willodean /Malagon/',
                   'NAME_LINE': 15,
                   'SEX': 'F',
                   'SEX_LINE': 19,
                   'BIRT_LINE': 20,
                   'BIRT': '1958-7-7',
                   'DEAT_LINE': 22,
                   'DEAT': '1972-6-20',
                   'INDI_CHILD': ['@F2@'],
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 24,
                   'FAMC_LINE': 25,
                   'AGE': '75',
                   'ALIVE': False},
                  'children_objects': [{'INDI': '@I7@',
                    'INDI_LINE': 76,
                    'NAME': 'Byron /Vezon/',
                    'NAME_LINE': 77,
                    'SEX': 'M',
                    'SEX_LINE': 81,
                    'BIRT_LINE': 82,
                    'BIRT': '1973-7-6',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': ['@F6@'],
                    'FAMS_LINE': 84,
                    'FAMC_LINE': 85,
                    'DEAT': 'NA',
                    'AGE': '10',
                    'ALIVE': True},
                   {'INDI': '@I13@',
                    'INDI_LINE': 133,
                    'NAME': 'Beth /Venzon/',
                    'NAME_LINE': 134,
                    'SEX': 'F',
                    'SEX_LINE': 138,
                    'BIRT_LINE': 139,
                    'BIRT': '1975-7-8',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': 'NA',
                    'FAMC_LINE': 141,
                    'DEAT': 'NA',
                    'AGE': '44',
                    'ALIVE': True}]}
                 }
    
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.check_divorce_before_death()

    return Project.error_array==['ERROR: FAMILY: US06: 530: @F1@: Divorce 1971-7-7 happened after the death of husband 1971-7-1.']


# In[179]:


def test_divorce_before_death_pass():
    family_dic = {
                  '@F1@': {'FAM': '@F1@',
                  'FAM_LINE': 433,
                  'HUSB_NAME': 'Samuel /Venzon/',
                  'HUSB_LINE': 434,
                  'HUSB': '@I6@',
                  'WIFE_NAME': 'Willodean /Malagon/',
                  'WIFE_LINE': 435,
                  'WIFE': '@I1@',
                  'FAM_CHILD': ['@I7@', '@I13@'],
                  'CHIL_LINE_@I7@': 436,
                  'CHIL': '@I13@',
                  'CHIL_LINE': 437,
                  'CHIL_LINE_@I13@': 437,
                  'MARR_LINE': 438,
                  'MARR': '1970-7-7',
                  'DIV': '1972-7-8',
                  "DIV_LINE": 530,
                  'husband_object': {'INDI': '@I6@',
                   'INDI_LINE': 67,
                   'NAME': 'Samuel /Venzon/',
                   'NAME_LINE': 68,
                   'SEX': 'M',
                   'SEX_LINE': 72,
                   'BIRT_LINE': 73,
                   'BIRT': '1958-12-6',
                   'INDI_CHILD': 'NA',
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 75,
                   'DEAT': '1973-7-1',
                   'AGE': '110',
                   'ALIVE': True},
                  'wife_object': {'INDI': '@I1@',
                   'INDI_LINE': 14,
                   'NAME': 'Willodean /Malagon/',
                   'NAME_LINE': 15,
                   'SEX': 'F',
                   'SEX_LINE': 19,
                   'BIRT_LINE': 20,
                   'BIRT': '1958-7-7',
                   'DEAT_LINE': 22,
                   'DEAT': '1979-6-20',
                   'INDI_CHILD': ['@F2@'],
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 24,
                   'FAMC_LINE': 25,
                   'AGE': '75',
                   'ALIVE': False},
                  'children_objects': [{'INDI': '@I7@',
                    'INDI_LINE': 76,
                    'NAME': 'Byron /Vezon/',
                    'NAME_LINE': 77,
                    'SEX': 'M',
                    'SEX_LINE': 81,
                    'BIRT_LINE': 82,
                    'BIRT': '1973-7-6',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': ['@F6@'],
                    'FAMS_LINE': 84,
                    'FAMC_LINE': 85,
                    'DEAT': 'NA',
                    'AGE': '10',
                    'ALIVE': True},
                   {'INDI': '@I13@',
                    'INDI_LINE': 133,
                    'NAME': 'Beth /Venzon/',
                    'NAME_LINE': 134,
                    'SEX': 'F',
                    'SEX_LINE': 138,
                    'BIRT_LINE': 139,
                    'BIRT': '1975-7-8',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': 'NA',
                    'FAMC_LINE': 141,
                    'DEAT': 'NA',
                    'AGE': '44',
                    'ALIVE': True}]}
                 }
    
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.check_divorce_before_death()

    return len(Project.error_array)==0


# In[180]:


def test_parents_not_too_old_fail():
    family_dic = {
                  '@F1@': {'FAM': '@F1@',
                  'FAM_LINE': 433,
                  'HUSB_NAME': 'Samuel /Venzon/',
                  'HUSB_LINE': 434,
                  'HUSB': '@I6@',
                  'WIFE_NAME': 'Willodean /Malagon/',
                  'WIFE_LINE': 435,
                  'WIFE': '@I1@',
                  'FAM_CHILD': ['@I7@', '@I13@'],
                  'CHIL_LINE_@I7@': 436,
                  'CHIL': '@I13@',
                  'CHIL_LINE': 437,
                  'CHIL_LINE_@I13@': 437,
                  'MARR_LINE': 438,
                  'MARR': '1970-7-7',
                  'DIV': '1972-7-8',
                  "DIV_LINE": 530,
                  'husband_object': {'INDI': '@I6@',
                   'INDI_LINE': 67,
                   'NAME': 'Samuel /Venzon/',
                   'NAME_LINE': 68,
                   'SEX': 'M',
                   'SEX_LINE': 72,
                   'BIRT_LINE': 73,
                   'BIRT': '1958-12-6',
                   'INDI_CHILD': 'NA',
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 75,
                   'DEAT': '1971-7-1',
                   'AGE': '110',
                   'ALIVE': True},
                  'wife_object': {'INDI': '@I1@',
                   'INDI_LINE': 14,
                   'NAME': 'Willodean /Malagon/',
                   'NAME_LINE': 15,
                   'SEX': 'F',
                   'SEX_LINE': 19,
                   'BIRT_LINE': 20,
                   'BIRT': '1958-7-7',
                   'DEAT_LINE': 22,
                   'DEAT': '1970-6-20',
                   'INDI_CHILD': ['@F2@'],
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 24,
                   'FAMC_LINE': 25,
                   'AGE': '75',
                   'ALIVE': False},
                  'children_objects': [{'INDI': '@I7@',
                    'INDI_LINE': 76,
                    'NAME': 'Byron /Vezon/',
                    'NAME_LINE': 77,
                    'SEX': 'M',
                    'SEX_LINE': 81,
                    'BIRT_LINE': 82,
                    'BIRT': '1973-7-6',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': ['@F6@'],
                    'FAMS_LINE': 84,
                    'FAMC_LINE': 85,
                    'DEAT': 'NA',
                    'AGE': '10',
                    'ALIVE': True},
                   {'INDI': '@I13@',
                    'INDI_LINE': 133,
                    'NAME': 'Beth /Venzon/',
                    'NAME_LINE': 134,
                    'SEX': 'F',
                    'SEX_LINE': 138,
                    'BIRT_LINE': 139,
                    'BIRT': '1975-7-8',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': 'NA',
                    'FAMC_LINE': 141,
                    'DEAT': 'NA',
                    'AGE': '44',
                    'ALIVE': True}]}
                 }
    
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.check_parents_not_too_old()

    return Project.error_array==['ERROR: INDIVIDUAL: US12: 67: @F1@: Father is 100 older than the child @I7@.',
 'ERROR: FAMILY: US12: 14: @F1@: Wife is 65 older than the child @I7@.']


# In[181]:


def test_parents_not_too_old_pass():
    family_dic = {
                  '@F1@': {'FAM': '@F1@',
                  'FAM_LINE': 433,
                  'HUSB_NAME': 'Samuel /Venzon/',
                  'HUSB_LINE': 434,
                  'HUSB': '@I6@',
                  'WIFE_NAME': 'Willodean /Malagon/',
                  'WIFE_LINE': 435,
                  'WIFE': '@I1@',
                  'FAM_CHILD': ['@I7@', '@I13@'],
                  'CHIL_LINE_@I7@': 436,
                  'CHIL': '@I13@',
                  'CHIL_LINE': 437,
                  'CHIL_LINE_@I13@': 437,
                  'MARR_LINE': 438,
                  'MARR': '1970-7-7',
                  'DIV': '1972-7-8',
                  "DIV_LINE": 530,
                  'husband_object': {'INDI': '@I6@',
                   'INDI_LINE': 67,
                   'NAME': 'Samuel /Venzon/',
                   'NAME_LINE': 68,
                   'SEX': 'M',
                   'SEX_LINE': 72,
                   'BIRT_LINE': 73,
                   'BIRT': '1958-12-6',
                   'INDI_CHILD': 'NA',
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 75,
                   'DEAT': '1971-7-1',
                   'AGE': '70',
                   'ALIVE': True},
                  'wife_object': {'INDI': '@I1@',
                   'INDI_LINE': 14,
                   'NAME': 'Willodean /Malagon/',
                   'NAME_LINE': 15,
                   'SEX': 'F',
                   'SEX_LINE': 19,
                   'BIRT_LINE': 20,
                   'BIRT': '1958-7-7',
                   'DEAT_LINE': 22,
                   'DEAT': '1970-6-20',
                   'INDI_CHILD': ['@F2@'],
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 24,
                   'FAMC_LINE': 25,
                   'AGE': '65',
                   'ALIVE': False},
                  'children_objects': [{'INDI': '@I7@',
                    'INDI_LINE': 76,
                    'NAME': 'Byron /Vezon/',
                    'NAME_LINE': 77,
                    'SEX': 'M',
                    'SEX_LINE': 81,
                    'BIRT_LINE': 82,
                    'BIRT': '1973-7-6',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': ['@F6@'],
                    'FAMS_LINE': 84,
                    'FAMC_LINE': 85,
                    'DEAT': 'NA',
                    'AGE': '20',
                    'ALIVE': True},
                   {'INDI': '@I13@',
                    'INDI_LINE': 133,
                    'NAME': 'Beth /Venzon/',
                    'NAME_LINE': 134,
                    'SEX': 'F',
                    'SEX_LINE': 138,
                    'BIRT_LINE': 139,
                    'BIRT': '1975-7-8',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': 'NA',
                    'FAMC_LINE': 141,
                    'DEAT': 'NA',
                    'AGE': '44',
                    'ALIVE': True}]}
                 }
    
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.check_parents_not_too_old()

    return len(Project.error_array)==0


# In[182]:


# US03 - Happy Path Test Case

def test_is_birth_before_death():
    individuals = {
                  '@I1@': {'INDI': '@I1@',
                  'INDI_LINE': 14,
                  'NAME': 'Willodean /Malagon/',
                  'NAME_LINE': 15,
                  'SEX': 'F',
                  'SEX_LINE': 19,
                  'BIRT_LINE': 20,
                  'BIRT': '1958-7-7',
                  'DEAT_LINE': 22,
                  'DEAT': '1974-6-20',
                  'INDI_CHILD': ['@F2@'],
                  'SPOUSE': ['@F1@'],
                  'FAMS_LINE': 24,
                  'FAMC_LINE': 25,
                  'AGE': '15',
                  'ALIVE': False}
                 }
    Project.individuals = individuals
    Project.error_array = []
    Project.is_birth_before_death()

    return len(Project.error_array) == 0


# In[183]:


#US03 - Sad Path Test Case
#  return Project.error_array==['ERROR: INDIVIDUAL: US12: 67: @F1@: Father is 100 older than the child @I7@.',
#  'ERROR: FAMILY: US12: 14: @F1@: Wife is 65 older than the child @I7@.']

def test_is_birth_before_death_fail():
    individuals = {
                  '@I1@': {'INDI': '@I1@',
                  'INDI_LINE': 14,
                  'NAME': 'Willodean /Malagon/',
                  'NAME_LINE': 15,
                  'SEX': 'F',
                  'SEX_LINE': 19,
                  'BIRT_LINE': 20,
                  'BIRT': '1975-7-7',
                  'DEAT_LINE': 22,
                  'DEAT': '1974-6-20',
                  'INDI_CHILD': ['@F2@'],
                  'SPOUSE': ['@F1@'],
                  'FAMS_LINE': 24,
                  'FAMC_LINE': 25,
                  'AGE': '15',
                  'ALIVE': False}
                 }
    Project.individuals = individuals
    Project.error_array = []
    Project.is_birth_before_death()

    return Project.error_array==['ERROR: INDIVIDUAL: US03: @I1@: Individual has Birth date 1975-7-7 after Death Date 1974-6-20']


# In[184]:


# US04 - Happy Path Test Case

def test_is_marriage_after_divorce():
    individuals = {
                  '@I1@': {'INDI': '@I1@',
                  'INDI_LINE': 14,
                  'NAME': 'Willodean /Malagon/',
                  'NAME_LINE': 15,
                  'SEX': 'F',
                  'SEX_LINE': 19,
                  'BIRT_LINE': 20,
                  'BIRT': '1958-7-7',
                  'DEAT_LINE': 22,
                  'DEAT': '1974-6-20',
                  'INDI_CHILD': ['@F2@'],
                  'SPOUSE': ['@F1@'],
                  'FAMS_LINE': 24,
                  'FAMC_LINE': 25,
                  'AGE': '15',
                  'ALIVE': False}
                 }
    
    family_dic = {
                  '@F1@': {'FAM': '@F1@',
                  'FAM_LINE': 433,
                  'HUSB_NAME': 'Samuel /Venzon/',
                  'HUSB_LINE': 434,
                  'HUSB': '@I6@',
                  'WIFE_NAME': 'Willodean /Malagon/',
                  'WIFE_LINE': 435,
                  'WIFE': '@I1@',
                  'FAM_CHILD': ['@I7@', '@I13@'],
                  'CHIL_LINE_@I7@': 436,
                  'CHIL': '@I13@',
                  'CHIL_LINE': 437,
                  'CHIL_LINE_@I13@': 437,
                  'MARR_LINE': 438,
                  'MARR': '1970-7-7',
                  'DIV': '1971-7-7',
                  'husband_object': {'INDI': '@I6@',
                   'INDI_LINE': 67,
                   'NAME': 'Samuel /Venzon/',
                   'NAME_LINE': 68,
                   'SEX': 'M',
                   'SEX_LINE': 72,
                   'BIRT_LINE': 73,
                   'BIRT': '1958-12-6',
                   'INDI_CHILD': 'NA',
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 75,
                   'DEAT': 'NA',
                   'AGE': '60',
                   'ALIVE': True},
                  'wife_object': {'INDI': '@I1@',
                   'INDI_LINE': 14,
                   'NAME': 'Willodean /Malagon/',
                   'NAME_LINE': 15,
                   'SEX': 'F',
                   'SEX_LINE': 19,
                   'BIRT_LINE': 20,
                   'BIRT': '1958-7-7',
                   'DEAT_LINE': 22,
                   'DEAT': '1974-6-20',
                   'INDI_CHILD': ['@F2@'],
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 24,
                   'FAMC_LINE': 25,
                   'AGE': '15',
                   'ALIVE': False},
                  'children_objects': [{'INDI': '@I7@',
                    'INDI_LINE': 76,
                    'NAME': 'Byron /Vezon/',
                    'NAME_LINE': 77,
                    'SEX': 'M',
                    'SEX_LINE': 81,
                    'BIRT_LINE': 82,
                    'BIRT': '1973-7-6',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': ['@F6@'],
                    'FAMS_LINE': 84,
                    'FAMC_LINE': 85,
                    'DEAT': 'NA',
                    'AGE': '46',
                    'ALIVE': True},
                   {'INDI': '@I13@',
                    'INDI_LINE': 133,
                    'NAME': 'Beth /Venzon/',
                    'NAME_LINE': 134,
                    'SEX': 'F',
                    'SEX_LINE': 138,
                    'BIRT_LINE': 139,
                    'BIRT': '1975-7-8',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': 'NA',
                    'FAMC_LINE': 141,
                    'DEAT': 'NA',
                    'AGE': '44',
                    'ALIVE': True}]}
                 }
    
    
    Project.individuals = individuals
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.is_marriage_after_divorce()

    return len(Project.anomaly_array) == 0


# In[185]:


# US04 - Sad Path Test Case 
def test_is_marriage_after_divorce_error():
    individuals = {
                  '@I1@': {'INDI': '@I1@',
                  'INDI_LINE': 14,
                  'NAME': 'Willodean /Malagon/',
                  'NAME_LINE': 15,
                  'SEX': 'F',
                  'SEX_LINE': 19,
                  'BIRT_LINE': 20,
                  'BIRT': '1958-7-7',
                  'DEAT_LINE': 22,
                  'DEAT': '1974-6-20',
                  'INDI_CHILD': ['@F2@'],
                  'SPOUSE': ['@F1@'],
                  'FAMS_LINE': 24,
                  'FAMC_LINE': 25,
                  'AGE': '15',
                  'ALIVE': False}
                 }
    
    family_dic = {
                  '@F1@': {'FAM': '@F1@',
                  'FAM_LINE': 433,
                  'HUSB_NAME': 'Samuel /Venzon/',
                  'HUSB_LINE': 434,
                  'HUSB': '@I6@',
                  'WIFE_NAME': 'Willodean /Malagon/',
                  'WIFE_LINE': 435,
                  'WIFE': '@I1@',
                  'FAM_CHILD': ['@I7@', '@I13@'],
                  'CHIL_LINE_@I7@': 436,
                  'CHIL': '@I13@',
                  'CHIL_LINE': 437,
                  'CHIL_LINE_@I13@': 437,
                  'MARR_LINE': 438,
                  'MARR': '1970-7-7',
                  'DIV': '1969-7-7',
                  'husband_object': {'INDI': '@I6@',
                   'INDI_LINE': 67,
                   'NAME': 'Samuel /Venzon/',
                   'NAME_LINE': 68,
                   'SEX': 'M',
                   'SEX_LINE': 72,
                   'BIRT_LINE': 73,
                   'BIRT': '1958-12-6',
                   'INDI_CHILD': 'NA',
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 75,
                   'DEAT': 'NA',
                   'AGE': '60',
                   'ALIVE': True},
                  'wife_object': {'INDI': '@I1@',
                   'INDI_LINE': 14,
                   'NAME': 'Willodean /Malagon/',
                   'NAME_LINE': 15,
                   'SEX': 'F',
                   'SEX_LINE': 19,
                   'BIRT_LINE': 20,
                   'BIRT': '1958-7-7',
                   'DEAT_LINE': 22,
                   'DEAT': '1974-6-20',
                   'INDI_CHILD': ['@F2@'],
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 24,
                   'FAMC_LINE': 25,
                   'AGE': '15',
                   'ALIVE': False},
                  'children_objects': [{'INDI': '@I7@',
                    'INDI_LINE': 76,
                    'NAME': 'Byron /Vezon/',
                    'NAME_LINE': 77,
                    'SEX': 'M',
                    'SEX_LINE': 81,
                    'BIRT_LINE': 82,
                    'BIRT': '1973-7-6',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': ['@F6@'],
                    'FAMS_LINE': 84,
                    'FAMC_LINE': 85,
                    'DEAT': 'NA',
                    'AGE': '46',
                    'ALIVE': True},
                   {'INDI': '@I13@',
                    'INDI_LINE': 133,
                    'NAME': 'Beth /Venzon/',
                    'NAME_LINE': 134,
                    'SEX': 'F',
                    'SEX_LINE': 138,
                    'BIRT_LINE': 139,
                    'BIRT': '1975-7-8',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': 'NA',
                    'FAMC_LINE': 141,
                    'DEAT': 'NA',
                    'AGE': '44',
                    'ALIVE': True}]}
                 }
    
    
    Project.individuals = individuals
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.is_marriage_after_divorce()
    
    return Project.anomaly_array[0] == "ANOMALY: INDIVIDUAL: US04: 438: @I1@: Marriage Before Divorce - Marriage Date 1970-7-7 - Divorce Date 1969-7-7"


# In[186]:


# US05 - Happy Path Test Case
def test_is_marriage_after_death():
    individuals = {
                  '@I1@': {'INDI': '@I1@',
                  'INDI_LINE': 14,
                  'NAME': 'Willodean /Malagon/',
                  'NAME_LINE': 15,
                  'SEX': 'F',
                  'SEX_LINE': 19,
                  'BIRT_LINE': 20,
                  'BIRT': '1958-7-7',
                  'DEAT_LINE': 22,
                  'DEAT': '1974-6-20',
                  'INDI_CHILD': ['@F2@'],
                  'SPOUSE': ['@F1@'],
                  'FAMS_LINE': 24,
                  'FAMC_LINE': 25,
                  'AGE': '15',
                  'ALIVE': False}
                 }
    
    family_dic = {
                  '@F1@': {'FAM': '@F1@',
                  'FAM_LINE': 433,
                  'HUSB_NAME': 'Samuel /Venzon/',
                  'HUSB_LINE': 434,
                  'HUSB': '@I6@',
                  'WIFE_NAME': 'Willodean /Malagon/',
                  'WIFE_LINE': 435,
                  'WIFE': '@I1@',
                  'FAM_CHILD': ['@I7@', '@I13@'],
                  'CHIL_LINE_@I7@': 436,
                  'CHIL': '@I13@',
                  'CHIL_LINE': 437,
                  'CHIL_LINE_@I13@': 437,
                  'MARR_LINE': 438,
                  'MARR': '1970-7-7',
                  'DIV': '1971-7-7',
                  'husband_object': {'INDI': '@I6@',
                   'INDI_LINE': 67,
                   'NAME': 'Samuel /Venzon/',
                   'NAME_LINE': 68,
                   'SEX': 'M',
                   'SEX_LINE': 72,
                   'BIRT_LINE': 73,
                   'BIRT': '1958-12-6',
                   'INDI_CHILD': 'NA',
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 75,
                   'DEAT': 'NA',
                   'AGE': '60',
                   'ALIVE': True},
                  'wife_object': {'INDI': '@I1@',
                   'INDI_LINE': 14,
                   'NAME': 'Willodean /Malagon/',
                   'NAME_LINE': 15,
                   'SEX': 'F',
                   'SEX_LINE': 19,
                   'BIRT_LINE': 20,
                   'BIRT': '1958-7-7',
                   'DEAT_LINE': 22,
                   'DEAT': '1974-6-20',
                   'INDI_CHILD': ['@F2@'],
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 24,
                   'FAMC_LINE': 25,
                   'AGE': '15',
                   'ALIVE': False},
                  'children_objects': [{'INDI': '@I7@',
                    'INDI_LINE': 76,
                    'NAME': 'Byron /Vezon/',
                    'NAME_LINE': 77,
                    'SEX': 'M',
                    'SEX_LINE': 81,
                    'BIRT_LINE': 82,
                    'BIRT': '1973-7-6',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': ['@F6@'],
                    'FAMS_LINE': 84,
                    'FAMC_LINE': 85,
                    'DEAT': 'NA',
                    'AGE': '46',
                    'ALIVE': True},
                   {'INDI': '@I13@',
                    'INDI_LINE': 133,
                    'NAME': 'Beth /Venzon/',
                    'NAME_LINE': 134,
                    'SEX': 'F',
                    'SEX_LINE': 138,
                    'BIRT_LINE': 139,
                    'BIRT': '1975-7-8',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': 'NA',
                    'FAMC_LINE': 141,
                    'DEAT': 'NA',
                    'AGE': '44',
                    'ALIVE': True}]}
                 }
    
    
    Project.individuals = individuals
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.is_marriage_after_death()

    assert len(Project.anomaly_array) == 0
    return True


# In[187]:


# US05 - Sad Path Test Case
def test_is_marriage_after_death_error():
    individuals = {
                  '@I1@': {'INDI': '@I1@',
                  'INDI_LINE': 14,
                  'NAME': 'Willodean /Malagon/',
                  'NAME_LINE': 15,
                  'SEX': 'F',
                  'SEX_LINE': 19,
                  'BIRT_LINE': 20,
                  'BIRT': '1958-7-7',
                  'DEAT_LINE': 22,
                  'DEAT': '1969-6-20',
                  'INDI_CHILD': ['@F2@'],
                  'SPOUSE': ['@F1@'],
                  'FAMS_LINE': 24,
                  'FAMC_LINE': 25,
                  'AGE': '15',
                  'ALIVE': False}
                 }
    
    family_dic = {
                  '@F1@': {'FAM': '@F1@',
                  'FAM_LINE': 433,
                  'HUSB_NAME': 'Samuel /Venzon/',
                  'HUSB_LINE': 434,
                  'HUSB': '@I6@',
                  'WIFE_NAME': 'Willodean /Malagon/',
                  'WIFE_LINE': 435,
                  'WIFE': '@I1@',
                  'FAM_CHILD': ['@I7@', '@I13@'],
                  'CHIL_LINE_@I7@': 436,
                  'CHIL': '@I13@',
                  'CHIL_LINE': 437,
                  'CHIL_LINE_@I13@': 437,
                  'MARR_LINE': 438,
                  'MARR': '1970-7-7',
                  'DIV': '1971-7-7',
                  'husband_object': {'INDI': '@I6@',
                   'INDI_LINE': 67,
                   'NAME': 'Samuel /Venzon/',
                   'NAME_LINE': 68,
                   'SEX': 'M',
                   'SEX_LINE': 72,
                   'BIRT_LINE': 73,
                   'BIRT': '1958-12-6',
                   'INDI_CHILD': 'NA',
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 75,
                   'DEAT': 'NA',
                   'AGE': '60',
                   'ALIVE': True},
                  'wife_object': {'INDI': '@I1@',
                   'INDI_LINE': 14,
                   'NAME': 'Willodean /Malagon/',
                   'NAME_LINE': 15,
                   'SEX': 'F',
                   'SEX_LINE': 19,
                   'BIRT_LINE': 20,
                   'BIRT': '1958-7-7',
                   'DEAT_LINE': 22,
                   'DEAT': '1974-6-20',
                   'INDI_CHILD': ['@F2@'],
                   'SPOUSE': ['@F1@'],
                   'FAMS_LINE': 24,
                   'FAMC_LINE': 25,
                   'AGE': '15',
                   'ALIVE': False},
                  'children_objects': [{'INDI': '@I7@',
                    'INDI_LINE': 76,
                    'NAME': 'Byron /Vezon/',
                    'NAME_LINE': 77,
                    'SEX': 'M',
                    'SEX_LINE': 81,
                    'BIRT_LINE': 82,
                    'BIRT': '1973-7-6',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': ['@F6@'],
                    'FAMS_LINE': 84,
                    'FAMC_LINE': 85,
                    'DEAT': 'NA',
                    'AGE': '46',
                    'ALIVE': True},
                   {'INDI': '@I13@',
                    'INDI_LINE': 133,
                    'NAME': 'Beth /Venzon/',
                    'NAME_LINE': 134,
                    'SEX': 'F',
                    'SEX_LINE': 138,
                    'BIRT_LINE': 139,
                    'BIRT': '1975-7-8',
                    'INDI_CHILD': ['@F1@'],
                    'SPOUSE': 'NA',
                    'FAMC_LINE': 141,
                    'DEAT': 'NA',
                    'AGE': '44',
                    'ALIVE': True}]}
                 }
    
    
    Project.individuals = individuals
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.is_marriage_after_death()
    assert Project.anomaly_array[0] == "ANOMALY: INDIVIDUAL: US05: 438: @I1@: Marriage Before Death - Marriage Date 1970-7-7 - Death Date 1969-6-20"
    return True


# In[188]:


def test_death_before_marriage_fail():
    
    family_dic={'@F1@': {'FAM': '@F1@',
  'HUSB_NAME': 'Samuel /Venzon/',
  'HUSB': '@I6@',
  'WIFE_NAME': 'Willodean /Malagon/',
  'WIFE': '@I1@',
  'FAM_CHILD': ['@I7@', '@I13@'],
  'CHIL': '@I13@',
  'MARR': '1973-7-7',
  'DIV': '1980-12-1',
  'husband_object': {'INDI': '@I6@',
   'NAME': 'Samuel /Venzon/',
   'SEX': 'M',
   'BIRT': '1958-12-6',
   'INDI_CHILD': 'NA',
   'SPOUSE': ['@F1@'],
   'DEAT': 'NA',
   'AGE': '60',
   'ALIVE': True},
  'wife_object': {'INDI': '@I1@',
   'NAME': 'Willodean /Malagon/',
   'SEX': 'F',
   'BIRT': '1958-7-7',
   'INDI_CHILD': ['@F2@'],
   'SPOUSE': ['@F1@'],
   'DEAT': 'NA',
   'AGE': '61',
   'ALIVE': True},
  'children_objects': [{'INDI': '@I7@',
    'NAME': 'Byron /Vezon/',
    'SEX': 'M',
    'BIRT': '1973-7-6',
    'BIRT_LINE':100,
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': ['@F5@'],
    'DEAT': 'NA',
    'AGE': '46',
    'ALIVE': True},
   {'INDI': '@I13@',
    'NAME': 'Beth /Venzon/',
    'SEX': 'F',
    'BIRT': '1981-9-8',
    'BIRT_LINE':200,
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': 'NA',
    'DEAT': 'NA',
    'AGE': '44',
    'ALIVE': True}]}}
    
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.birth_before_marriage()

    return Project.anomaly_array==['ANOMALY: INDIVIDUAL: US08: 100: @I7@: Child was born at 1973-7-6 before marriage of parents 1973-7-7',
 'ANOMALY: INDIVIDUAL: US08: 200: @I13@: Child was born at 1981-9-8 after 9 month divorce of parents 1980-12-1']


# In[189]:


def test_death_before_marriage_pass():
    
    family_dic={'@F1@': {'FAM': '@F1@',
  'HUSB_NAME': 'Samuel /Venzon/',
  'HUSB': '@I6@',
  'WIFE_NAME': 'Willodean /Malagon/',
  'WIFE': '@I1@',
  'FAM_CHILD': ['@I7@', '@I13@'],
  'CHIL': '@I13@',
  'MARR': '1973-7-7',
  'DIV': 'NA',
  'husband_object': {'INDI': '@I6@',
   'NAME': 'Samuel /Venzon/',
   'SEX': 'M',
   'BIRT': '1958-12-6',
   'INDI_CHILD': 'NA',
   'SPOUSE': ['@F1@'],
   'DEAT': 'NA',
   'AGE': '60',
   'ALIVE': True},
  'wife_object': {'INDI': '@I1@',
   'NAME': 'Willodean /Malagon/',
   'SEX': 'F',
   'BIRT': '1958-7-7',
   'INDI_CHILD': ['@F2@'],
   'SPOUSE': ['@F1@'],
   'DEAT': 'NA',
   'AGE': '61',
   'ALIVE': True},
  'children_objects': [{'INDI': '@I7@',
    'NAME': 'Byron /Vezon/',
    'SEX': 'M',
    'BIRT': '1978-7-6',
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': ['@F5@'],
    'DEAT': 'NA',
    'AGE': '46',
    'ALIVE': True},
   {'INDI': '@I13@',
    'NAME': 'Beth /Venzon/',
    'SEX': 'F',
    'BIRT': '1978-7-8',
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': 'NA',
    'DEAT': 'NA',
    'AGE': '44',
    'ALIVE': True}]}}
    
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.birth_before_marriage()

    return len(Project.anomaly_array)==0


# In[190]:


def test_birth_before_death_fail():
    
    family_dic={'@F1@': {'FAM': '@F1@',
  'HUSB_NAME': 'Samuel /Venzon/',
  'HUSB': '@I6@',
  'WIFE_NAME': 'Willodean /Malagon/',
  'WIFE': '@I1@',
  'FAM_CHILD': ['@I7@', '@I13@'],
  'CHIL': '@I13@',
  'MARR': '1973-7-7',
  'DIV': 'NA',
  'husband_object': {'INDI': '@I6@',
   'NAME': 'Samuel /Venzon/',
   'SEX': 'M',
   'BIRT': '1958-12-6',
   'INDI_CHILD': 'NA',
   'SPOUSE': ['@F1@'],
   'DEAT': '1988-10-6',
   'AGE': '60',
   'ALIVE': True},
  'wife_object': {'INDI': '@I1@',
   'NAME': 'Willodean /Malagon/',
   'SEX': 'F',
   'BIRT': '1958-7-7',
   'INDI_CHILD': ['@F2@'],
   'SPOUSE': ['@F1@'],
   'DEAT': '1987-12-6',
   'AGE': '61',
   'ALIVE': True},
  'children_objects': [{'INDI': '@I7@',
    'NAME': 'Byron /Vezon/',
    'SEX': 'M',
    'BIRT': '1988-1-9',
    'BIRT_LINE':100,
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': ['@F5@'],
    'DEAT': 'NA',
    'AGE': '46',
    'ALIVE': True},
   {'INDI': '@I13@',
    'NAME': 'Beth /Venzon/',
    'SEX': 'F',
    'BIRT': '1989-7-8',
    'BIRT_LINE':200,
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': 'NA',
    'DEAT': 'NA',
    'AGE': '44',
    'ALIVE': True}]}}
    
    
    Project.family_dic = family_dic
    Project.error_array = []
    Project.birth_before_death()

    return Project.error_array==['ERROR: INDIVIDUAL: US09: 100: @I7@: Child was born at 1988-1-9 after death of mother 1987-12-6',
 'ERROR: INDIVIDUAL: US09: 200: @I13@: Child was born at 1989-7-8 after death of mother 1987-12-6',
 'ERROR: INDIVIDUAL: US09: 200: @I13@: Child was born at 1989-7-8 after 9 month death of father 1988-10-6']


# In[191]:


def test_birth_before_death_pass():
    
    family_dic={'@F1@': {'FAM': '@F1@',
  'HUSB_NAME': 'Samuel /Venzon/',
  'HUSB': '@I6@',
  'WIFE_NAME': 'Willodean /Malagon/',
  'WIFE': '@I1@',
  'FAM_CHILD': ['@I7@', '@I13@'],
  'CHIL': '@I13@',
  'MARR': '1973-7-7',
  'DIV': 'NA',
  'husband_object': {'INDI': '@I6@',
   'NAME': 'Samuel /Venzon/',
   'SEX': 'M',
   'BIRT': '1958-12-6',
   'INDI_CHILD': 'NA',
   'SPOUSE': ['@F1@'],
   'DEAT': '1988-10-6',
   'AGE': '60',
   'ALIVE': True},
  'wife_object': {'INDI': '@I1@',
   'NAME': 'Willodean /Malagon/',
   'SEX': 'F',
   'BIRT': '1958-7-7',
   'INDI_CHILD': ['@F2@'],
   'SPOUSE': ['@F1@'],
   'DEAT': '1987-12-6',
   'AGE': '61',
   'ALIVE': True},
  'children_objects': [{'INDI': '@I7@',
    'NAME': 'Byron /Vezon/',
    'SEX': 'M',
    'BIRT': '1980-1-9',
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': ['@F5@'],
    'DEAT': 'NA',
    'AGE': '46',
    'ALIVE': True},
   {'INDI': '@I13@',
    'NAME': 'Beth /Venzon/',
    'SEX': 'F',
    'BIRT': '1980-7-8',
    'INDI_CHILD': ['@F1@'],
    'SPOUSE': 'NA',
    'DEAT': 'NA',
    'AGE': '44',
    'ALIVE': True}]}}
    
    
    Project.family_dic = family_dic
    Project.error_array = []
    Project.birth_before_death()

    return len(Project.error_array)==0


# In[192]:


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


# In[193]:


def test_dates_error():
    
    family_dic={'@F8@': {'FAM': '@F8@',
                         'MARR_LINE':200,
                         'DIV_LINE':250,
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
   'BIRT_LINE':100,
  'INDI_CHILD': ['@F2@'],
  'SPOUSE': ['@F1@'],
  'DEAT': 'NA',
  'AGE': '9',
  'ALIVE': True},
 '@I2@': {'INDI': '@I2@',
  'NAME': 'Helen /Colon/',
  'SEX': 'F',
  'BIRT': '2000-12-10',
   'DEAT_LINE':200,
  'DEAT': '2020-6-2',
  'INDI_CHILD': 'NA',
  'SPOUSE': ['@F1@'],
  'AGE': '81',
  'ALIVE': False}}
    
    Project.family_dic = family_dic
    Project.individuals=individuals
    Project.error_array = []
    Project.validate_dates()

    return Project.error_array==['ERROR: FAMILY: US01: 200: @F8@: Family has marrige date 2020-3-24 later than today',
                                 'ERROR: FAMILY: US01: 250: @F8@: Family has divorce date 2021-3-24 later than today',
                                 'ERROR: INDIVIDUAL: US01: 100: @I1@: Individual has birth date 2030-12-10 later than today',
                                 'ERROR: INDIVIDUAL: US01: 200: @I2@: Individual has death date 2020-6-2 later than today']


# In[194]:


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


# In[195]:


def test_birth_before_marraige_do_nothing():
    family_dic = {'@F1@':{'MARR':'1968-6-4','husband_object':{'INDI':'@I1@','BIRT':'1950-11-8'},'wife_object':{'INDI':'@I2@','BIRT':'1960-11-8'}}}
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.is_birth_before_marraige()
    
    return len(Project.error_array) == 0


# In[196]:


def test_birth_after_marraige_appended_to_error():
    family_dic = {'@F1@':{'MARR':'1968-6-4','MARR_LINE': 320, 'husband_object':{'INDI':'@I1@','BIRT':'1970-11-8'},'wife_object':{'INDI':'@I2@','BIRT':'1960-11-8'}}}
    Project.family_dic = family_dic
    Project.error_array = []
    
    Project.is_birth_before_marraige()
    
    assert Project.error_array[0] == "ERROR: INDIVIDUAL: US02: 320: @I1@: Person has marriage date 1968-6-4 before birth date 1970-11-8"
    return True


# In[197]:


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
   'BIRT_LINE': 100,
   'INDI_CHILD': 'NA',
   'SPOUSE': ['@F8@'],
   'DEAT': 'NA',
   'AGE': '45',
   'ALIVE': True},
  'wife_object': {'INDI': '@I13@',
   'NAME': 'Kitty /Nilson/',
   'SEX': 'F',
   'BIRT': '1980-7-10',
    'BIRT_LINE': 200,
   'INDI_CHILD': ['@F5@'],
   'SPOUSE': ['@F8@'],
   'DEAT': 'NA',
   'AGE': '39',
   'ALIVE': True}}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.is_marriage_legal()

    return Project.anomaly_array==["ANOMALY: INDIVIDUAL: US10: 100: @I18@: Father of family @F8@ is younger than 14 years old - Birth Date 1980-3-17",
"ANOMALY: INDIVIDUAL: US10: 200: @I13@: Wife of family @F8@ is younger than 14 years old - Birth Date 1980-7-10"]


# In[198]:


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


# In[199]:


def test_over_age_150():
    individuals={'@I1@': {'INDI': '@I1@',
  'NAME': 'Jimmy /Colon/',
  'SEX': 'M',
  'BIRT': '1860-6-5',
  'BIRT_LINE': 130,
  'INDI_CHILD': ['@F2@'],
  'SPOUSE': ['@F1@'],
  'DEAT': 'NA',
  'AGE': '159',
  'ALIVE': True},
 '@I2@': {'INDI': '@I2@',
  'NAME': 'Helen /Colon/',
  'SEX': 'F',
  'BIRT': '1850-12-10',
'BIRT_LINE': 230,
  'DEAT': '2009-6-2',
  'INDI_CHILD': 'NA',
  'SPOUSE': ['@F1@'],
  'AGE': '159',
  'ALIVE': False}}
                 
    Project.individuals = individuals
    Project.anomaly_array = []
    Project.is_age_legal()
    return Project.anomaly_array==['ANOMALY: INDIVIDUAL: US07: 130: @I1@: More than 150 years old - Birth Date 1860-6-5',
 'ANOMALY: INDIVIDUAL: US07: 230: @I2@: More than 150 years old at death - Birth Date 1850-12-10: Death Date 2009-6-2']


# In[200]:


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


# In[201]:


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


# In[202]:


# User_Story_29: List all deceased individuals in a GEDCOM file
# Failed test: Person is dead but has no Death Date
@mock.patch("Project.printTable")
def test_list_deceased_individuals_error(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT"]
    current_dic = {'@I6@': {'INDI': '@I6@', "INDI_LINE": '10', 'NAME': 'David /Chang/', 'NAME_LINE': '15', 'SEX': 'M', 'SEX_LINE': '20', 'BIRT': '2002-12-5', 'BIRT_LINE': '22', 'DEAT': 'NA', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F7@'], 'SPOUSE_LINE': '27', 'AGE': '79', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listDeceased()
    return mock_printTable.called == False


# In[203]:


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


# In[204]:


# User_Story_30: List all living married people in a GEDCOM file
# Failed test
@mock.patch("Project.printTable")
def test_list_living_married_individuals_error(mock_printTable):
    allFields = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
    tagNames = ["INDI", "NAME", "SEX", "BIRT", "AGE", "ALIVE", "DEAT", "SPOUSE"]
    current_dic = {'@I4@': {'INDI': '@I1@', 'INDI_LINE': '10', 'NAME': 'Michael /Chang/', 'NAME_LINE': '12', 'SEX': 'M', 'SEX_LINE': '15', 'BIRT': '1958-9-6', 'BIRT_LINE': '17', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'SPOUSE_LINE': '18', 'DEAT': '2002-9-6', 'DEAT_LINE': '22', 'AGE': '61', 'ALIVE': False}}
    Project.individuals = current_dic
    Project.listLivingMarried()
    
    return mock_printTable.called == False


# In[205]:


def test_more_than_15_siblings():
    family_dic = {'@F1@':{'FAM_LINE':230, 'FAM_CHILD':['@I1@','@I10@','@I11@','@I12@','@I13@','@I14@','@I15@','@I16@','@I17@','@I18@','@I19@','@I20@','@I21@','@I22@','@I23@','@I24@','@I24@']}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_sibling_count()

    return Project.anomaly_array[0] == 'ANOMALY: FAMILY: US15: 230: @F1@: Family has 17 siblings which is more than 15 siblings'


# In[206]:


def test_less_than_15_siblings():
    family_dic = {'@F1@':{'FAM_CHILD':['@I1@']}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_sibling_count()

    return len(Project.anomaly_array) == 0


# In[207]:


def test_different_male_last_name():
    family_dic = {'@F1@':{'HUSB_NAME':'Harry /Potter/', 'FAM_CHILD':['@I1@','@I10@'],'children_objects':[{'INDI':'@I1@', 'NAME_LINE':130, 'SEX':'M','NAME':'Chandler /Bing/'},{'INDI':'@I10@', 'SEX':'M','NAME':'Chandler /Potter/'}]}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_last_names()
    return Project.anomaly_array[0] == 'ANOMALY: INDIVIDUAL: US16: 130: @I1@: Individual has different last name Bing than family Potter'


# In[208]:


def test_same_male_last_name():
    family_dic = {'@F1@':{'HUSB_NAME':'Harry /Potter/','FAM_CHILD':['@I1@','@I10@'],'children_objects':[{'INDI':'@I1@', 'SEX':'M','NAME':'Joey /Potter/'},{'INDI':'@I10@', 'SEX':'M','NAME':'Chandler /Potter/'}]}}
    Project.family_dic = family_dic
    Project.anomaly_array = []
    
    Project.check_last_names()

    return len(Project.anomaly_array) == 0


# In[209]:


def test_unique_name_and_birth_error():
    individuals={'@I30@': {'INDI': '@I30@',
  'INDI_LINE': 302,
  'NAME': 'Chet /Malagon/',
  'NAME_LINE': 303,
  'SEX': 'M',
  'SEX_LINE': 307,
  'BIRT_LINE': 308,
  'BIRT': '1943-8-18',
  'INDI_CHILD': ['@F3@'],
  'SPOUSE': ['@F18@', '@F19@', '@F20@'],
  'FAMS_LINE': 312,
  'FAMC_LINE': 313,
  'DEAT': 'NA',
  'AGE': '76',
  'ALIVE': True},
 '@I32@': {'INDI': '@I32@',
  'INDI_LINE': 324,
  'NAME': 'Chet /Malagon/',
  'NAME_LINE': 325,
  'SEX': 'M',
  'SEX_LINE': 329,
  'BIRT_LINE': 330,
  'BIRT': '1943-8-18',
  'INDI_CHILD': ['@F3@'],
  'SPOUSE': 'NA',
  'FAMC_LINE': 332,
  'DEAT': 'NA',
  'AGE': '76',
  'ALIVE': True}}
        

    Project.individuals = individuals
    Project.anomaly_array = []
    Project.unique_name_and_birth()

    return Project.anomaly_array==['ANOMALY: INDIVIDUAL: US23: 324: @I32@: @I30@: Individuals have the same name Chet /Malagon/ and birth date 1943-8-18']


# In[210]:


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


# In[211]:


def test_unique_family_name_and_birth_error():
    family_dic = {'@F3@': {'FAM': '@F3@',
      'FAM_LINE': 365,
      'HUSB_NAME': 'Johnny /Malagon/',
      'HUSB_LINE': 366,
      'HUSB': '@I16@',
      'WIFE_NAME': 'Lura /Lomas/',
      'WIFE_LINE': 367,
      'WIFE': '@I17@',
      'FAM_CHILD': ['@I30@',
       '@I31@',
       '@I32@'],
      'CHIL': '@I33@',
      'CHIL_LINE': 383,
      'CHIL_LINE_@I30@': 380,
      'CHIL_LINE_@I31@': 381,
      'CHIL_LINE_@I32@': 382,
      'MARR_LINE': 384,
      'MARR': '1925-4-28',
      'DIV': 'NA',
      'husband_object': {'INDI': '@I16@',
       'INDI_LINE': 158,
       'NAME': 'Johnny /Malagon/',
       'NAME_LINE': 159,
       'SEX': 'M',
       'SEX_LINE': 163,
       'BIRT_LINE': 164,
       'BIRT': '1901-7-14',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F3@'],
       'FAMS_LINE': 166,
       'DEAT': 'NA',
       'AGE': '118',
       'ALIVE': True},
      'wife_object': {'INDI': '@I17@',
       'INDI_LINE': 167,
       'NAME': 'Lura /Lomas/',
       'NAME_LINE': 168,
       'SEX': 'F',
       'SEX_LINE': 172,
       'BIRT_LINE': 173,
       'BIRT': '1900-8-30',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F3@'],
       'FAMS_LINE': 175,
       'DEAT': 'NA',
       'AGE': '119',
       'ALIVE': True},
      'children_objects': [{'INDI': '@I30@',
        'INDI_LINE': 291,
        'NAME': 'Chet /Malagon/',
        'NAME_LINE': 292,
        'SEX': 'M',
        'SEX_LINE': 296,
        'BIRT_LINE': 297,
        'BIRT': '1943-8-18',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 299,
        'DEAT': 'NA',
        'AGE': '76',
        'ALIVE': True},
       {'INDI': '@I31@',
        'INDI_LINE': 300,
        'NAME': 'Sock /Malagon/',
        'NAME_LINE': 301,
        'SEX': 'F',
        'SEX_LINE': 305,
        'BIRT_LINE': 306,
        'BIRT': '1955-10-17',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 308,
        'DEAT': 'NA',
        'AGE': '63',
        'ALIVE': True},
       {'INDI': '@I32@',
        'INDI_LINE': 309,
        'NAME': 'Chet /Malagon/',
        'NAME_LINE': 310,
        'SEX': 'M',
        'SEX_LINE': 314,
        'BIRT_LINE': 315,
        'BIRT': '1943-8-18',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 317,
        'DEAT': 'NA',
        'AGE': '76',
        'ALIVE': True}]}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.unique_family_name_and_birth()

    return Project.anomaly_array==['ANOMALY: INDIVIDUAL: US25: 365: @I32@: @I30@: Individuals share the same first name Chet /Malagon/ and birth date 1943-8-18 from family @F3@']


# In[212]:


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


# In[213]:


# US20 Aunts and uncles - success
def aunts_and_uncles_success():
    individuals = {'@I1@': {'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F1@'], 'SPOUSE': 'NA', 'FAMC_LINE': 22, 'DEAT': 'NA', 'BIRT_LINE': 22, 'AGE': '31', 'ALIVE': True}, '@I2@': {'INDI': '@I2@', 'INDI_LINE': 23, 'NAME': 'Johny /Chang/', 'NAME_LINE': 24, 'SEX': 'M', 'SEX_LINE': 28, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 31, 'DEAT': 'NA', 'BIRT_LINE': 31, 'AGE': '61', 'ALIVE': True}, '@I3@': {'INDI': '@I3@', 'INDI_LINE': 32, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 33, 'SEX': 'F', 'SEX_LINE': 37, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 40, 'DEAT': 'NA', 'BIRT_LINE': 40, 'AGE': '59', 'ALIVE': True}}
    family_dic = {'@F1@': {'FAM': '@F1@', 'FAM_LINE': 47, 'HUSB_NAME': 'Johny /Chang/', 'HUSB_LINE': 42, 'HUSB': '@I2@', 'WIFE_NAME': 'Nancy /Tsai/', 'WIFE_LINE': 43, 'WIFE': '@I3@', 'FAM_CHILD': ['@I1@'], 'CHIL_LINE': 44, 'CHIL': '@I1@', 'MARR': '1980-3-2', 'DIV': 'NA', 'husband_object': {'INDI': '@I2@', 'INDI_LINE': 23, 'NAME': 'Johny /Chang/', 'NAME_LINE': 24, 'SEX': 'M', 'SEX_LINE': 28, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 31, 'DEAT': 'NA', 'BIRT_LINE': 31, 'AGE': '61', 'ALIVE': True}, 'wife_object': {'INDI': '@I3@', 'INDI_LINE': 32, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 33, 'SEX': 'F', 'SEX_LINE': 37, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 40, 'DEAT': 'NA', 'BIRT_LINE': 40, 'AGE': '59', 'ALIVE': True}, 'children_objects': [{'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F1@'], 'SPOUSE': 'NA', 'FAMC_LINE': 22, 'DEAT': 'NA', 'BIRT_LINE': 22, 'AGE': '31', 'ALIVE': True}]}}
    
    Project.individuals = individuals
    Project.family_dic = family_dic
    
    assert Project.is_uncle_aunt_marriage_legal() == True
    return True


# In[214]:


# US20 Aunts and uncles - error
def aunts_and_uncles_error():
    individuals = {'@I1@': {'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 22, 'FAMC_LINE': 23, 'DEAT': 'NA', 'BIRT_LINE': 23, 'AGE': '31', 'ALIVE': True}, '@I2@': {'INDI': '@I2@', 'INDI_LINE': 24, 'NAME': 'Johny /Chang/', 'NAME_LINE': 25, 'SEX': 'M', 'SEX_LINE': 29, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'FAMS_LINE': 32, 'DEAT': 'NA', 'BIRT_LINE': 32, 'AGE': '61', 'ALIVE': True}, '@I3@': {'INDI': '@I3@', 'INDI_LINE': 33, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 34, 'SEX': 'F', 'SEX_LINE': 38, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'FAMS_LINE': 41, 'DEAT': 'NA', 'BIRT_LINE': 41, 'AGE': '59', 'ALIVE': True}, '@I4@': {'INDI': '@I4@', 'INDI_LINE': 42, 'NAME': 'Dylan /Chang/', 'NAME_LINE': 43, 'SEX': 'M', 'SEX_LINE': 47, 'BIRT': '1990-6-20', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'FAMS_LINE': 50, 'FAMC_LINE': 51, 'DEAT': 'NA', 'BIRT_LINE': 51, 'AGE': '29', 'ALIVE': True}, '@I5@': {'INDI': '@I5@', 'INDI_LINE': 52, 'NAME': 'Diana /Liu/', 'NAME_LINE': 53, 'SEX': 'F', 'SEX_LINE': 57, 'BIRT': '1990-8-26', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F3@'], 'FAMS_LINE': 60, 'DEAT': 'NA', 'BIRT_LINE': 60, 'AGE': '29', 'ALIVE': True}, '@I6@': {'INDI': '@I6@', 'INDI_LINE': 61, 'NAME': 'Felicia /Chang/', 'NAME_LINE': 62, 'SEX': 'F', 'SEX_LINE': 66, 'BIRT': '2010-9-8', 'INDI_CHILD': ['@F3@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 69, 'FAMC_LINE': 70, 'DEAT': 'NA', 'BIRT_LINE': 70, 'AGE': '9', 'ALIVE': True}}
    family_dic = {'@F1@': {'FAM': '@F1@', 'FAM_LINE': 77, 'HUSB_NAME': 'David /Chang/', 'HUSB_LINE': 72, 'HUSB': '@I1@', 'WIFE_NAME': 'Felicia /Chang/', 'WIFE_LINE': 73, 'WIFE': '@I6@', 'MARR': '2012-6-12', 'DIV': 'NA', 'FAM_CHILD': 'NA', 'husband_object': {'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 22, 'FAMC_LINE': 23, 'DEAT': 'NA', 'BIRT_LINE': 23, 'AGE': '31', 'ALIVE': True}, 'wife_object': {'INDI': '@I6@', 'INDI_LINE': 61, 'NAME': 'Felicia /Chang/', 'NAME_LINE': 62, 'SEX': 'F', 'SEX_LINE': 66, 'BIRT': '2010-9-8', 'INDI_CHILD': ['@F3@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 69, 'FAMC_LINE': 70, 'DEAT': 'NA', 'BIRT_LINE': 70, 'AGE': '9', 'ALIVE': True}}, '@F2@': {'FAM': '@F2@', 'FAM_LINE': 85, 'HUSB_NAME': 'Johny /Chang/', 'HUSB_LINE': 79, 'HUSB': '@I2@', 'WIFE_NAME': 'Nancy /Tsai/', 'WIFE_LINE': 80, 'WIFE': '@I3@', 'FAM_CHILD': ['@I1@', '@I4@'], 'CHIL_LINE': 82, 'CHIL': '@I4@', 'MARR': '1980-3-2', 'DIV': 'NA', 'husband_object': {'INDI': '@I2@', 'INDI_LINE': 24, 'NAME': 'Johny /Chang/', 'NAME_LINE': 25, 'SEX': 'M', 'SEX_LINE': 29, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'FAMS_LINE': 32, 'DEAT': 'NA', 'BIRT_LINE': 32, 'AGE': '61', 'ALIVE': True}, 'wife_object': {'INDI': '@I3@', 'INDI_LINE': 33, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 34, 'SEX': 'F', 'SEX_LINE': 38, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F2@'], 'FAMS_LINE': 41, 'DEAT': 'NA', 'BIRT_LINE': 41, 'AGE': '59', 'ALIVE': True}, 'children_objects': [{'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 22, 'FAMC_LINE': 23, 'DEAT': 'NA', 'BIRT_LINE': 23, 'AGE': '31', 'ALIVE': True}, {'INDI': '@I4@', 'INDI_LINE': 42, 'NAME': 'Dylan /Chang/', 'NAME_LINE': 43, 'SEX': 'M', 'SEX_LINE': 47, 'BIRT': '1990-6-20', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'FAMS_LINE': 50, 'FAMC_LINE': 51, 'DEAT': 'NA', 'BIRT_LINE': 51, 'AGE': '29', 'ALIVE': True}]}, '@F3@': {'FAM': '@F3@', 'FAM_LINE': 90, 'HUSB_NAME': 'Dylan /Chang/', 'HUSB_LINE': 87, 'HUSB': '@I4@', 'WIFE_NAME': 'Diana /Liu/', 'WIFE_LINE': 88, 'WIFE': '@I5@', 'FAM_CHILD': ['@I6@'], 'CHIL_LINE': 89, 'CHIL': '@I6@', 'DIV': 'NA', 'MARR': 'NA', 'husband_object': {'INDI': '@I4@', 'INDI_LINE': 42, 'NAME': 'Dylan /Chang/', 'NAME_LINE': 43, 'SEX': 'M', 'SEX_LINE': 47, 'BIRT': '1990-6-20', 'INDI_CHILD': ['@F2@'], 'SPOUSE': ['@F3@'], 'FAMS_LINE': 50, 'FAMC_LINE': 51, 'DEAT': 'NA', 'BIRT_LINE': 51, 'AGE': '29', 'ALIVE': True}, 'wife_object': {'INDI': '@I5@', 'INDI_LINE': 52, 'NAME': 'Diana /Liu/', 'NAME_LINE': 53, 'SEX': 'F', 'SEX_LINE': 57, 'BIRT': '1990-8-26', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F3@'], 'FAMS_LINE': 60, 'DEAT': 'NA', 'BIRT_LINE': 60, 'AGE': '29', 'ALIVE': True}, 'children_objects': [{'INDI': '@I6@', 'INDI_LINE': 61, 'NAME': 'Felicia /Chang/', 'NAME_LINE': 62, 'SEX': 'F', 'SEX_LINE': 66, 'BIRT': '2010-9-8', 'INDI_CHILD': ['@F3@'], 'SPOUSE': ['@F1@'], 'FAMS_LINE': 69, 'FAMC_LINE': 70, 'DEAT': 'NA', 'BIRT_LINE': 70, 'AGE': '9', 'ALIVE': True}]}}
    Project.individuals = individuals
    Project.family_dic = family_dic
    
    return Project.is_uncle_aunt_marriage_legal() == False


# In[215]:


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
    assert fam["FAM_LINE"] == 43
    assert fam["HUSB_LINE"] == 44
    assert fam["WIFE_LINE"] == 45
    assert fam["MARR_LINE"] == 47
                           
    return True


# In[216]:


def test_check_positive_for_bigamy():
    family_dic = {'@F1@': {'MARR': '2010-10-18','DIV': '2015-12-10'}, '@F2@': {'MARR': '2012-10-18','DIV': '2018-12-10'}}
    individuals = {'@I1@': {'SPOUSE': ['@F1@', '@F2@'], 'INDI_LINE': '10', 'INDI': '@I1@'}, '@I2': {'SPOUSE': ['@F1@']}, '@I3': {'SPOUSE': ['@F2@']}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.individuals = individuals
    Project.check_for_bigamy()
    
    return Project.anomaly_array[0] == 'ANOMALY: INDIVIDUAL: US11: 10: @I1@: Performing bigamy'


# In[217]:


def test_check_negative_for_bigamy():
    family_dic = {'@F1@': {'MARR': '2010-10-18','DIV': '2015-12-10'}, '@F2@': {'MARR': '2016-10-18','DIV': '2018-12-10'}}
    individuals = {'@I1': {'SPOUSE': ['@F1@', '@F2@']}, '@I2': {'SPOUSE': ['@F1@']}, '@I3': {'SPOUSE': ['@F2@']}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.individuals = individuals
    Project.check_for_bigamy()
    
    return len(Project.anomaly_array) == 0


# In[218]:


def test_check_positive_parent_child_marriage():
    family_dic = {'@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@','FAM_CHILD': ['@I3@']},'@F2@': {'HUSB': '@I3@','WIFE': '@I2@', 'WIFE_LINE': '11'}}
    individuals = {'@I1@': {'SPOUSE': ['@F1@']}, '@I2@': {'SPOUSE': ['@F1@', '@F2@']},'@I3@': {'SPOUSE': ['@F2@']}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.individuals = individuals
    Project.check_parent_child_marriage()
    
    return Project.anomaly_array[0] == "ANOMALY: INDIVIDUAL: US17: 11: @I2@: Individual married to child @I3@"


# In[219]:


def test_check_negative_parent_child_marriage():
    family_dic = {'@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@','FAM_CHILD': ['@I3@']},'@F2@': {'HUSB': '@I4@','WIFE': '@I2@'}}
    individuals = {'@I1@': {'SPOUSE': ['@F1@']}, '@I2@': {'SPOUSE': ['@F1@', '@F2@']},'@I3@': {'SPOUSE': 'NA'}, '@I4@': {'SPOUSE': ['@F2@']}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.individuals = individuals
    Project.check_parent_child_marriage()
    
    return len(Project.anomaly_array) == 0


# In[220]:


def test_multiple_birth_pass():
    family_dic = {'@F3@': {'FAM': '@F3@',
      'FAM_LINE': 365,
      'HUSB_NAME': 'Johnny /Malagon/',
      'HUSB_LINE': 366,
      'HUSB': '@I16@',
      'WIFE_NAME': 'Lura /Lomas/',
      'WIFE_LINE': 367,
      'WIFE': '@I17@',
      'FAM_CHILD': ['@I2@',
       '@I18@',
       '@I20@',
       '@I21@',
       '@I22@',
       '@I23@',
       '@I24@',
       '@I25@',
       '@I26@',
       '@I27@',
       '@I28@',
       '@I29@',
       '@I30@',
       '@I31@',
       '@I32@',
       '@I33@'],
      'CHIL_LINE_@I2@': 368,
      'CHIL': '@I33@',
      'CHIL_LINE': 383,
      'CHIL_LINE_@I18@': 369,
      'CHIL_LINE_@I20@': 370,
      'CHIL_LINE_@I21@': 371,
      'CHIL_LINE_@I22@': 372,
      'CHIL_LINE_@I23@': 373,
      'CHIL_LINE_@I24@': 374,
      'CHIL_LINE_@I25@': 375,
      'CHIL_LINE_@I26@': 376,
      'CHIL_LINE_@I27@': 377,
      'CHIL_LINE_@I28@': 378,
      'CHIL_LINE_@I29@': 379,
      'CHIL_LINE_@I30@': 380,
      'CHIL_LINE_@I31@': 381,
      'CHIL_LINE_@I32@': 382,
      'CHIL_LINE_@I33@': 383,
      'MARR_LINE': 384,
      'MARR': '1925-4-28',
      'DIV': 'NA',
      'husband_object': {'INDI': '@I16@',
       'INDI_LINE': 158,
       'NAME': 'Johnny /Malagon/',
       'NAME_LINE': 159,
       'SEX': 'M',
       'SEX_LINE': 163,
       'BIRT_LINE': 164,
       'BIRT': '1901-7-14',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F3@'],
       'FAMS_LINE': 166,
       'DEAT': 'NA',
       'AGE': '118',
       'ALIVE': True},
      'wife_object': {'INDI': '@I17@',
       'INDI_LINE': 167,
       'NAME': 'Lura /Lomas/',
       'NAME_LINE': 168,
       'SEX': 'F',
       'SEX_LINE': 172,
       'BIRT_LINE': 173,
       'BIRT': '1900-8-30',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F3@'],
       'FAMS_LINE': 175,
       'DEAT': 'NA',
       'AGE': '119',
       'ALIVE': True},
      'children_objects': [{'INDI': '@I2@',
        'INDI_LINE': 24,
        'NAME': 'Stephan /Malagon/',
        'NAME_LINE': 25,
        'SEX': 'M',
        'SEX_LINE': 29,
        'BIRT_LINE': 30,
        'BIRT': '1930-8-21',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': ['@F2@'],
        'FAMS_LINE': 32,
        'FAMC_LINE': 33,
        'DEAT': 'NA',
        'AGE': '89',
        'ALIVE': True},
       {'INDI': '@I18@',
        'INDI_LINE': 176,
        'NAME': 'Tesha /Malagon/',
        'NAME_LINE': 177,
        'SEX': 'F',
        'SEX_LINE': 181,
        'BIRT_LINE': 182,
        'BIRT': '1819-7-8',
        'DEAT_LINE': 184,
        'DEAT': '2019-8-2',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 186,
        'AGE': '200',
        'ALIVE': False},
       {'INDI': '@I20@',
        'INDI_LINE': 196,
        'NAME': 'Lucile /Malagon/',
        'NAME_LINE': 197,
        'SEX': 'F',
        'SEX_LINE': 201,
        'BIRT_LINE': 202,
        'BIRT': '1931-9-9',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 204,
        'DEAT': 'NA',
        'AGE': '88',
        'ALIVE': True},
       {'INDI': '@I21@',
        'INDI_LINE': 205,
        'NAME': 'Regena /Malagon/',
        'NAME_LINE': 206,
        'SEX': 'F',
        'SEX_LINE': 210,
        'BIRT_LINE': 211,
        'BIRT': '1820-10-8',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 213,
        'DEAT': 'NA',
        'AGE': '199',
        'ALIVE': True},
       {'INDI': '@I22@',
        'INDI_LINE': 214,
        'NAME': 'Tom /Malagon/',
        'NAME_LINE': 215,
        'SEX': 'M',
        'SEX_LINE': 219,
        'BIRT_LINE': 220,
        'BIRT': '1923-5-8',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': ['@F9@'],
        'FAMS_LINE': 222,
        'FAMC_LINE': 223,
        'DEAT': 'NA',
        'AGE': '96',
        'ALIVE': True},
       {'INDI': '@I23@',
        'INDI_LINE': 224,
        'NAME': 'Vonnie /Malagon/',
        'NAME_LINE': 225,
        'SEX': 'M',
        'SEX_LINE': 229,
        'BIRT_LINE': 230,
        'BIRT': '1936-3-10',
        'DEAT_LINE': 232,
        'DEAT': '1937-7-6',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 234,
        'AGE': '1',
        'ALIVE': False},
       {'INDI': '@I24@',
        'INDI_LINE': 235,
        'NAME': 'Shena /Malagon/',
        'NAME_LINE': 236,
        'SEX': 'F',
        'SEX_LINE': 240,
        'BIRT_LINE': 241,
        'BIRT': '1937-11-6',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 243,
        'DEAT': 'NA',
        'AGE': '81',
        'ALIVE': True},
       {'INDI': '@I25@',
        'INDI_LINE': 244,
        'NAME': 'Hailey /Malagon/',
        'NAME_LINE': 245,
        'SEX': 'F',
        'SEX_LINE': 249,
        'BIRT_LINE': 250,
        'BIRT': '1938-10-8',
        'DEAT_LINE': 252,
        'DEAT': '1939-9-18',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 254,
        'AGE': '0',
        'ALIVE': False},
       {'INDI': '@I26@',
        'INDI_LINE': 255,
        'NAME': 'Milford /Malagon/',
        'NAME_LINE': 256,
        'SEX': 'M',
        'SEX_LINE': 260,
        'BIRT_LINE': 261,
        'BIRT': '1939-11-8',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 263,
        'DEAT': 'NA',
        'AGE': '79',
        'ALIVE': True},
       {'INDI': '@I27@',
        'INDI_LINE': 264,
        'NAME': 'Rashida /Malagon/',
        'NAME_LINE': 265,
        'SEX': 'F',
        'SEX_LINE': 269,
        'BIRT_LINE': 270,
        'BIRT': '1940-12-7',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 272,
        'DEAT': 'NA',
        'AGE': '78',
        'ALIVE': True},
       {'INDI': '@I28@',
        'INDI_LINE': 273,
        'NAME': 'Deeann /Malagon/',
        'NAME_LINE': 274,
        'SEX': 'F',
        'SEX_LINE': 278,
        'BIRT_LINE': 279,
        'BIRT': '1941-10-23',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 281,
        'DEAT': 'NA',
        'AGE': '77',
        'ALIVE': True},
       {'INDI': '@I29@',
        'INDI_LINE': 282,
        'NAME': 'Dario /Malagon/',
        'NAME_LINE': 283,
        'SEX': 'M',
        'SEX_LINE': 287,
        'BIRT_LINE': 288,
        'BIRT': '1942-12-14',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 290,
        'DEAT': 'NA',
        'AGE': '76',
        'ALIVE': True},
       {'INDI': '@I30@',
        'INDI_LINE': 291,
        'NAME': 'Chet /Malagon/',
        'NAME_LINE': 292,
        'SEX': 'M',
        'SEX_LINE': 296,
        'BIRT_LINE': 297,
        'BIRT': '1943-8-18',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 299,
        'DEAT': 'NA',
        'AGE': '76',
        'ALIVE': True},
       {'INDI': '@I31@',
        'INDI_LINE': 300,
        'NAME': 'Sock /Malagon/',
        'NAME_LINE': 301,
        'SEX': 'F',
        'SEX_LINE': 305,
        'BIRT_LINE': 306,
        'BIRT': '1955-10-17',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 308,
        'DEAT': 'NA',
        'AGE': '63',
        'ALIVE': True},
       {'INDI': '@I32@',
        'INDI_LINE': 309,
        'NAME': 'Chet /Malagon/',
        'NAME_LINE': 310,
        'SEX': 'M',
        'SEX_LINE': 314,
        'BIRT_LINE': 315,
        'BIRT': '1943-8-18',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 317,
        'DEAT': 'NA',
        'AGE': '76',
        'ALIVE': True},
       {'INDI': '@I33@',
        'INDI_LINE': 318,
        'NAME': 'Loyd /Malagon/',
        'NAME_LINE': 319,
        'SEX': 'M',
        'SEX_LINE': 323,
        'BIRT_LINE': 324,
        'BIRT': '1965-8-9',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 326,
        'DEAT': 'NA',
        'AGE': '54',
        'ALIVE': True}]}}
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.multiple_birth()

    return Project.anomaly_array==['ANOMALY: FAMILY: US32: 365: @F3@: The two or more individuals were born at the same time']
    


# In[221]:


def test_multiple_birth_fail():
    family_dic = {'@F3@': {'FAM': '@F3@',
      'HUSB_NAME': 'Johnny /Malagon/',
      'HUSB': '@I16@',
      'WIFE_NAME': 'Lura /Lomas/',
      'WIFE': '@I17@',
      'FAM_CHILD': ['@I30@',
       '@I31@'],
      'CHIL': '@I34@',
      'MARR': '1925-4-28',
      'DIV': 'NA',
      'husband_object': {'INDI': '@I16@',
       'NAME': 'Johnny /Malagon/',
       'SEX': 'M',
       'BIRT': '1901-7-14',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F3@'],
       'DEAT': 'NA',
       'AGE': '118',
       'ALIVE': True},
      'wife_object': {'INDI': '@I17@',
       'NAME': 'Lura /Lomas/',
       'SEX': 'F',
       'BIRT': '1900-8-30',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F3@'],
       'DEAT': 'NA',
       'AGE': '119',
       'ALIVE': True},
      'children_objects': [{'INDI': '@I30@',
        'INDI_LINE': 291,
        'NAME': 'Chet /Malagon/',
        'NAME_LINE': 292,
        'SEX': 'M',
        'SEX_LINE': 296,
        'BIRT_LINE': 297,
        'BIRT': '1943-8-18',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 299,
        'DEAT': 'NA',
        'AGE': '76',
        'ALIVE': True},
       {'INDI': '@I31@',
        'INDI_LINE': 300,
        'NAME': 'Sock /Malagon/',
        'NAME_LINE': 301,
        'SEX': 'F',
        'SEX_LINE': 305,
        'BIRT_LINE': 306,
        'BIRT': '1955-10-17',
        'INDI_CHILD': ['@F3@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 308,
        'DEAT': 'NA',
        'AGE': '63',
        'ALIVE': True}]}}
    
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.multiple_birth()

    return len(Project.anomaly_array) == 0


# In[222]:


def test_large_age_diff_pass():
    family_dic = {'@F4@': {'FAM': '@F4@',
      'FAM_LINE': 388,
      'HUSB_NAME': 'Josh /Malagon/',
      'HUSB_LINE': 389,
      'HUSB': '@I5@',
      'WIFE_NAME': 'Cinda /Burgard/',
      'WIFE_LINE': 390,
      'WIFE': '@I8@',
      'FAM_CHILD': ['@I10@'],
      'CHIL_LINE_@I10@': 391,
      'CHIL': '@I10@',
      'CHIL_LINE': 391,
      'MARR_LINE': 392,
      'MARR': '1978-9-2',
      'DIV': 'NA',
      'husband_object': {'INDI': '@I5@',
       'INDI_LINE': 52,
       'NAME': 'Josh /Malagon/',
       'NAME_LINE': 53,
       'SEX': 'M',
       'SEX_LINE': 57,
       'BIRT_LINE': 58,
       'BIRT': '1964-10-31',
       'DEAT_LINE': 60,
       'DEAT': '1984-5-7',
       'INDI_CHILD': ['@F2@'],
       'SPOUSE': ['@F4@'],
       'FAMS_LINE': 62,
       'FAMC_LINE': 63,
       'AGE': '19',
       'ALIVE': False},
      'wife_object': {'INDI': '@I8@',
       'INDI_LINE': 83,
       'NAME': 'Cinda /Burgard/',
       'NAME_LINE': 84,
       'SEX': 'F',
       'SEX_LINE': 88,
       'BIRT_LINE': 89,
       'BIRT': '1966-8-8',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F4@', '@F6@', '@F7@'],
       'FAMS_LINE': 93,
       'DEAT': 'NA',
       'AGE': '53',
       'ALIVE': True},
      'children_objects': [{'INDI': '@I10@',
        'INDI_LINE': 103,
        'NAME': 'Ruthe /Malagon/',
        'NAME_LINE': 104,
        'SEX': 'F',
        'SEX_LINE': 108,
        'BIRT_LINE': 109,
        'BIRT': '1977-9-8',
        'INDI_CHILD': ['@F4@'],
        'SPOUSE': 'NA',
        'FAMC_LINE': 111,
        'DEAT': 'NA',
        'AGE': '42',
        'ALIVE': True}]}}
    
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.large_age_diff()

    return Project.anomaly_array==['ANOMALY: FAMILY: US34: 388: @F4@: Family has a large spouse age difference']


# In[223]:


def test_large_age_diff_fail():
    family_dic = {'@F6@': {'FAM': '@F6@',
      'FAM_LINE': 399,
      'HUSB_NAME': 'Jerrell /Finklea/',
      'HUSB_LINE': 400,
      'HUSB': '@I9@',
      'WIFE_NAME': 'Cinda /Burgard/',
      'WIFE_LINE': 401,
      'WIFE': '@I8@',
      'FAM_CHILD': ['@I11@', '@I19@'],
      'CHIL_LINE_@I11@': 402,
      'CHIL': '@I19@',
      'CHIL_LINE': 403,
      'CHIL_LINE_@I19@': 403,
      'MARR_LINE': 404,
      'MARR': '1985-4-5',
      'DIV': 'NA',
      'husband_object': {'INDI': '@I9@',
       'INDI_LINE': 94,
       'NAME': 'Jerrell /Finklea/',
       'NAME_LINE': 95,
       'SEX': 'M',
       'SEX_LINE': 99,
       'BIRT_LINE': 100,
       'BIRT': '1965-9-8',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F6@'],
       'FAMS_LINE': 102,
       'DEAT': 'NA',
       'AGE': '54',
       'ALIVE': True},
      'wife_object': {'INDI': '@I8@',
       'INDI_LINE': 83,
       'NAME': 'Cinda /Burgard/',
       'NAME_LINE': 84,
       'SEX': 'F',
       'SEX_LINE': 88,
       'BIRT_LINE': 89,
       'BIRT': '1966-8-8',
       'INDI_CHILD': 'NA',
       'SPOUSE': ['@F4@', '@F6@', '@F7@'],
       'FAMS_LINE': 93,
       'DEAT': 'NA',
       'AGE': '53',
       'ALIVE': True}}}
    
    
    Project.family_dic = family_dic
    Project.anomaly_array = []
    Project.large_age_diff()

    return len(Project.anomaly_array) == 0


# In[224]:


# US38 Test tist upcoming birthdays
def test_list_upcoming_bday_pass():
    from datetime import datetime
    from datetime import timedelta
    
    #Mock individuals dictionary
    individuals = {'@I1@': {'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-11-9', 'INDI_CHILD': ['@F1@'], 'SPOUSE': 'NA', 'FAMC_LINE': 22, 'DEAT': 'NA', 'BIRT_LINE': 22, 'AGE': '31', 'ALIVE': True}}
    
    #Creates a new date that's within 30 days from today's date
    current_date = datetime.today() + timedelta(days=10)
    individuals["@I1@"]["BIRT"] = current_date.strftime("%Y-%m-%d")
    
    Project.individuals = individuals

    assert Project.list_upcoming_bday() == True
    return True


# In[225]:


# US38 Test list upcoming birthdays
def test_list_upcoming_bday_fail():
    #Mock individuals dictionary
    individuals = {'@I1@': {'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': 'NA', 'INDI_CHILD': ['@F1@'], 'SPOUSE': 'NA', 'FAMC_LINE': 22, 'DEAT': 'NA', 'BIRT_LINE': 22, 'AGE': '31', 'ALIVE': True}, '@I2@': {'INDI': '@I2@', 'INDI_LINE': 23, 'NAME': 'Johny /Chang/', 'NAME_LINE': 24, 'SEX': 'M', 'SEX_LINE': 28, 'BIRT': '1958-11-25', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 31, 'DEAT': 'NA', 'BIRT_LINE': 31, 'AGE': '61', 'ALIVE': True}, '@I3@': {'INDI': '@I3@', 'INDI_LINE': 32, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 33, 'SEX': 'F', 'SEX_LINE': 37, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 40, 'DEAT': 'NA', 'BIRT_LINE': 40, 'AGE': '59', 'ALIVE': True}}
    
    Project.individuals = individuals
    return Project.list_upcoming_bday() == False


# In[226]:


# US39 Test list upcoming birthdays
def test_list_upcoming_anni_pass():
    from datetime import datetime
    from datetime import timedelta
    
    #Mock family dictionary
    family_dic = {'@F1@': {'FAM': '@F1@', 'FAM_LINE': 47, 'HUSB_NAME': 'Johny /Chang/', 'HUSB_LINE': 42, 'HUSB': '@I2@', 'WIFE_NAME': 'Nancy /Tsai/', 'WIFE_LINE': 43, 'WIFE': '@I3@', 'FAM_CHILD': ['@I1@'], 'CHIL_LINE': 44, 'CHIL': '@I1@', 'MARR': '1980-3-2', 'DIV': 'NA', 'husband_object': {'INDI': '@I2@', 'INDI_LINE': 23, 'NAME': 'Johny /Chang/', 'NAME_LINE': 24, 'SEX': 'M', 'SEX_LINE': 28, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 31, 'DEAT': 'NA', 'BIRT_LINE': 31, 'AGE': '61', 'ALIVE': True}, 'wife_object': {'INDI': '@I3@', 'INDI_LINE': 32, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 33, 'SEX': 'F', 'SEX_LINE': 37, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 40, 'DEAT': 'NA', 'BIRT_LINE': 40, 'AGE': '59', 'ALIVE': True}, 'children_objects': [{'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F1@'], 'SPOUSE': 'NA', 'FAMC_LINE': 22, 'DEAT': 'NA', 'BIRT_LINE': 22, 'AGE': '31', 'ALIVE': True}]}}
    #Creates a new date that's within 30 days from today's date
    current_date = datetime.today() + timedelta(days=10)
    family_dic["@F1@"]["MARR"] = current_date.strftime("%Y-%m-%d")
    
    Project.family_dic = family_dic

    assert Project.list_upcoming_anni() == True
    return True


# In[227]:


# US39 Test list upcoming birthdays
def test_list_upcoming_anni_fail():
    #Mock family dictionary
    family_dic = {'@F1@': {'FAM': '@F1@', 'FAM_LINE': 47, 'HUSB_NAME': 'Johny /Chang/', 'HUSB_LINE': 42, 'HUSB': '@I2@', 'WIFE_NAME': 'Nancy /Tsai/', 'WIFE_LINE': 43, 'WIFE': '@I3@', 'FAM_CHILD': ['@I1@'], 'CHIL_LINE': 44, 'CHIL': '@I1@', 'MARR': 'NA', 'DIV': 'NA', 'husband_object': {'INDI': '@I2@', 'INDI_LINE': 23, 'NAME': 'Johny /Chang/', 'NAME_LINE': 24, 'SEX': 'M', 'SEX_LINE': 28, 'BIRT': '1958-8-9', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 31, 'DEAT': 'NA', 'BIRT_LINE': 31, 'AGE': '61', 'ALIVE': True}, 'wife_object': {'INDI': '@I3@', 'INDI_LINE': 32, 'NAME': 'Nancy /Tsai/', 'NAME_LINE': 33, 'SEX': 'F', 'SEX_LINE': 37, 'BIRT': '1960-9-6', 'INDI_CHILD': 'NA', 'SPOUSE': ['@F1@'], 'FAMS_LINE': 40, 'DEAT': 'NA', 'BIRT_LINE': 40, 'AGE': '59', 'ALIVE': True}, 'children_objects': [{'INDI': '@I1@', 'INDI_LINE': 14, 'NAME': 'David /Chang/', 'NAME_LINE': 15, 'SEX': 'M', 'SEX_LINE': 19, 'BIRT': '1988-7-9', 'INDI_CHILD': ['@F1@'], 'SPOUSE': 'NA', 'FAMC_LINE': 22, 'DEAT': 'NA', 'BIRT_LINE': 22, 'AGE': '31', 'ALIVE': True}]}}
    
    Project.family_dic = family_dic
    return Project.list_upcoming_anni() == False


# In[228]:


def test_check_sibling_spacing_1_month_apart():
    family_dic = { '@F1@': {'FAM_CHILD': ['@I1@', '@I2@']} }
    individuals = {'@I1@': {'INDI_LINE': 1, 'BIRT': '2001-10-1', 'INDI_CHILD': ['@F1@']}, '@I2@': {'INDI_LINE': 2, 'BIRT': '2001-11-1', 'INDI_CHILD': ['@F1@']}}
    result_array = ['ERROR: INDIVIDUAL: US13: 1: Child @I1@ is born within 8 months and more than 2 days of sibling', 'ERROR: INDIVIDUAL: US13: 2: Child @I2@ is born within 8 months and more than 2 days of sibling']
    Project.family_dic = family_dic
    Project.individuals = individuals
    Project.error_array = []
    
    Project.check_sibling_spacing()
    
    assert Project.error_array == result_array
    return True


# In[229]:


def test_check_sibling_spacing_siblings_1_day_apart():
    family_dic = { '@F1@': {'FAM_CHILD': ['@I1@', '@I2@']}}
    individuals = {'@I1@': {'INDI_LINE': 1, 'BIRT': '2001-10-1'}, '@I2@': {'INDI_LINE': 2, 'BIRT': '2001-10-2'}}
    result_array = ['ERROR: INDIVIDUAL: US13: 1: Child @I1@ is born within 8 months and more than 2 days of sibling', 'ERROR: INDIVIDUAL: US13: 2: Child @I2@ is born within 8 months and more than 2 days of sibling']
    Project.family_dic = family_dic
    Project.individuals = individuals
    Project.error_array = []
    
    Project.check_sibling_spacing()
    
    assert len(Project.error_array) == 0
    
    return True


# In[230]:


def test_check_sibling_marriage_married():
    family_dic = { '@F1@': {'FAM_CHILD': ['@I1@', '@I2@']}, '@F2@': {'WIFE':'@I1@', 'HUSB': '@I2@'}}
    individuals = {'@I1@': {'SPOUSE': ['@F2@'], 'INDI_LINE': 1, 'BIRT': '2001-10-1', 'INDI_CHILD': ['@F1@']}, '@I2@': {'SPOUSE': ['@F2@'], 'INDI_LINE': 2, 'BIRT': '2001-10-2', 'INDI_CHILD': ['@F1@']}}
    result_array = ['ANOMALY: INDIVIDUAL: US18: 1: @I1@: Individual married to sibling @I2@', 'ANOMALY: INDIVIDUAL: US18: 2: @I2@: Individual married to sibling @I1@']
    
    Project.anomaly_array = []
    Project.family_dic = family_dic
    Project.individuals = individuals
    
    Project.check_sibling_marriage()
    
    assert Project.anomaly_array == result_array
    
    return True


# In[231]:


def test_check_sibling_marriage_not_married():
    family_dic = { '@F1@': {'FAM_CHILD': ['@I1@']}, '@F2@': {'WIFE':'@I1@', 'HUSB': '@I2@'}}
    individuals = {'@I1@': {'SPOUSE': ['@F2@'], 'INDI_LINE': 1, 'BIRT': '2001-10-1', 'INDI_CHILD': ['@F1@']}, '@I2@': {'SPOUSE': ['@F2@'], 'INDI_LINE': 2, 'BIRT': '2001-10-2'}}
    result_array = ['ANOMALY: INDIVIDUAL: US18: 1: @I1@: Individual married to sibling @I2@', 'ANOMALY: INDIVIDUAL: US18: 2: @I2@: Individual married to sibling @I1@']
    
    Project.anomaly_array = []
    Project.family_dic = family_dic
    Project.individuals = individuals
    
    Project.check_sibling_marriage()
    
    assert len(Project.anomaly_array) == 0
    
    return True


# In[232]:


def test_check_cousin_marriage_pass():
    family_dic = { '@F1@': {'FAM_CHILD': ['@I1@', '@I2@']}, '@F2@': {'WIFE':'@I1@', 'HUSB': '@I2@'}}
    individuals = {'@I1@': {'SPOUSE': ['@F2@'], 'INDI_LINE': 1, 'BIRT': '2001-10-1', 'INDI_CHILD': ['@F1@']}, '@I2@': {'SPOUSE': ['@F2@'], 'INDI_LINE': 2, 'BIRT': '2001-10-2', 'INDI_CHILD': ['@F1@']}}
    
    Project.anomaly_array = []
    Project.family_dic = family_dic
    Project.individuals = individuals
    
    Project.check_cousins_marriage()
    
    return Project.anomaly_array == ['ANOMALY: INDIVIDUAL: US19: 1: @I1@: Individual married to cousins @I2@', 'ANOMALY: INDIVIDUAL: US19: 2: @I2@: Individual married to cousins @I1@']
    
    return True


# In[233]:


def test_check_cousin_marriage_fail():
    family_dic = { '@F1@': {'FAM_CHILD': ['@I1@']}, '@F2@': {'WIFE':'@I1@', 'HUSB': '@I2@'}}
    individuals = {'@I1@': {'SPOUSE': ['@F2@'], 'INDI_LINE': 1, 'BIRT': '2001-10-1', 'INDI_CHILD': ['@F1@']}, '@I2@': {'SPOUSE': ['@F2@'], 'INDI_LINE': 2, 'BIRT': '2001-10-2'}}

    
    Project.anomaly_array = []
    Project.family_dic = family_dic
    Project.individuals = individuals
    
    Project.check_cousins_marriage()
    
    return len(Project.anomaly_array) == 0


# In[234]:


def test_unique_indi_and_family():
    Project.error_array = []
    
    file = "./Romeo_Juliet_Family.ged"


    Project.read_in(file)
    return Project.error_array==['ERROR: INDIVIDUAL: US22: 51: @I1@: Individuals have the same ID', 'ERROR: FAMILY: US22: 62: @F1@: Two families share the same ID ']


# In[235]:


import unittest

class TestStringMethods(unittest.TestCase):
    
    #Sprint 1 Test Cases
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
    
    #Sprint 2 Test Cases
    def test_is_marriage_after_divorce(self):
        self.assertTrue(test_is_marriage_after_divorce());
    def test_is_marriage_after_divorce_error(self):
        self.assertTrue(test_is_marriage_after_divorce_error());
    def test_is_marriage_after_death(self):
        self.assertTrue(test_is_marriage_after_death());
    def test_is_marriage_after_death_error(self):
        self.assertTrue(test_is_marriage_after_death_error());
    def test_death_before_marriage_fail(self):
        self.assertTrue(test_death_before_marriage_fail());
    def test_death_before_marriage_pass(self):
        self.assertTrue(test_death_before_marriage_pass());
    def test_birth_before_death_fail(self):
        self.assertTrue(test_birth_before_death_fail());
    def test_birth_before_death_pass(self):
        self.assertTrue(test_birth_before_death_pass());
    def test_aunts_and_uncles_pass(self):
        self.assertTrue(aunts_and_uncles_success());
    def test_aunts_and_uncles_fail(self):
        self.assertTrue(aunts_and_uncles_error());
    def test_input_line_numbers_pass(self):
        self.assertTrue(input_line_numbers());
    def test_Check_Positive_For_Bigamy(self):
        self.assertTrue(test_check_positive_for_bigamy());
    def test_Check_Negative_For_Bigamy(self):
        self.assertTrue(test_check_negative_for_bigamy());
    def test_check_positive_parent_child_marriage(self):
        self.assertTrue(test_check_positive_parent_child_marriage());
    def test_check_negative_parent_child_marriage(self):
        self.assertTrue(test_check_negative_parent_child_marriage());
    def test_multiple_birth_pass(self):
        self.assertTrue(test_multiple_birth_pass());
    def test_multiple_birth_fail(self):
        self.assertTrue(test_multiple_birth_fail());
    def test_large_age_diff_pass(self):
        self.assertTrue(test_large_age_diff_pass());
    def test_large_age_diff_fail(self):
        self.assertTrue(test_large_age_diff_fail());
    
    #Sprint 3 Test Cases
    def test_is_birth_before_death(self):
        self.assertTrue(test_is_birth_before_death())
    def test_is_birth_before_death_fail(self):
        self.assertTrue(test_is_birth_before_death_fail)
    def test_parents_not_too_old_pass(self):
        self.assertTrue(test_parents_not_too_old_pass())
    def test_parents_not_too_old_fail(self):
        self.assertTrue(test_parents_not_too_old_fail())
    def test_divorce_before_death_pass(self):
        self.assertTrue(test_divorce_before_death_pass())
    def test_divorce_before_death_fail(self):
        self.assertTrue(test_divorce_before_death_fail())
    def test_list_upcoming_bday_pass(self):
        self.assertTrue(test_list_upcoming_bday_pass())
    def test_list_upcoming_bday_fail(self):
        self.assertTrue(test_list_upcoming_bday_fail())
    def test_list_upcoming_anni_pass(self):
        self.assertTrue(test_list_upcoming_anni_pass())
    def test_list_upcoming_anni_fail(self):
        self.assertTrue(test_list_upcoming_anni_fail())
    def test_check_sibling_spacing_1_month_apart(self):
        self.assertTrue(test_check_sibling_spacing_1_month_apart())
    def test_check_sibling_spacing_siblings_1_day_apart(self):
        self.assertTrue(test_check_sibling_spacing_siblings_1_day_apart())
    def test_check_sibling_marriage_married(self):
        self.assertTrue(test_check_sibling_marriage_married())
    def test_check_sibling_marriage_not_married(self):
        self.assertTrue(test_check_sibling_marriage_not_married())
    def test_unique_indi_and_family(self):
        self.assertTrue(test_unique_indi_and_family())
    def test_check_cousin_marriage_pass(self):
        self.assertTrue(test_check_cousin_marriage_pass())
    def test_check_cousin_marriage_fail(self):
        self.assertTrue(test_check_cousin_marriage_fail())
        
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

