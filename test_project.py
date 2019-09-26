#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pytest
import unittest
import Project as project
import StringIO
import sys


# In[85]:


def test_more_than_15_siblings():
    family_dic = {'@F1@':{'FAM_CHILD':['@I1@','@I10@','@I11@','@I12@','@I13@','@I14@','@I15@','@I16@','@I17@','@I18@','@I19@','@I20@','@I21@','@I22@','@I23@','@I24@','@I24@']}}
    project.family_dic = family_dic
    fake_out = StringIO.StringIO()
    sys.stdout = fake_out
    
    project.check_sibling_count()

    sys.stdout = sys.__stdout__
    assert fake_out.getvalue() == 'ANOMOLY: FAMILY: US16: @F1@: Family has 17 siblings which is more than 15 siblings\n'


# In[86]:


def test_less_than_15_siblings():
    family_dic = {'@F1@':{'FAM_CHILD':['@I1@']}}
    project.family_dic = family_dic
    fake_out = StringIO.StringIO()
    sys.stdout = fake_out
    
    project.check_sibling_count()

    sys.stdout = sys.__stdout__
    assert fake_out.getvalue() == ''


# In[87]:


def test_different_male_last_name():
    family_dic = {'@F1@':{'HUSB_NAME':'Harry /Potter/','FAM_CHILD':['@I1@','@I10@'],'children_objects':[{'INDI':'@I1@', 'SEX':'M','NAME':'Chandler /Bing/'},{'INDI':'@I10@', 'SEX':'M','NAME':'Chandler /Potter/'}]}}
    project.family_dic = family_dic
    fake_out = StringIO.StringIO()
    sys.stdout = fake_out
    
    project.check_last_names()

    sys.stdout = sys.__stdout__
    assert fake_out.getvalue() == 'ANOMOLY: INDIVIDUAL: US16: @I1@: Individual has different last name Bing than family Potter\n'
    


# In[88]:


def test_same_male_last_name():
    family_dic = {'@F1@':{'HUSB_NAME':'Harry /Potter/','FAM_CHILD':['@I1@','@I10@'],'children_objects':[{'INDI':'@I1@', 'SEX':'M','NAME':'Joey /Potter/'},{'INDI':'@I10@', 'SEX':'M','NAME':'Chandler /Potter/'}]}}
    project.family_dic = family_dic
    fake_out = StringIO.StringIO()
    sys.stdout = fake_out
    
    project.check_last_names()

    sys.stdout = sys.__stdout__
    assert fake_out.getvalue() == ''
    


# In[89]:


test_more_than_15_siblings()
test_less_than_15_siblings()
test_different_male_last_name()
test_same_male_last_name()


# In[ ]:




