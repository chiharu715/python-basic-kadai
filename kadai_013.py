# -*- coding: utf-8 -*-
"""kadai_013.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1luRl-Zrp0k5yjBXCrmQQaxzrDAnY_KkQ
"""

def total_price(price,tax):
  sales_tax = price * (tax / 100)
  total_price = price + sales_tax
  print(total_price)

total_price(100,10)