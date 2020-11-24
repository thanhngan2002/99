# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:17:08 2020

@author: Admin
"""

import time
check="n"
while check=="n":
    check=input("ban co muon tat may khong?(y/n):")
    if check=="n":
      time.sleep(30)
    else:
        import os
        os.system("shutdown /s /t 1")

 
 

    