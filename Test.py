# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import pytest
pytest.main(args = [__file__,'-v'])


def custom_max(min_liste):

    max_verdi = -float('inf')
    
    for tall in min_liste:
        if tall > max_verdi:
            max_verdi = tall
    
    return max_verdi


def test_custom_max1():
    min_liste = [2,3,8,5,6,1]
    assert custom_max(min_liste) == 8
    
def test_custom_max2():
    min_liste = [-2,-5,-8,-5,-6,-10]
    assert custom_max(min_liste) == -2 


lister = [[random.random() for tall in range(5)] for k in range(1000)]
@pytest.mark.parametrize('min_liste',lister)
def test_random_inputs(min_liste):
    assert custom_max(min_liste) == max(min_liste) 
    
