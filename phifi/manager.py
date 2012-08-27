#!/usr/bin/python
# -*- coding=utf-8 -*-
#
#   Copyright 2011, 2012, 2013 Lorenzo Setale
#   See: http://blog.setale.me/2011/04/13/ancora-lamerozzi/
#   Do not modify without Lorenzo's permissions.
#   THIS SOFTWARE IS NOT OPENSOURCE!
#

import urllib
from random import choice
import json
from phifi.site import Site
import bz2

class Manager(object):
    def __init__(self):
        self.database = list()
        self.targets = list()
        self.stats = dict()
        self.fake_names = list()
        
    def __update_target_list(self):
        for site in self.database:
            if not site['target'] in self.targets:
                self.targets.append(site['target'])
                self.stats[site['target']] = 0
    
    def get_databases(self):
        compraw = urllib.urlopen('http://data.phishtank.com/data/619c6e75a725eaeb742479317a84ac543029df837249eedcd4a43bd9941d3c9a/online-valid.json.bz2').read()
        rawdecomp = bz2.decompress(compraw)
        self.database = json.loads(rawdecomp)
        self.__update_target_list()
        
    def __return_random_site(self):
        return choice(self.database)
    
    def __return_random_site_by_target(self, target_to_use):
        if not target_to_use in self.targets:
            raise Exception("'%s' not in Manager.targets list" % target_to_use)
        site = self.__return_random_site()
        if site['target'] == target_to_use:
            return site
        else:
            return self.__return_random_site_by_target(target_to_use)
        
    def __request_onetime(self,raw_site):
        site = Site(raw_site)
        restult = site.run()
        if result:
            self.stats[site.target] += 1
        return result
        
    def nuke_one_time_random_by_target(self, target_to_use):
        site = self.__return_random_site_by_target(target_to_use)
        return self.__request_onetime(site)
        
    def nuke_one_time_random(self):
        site = self.__return_random_site()
        return self.__request_onetime(site)

    def nuke_one_time(self, url):
        return self.__request_onetime(site)

    def start_loop(self, site=None, target=None, times=100):
        if target:
            site = self.__return_random_site_by_target(target)
        
        elif site == None:
            site = self.__return_random_site()
        
        for a in range(0,times):
            self.__request_onetime(site)
        