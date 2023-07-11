#!/usr/bin/python3
'''Defining a Student class
'''


class Student:
    '''Student class defines a student
    '''
    def __init__(self, first_name, last_name, age):
        '''This is the intializer function'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''this function retrieves a dict representation of class instance'''
        return self.__dict__
