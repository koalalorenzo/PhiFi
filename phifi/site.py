#!/usr/bin/python
# -*- coding=utf-8 -*-
#
#   Copyright 2011, 2012, 2013 Lorenzo Setale
#   See: http://blog.setale.me/2011/04/13/ancora-lamerozzi/
#   Do not modify without Lorenzo's permissions.
#   THIS SOFTWARE IS NOT OPENSOURCE!
#   

import mechanize
from random import choice
import string
from sys import stdout

class Site(object):
    def __init__(self, site):
        self.target = site['target']
        self.url = site['url']
        
        self.__form = None
        self.__browser = None
        
        self.__initializeBrowser()
        self.__locateLoginForm()
            
    def __initializeBrowser(self):
        """initializes browser object and connects to URL"""
        self.__browser = mechanize.Browser()
        try:
            self.__browser.open(self.url)
        except:
            self.__browser = None
            
    def __locateLoginForm(self):
        """Used to locate the form"""
        if not self.__browser:
            return False
        for form in self.__browser.forms():
            try:
                form.find_control(type='password')
                form.find_control(type='text')
                self.__form = form
                return
            except:
                continue
        if not self.__form: return False
        
            
    def __run_w_text_and_password(self):
        """Run request generating username/email and password"""
        if not self.__form or not self.__browser:
            return False
            
        self.__form.find_control(type='text').value = self.GenerateEmail()
        self.__form.find_control(type='password').value = self.GeneratePassword()
        self.__browser.form = self.__form
        try:
            self.__browser.submit().read()
            return True
        except:
            return False

    def run(self):
        """Runs requests with randomly generated values"""
        if not self.__form or not self.__browser:
            return False
        if self.target == "Facebook":
            return self.__run_w_text_and_password()
        
   
    def GeneratePassword(self):
        return ''.join([choice(string.letters + string.digits) for i in range(8)])
    
    def GenerateEmail(self):
        ext = ''.join([choice(string.letters + string.digits) for i in range(3)])
        host = ''.join([choice(string.letters + string.digits) for i in range(5)])
        return "%s@%s.%s" % (self.GeneratePassword(), host, ext)