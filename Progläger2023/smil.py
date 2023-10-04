# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:22:05 2023

@author: ninae
"""
import numpy as np
import sys

smileys = [':)',';)', ':-)', ';-)']

def make_smillist(smillist):
    x = smillist.split(',')
    return x


def check_for_smiley(smileys,smillist):
    for j in smileys:
        indices = [smillist.find(j) for i in smillist]
    return indices
    
smillist = make_smillist(';),3s,a,a')
check_for_smiley(smileys, smillist) 
 