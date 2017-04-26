#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2016-2017 Conix Cybersecurity
#
# This file is part of BTG.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from lib.io import display
from lib.cache import Cache

class Sslblacklist():


    def __init__(self,ioc,type,config):
        self.config = config
        if self.config["sslblacklist_enabled"]:
            self.module_name = __name__.split(".")[1]
            self.types = ["SHA1"]
            self.search_method = "Online"
            self.description = "Search IOC in SslBlacklist database"
            self.author = "Conix"
            self.creation_date = "12-04-2017"
            self.type = type
            self.ioc = ioc
            if type in self.types:
                self.search()



    def search(self):
        display(self.module_name, self.ioc, "INFO", "Searching...")
        url = "https://sslbl.abuse.ch/blacklist/"
        paths = [
            "sslblacklist.csv"
        ]

        for path in paths:
            content = Cache(self.module_name, url, path, self.search_method).content
            for line in content.split("\n"):
                if self.ioc in line:
                    infos=line.split(',')
                    display(self.module_name, self.ioc, "FOUND", "%s | %s%s" % (infos[2],url,path))
                    return