#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Student():
    def __init__(self,name="Noname",age=18):
        self.name = name
        self.age = age
    
    def say(self):
        print("My name is {}".format(self.name))
        
def saying():
    print("我是一个函数")
    
if __name__ == "__main__":
    print("我是一个模块")
    

