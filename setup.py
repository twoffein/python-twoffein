#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# setup.py script for Twoffein
#
# Copyright (c) 2012 Malte Bublitz, https://malte-bublitz.de
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR
# AND/OR CONTRIBUTORS OF WindowsInfo BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 

from distutils.core import setup

setup( name         = 'Twoffein',
       version      = '0.20121212',
       description  = 'A module to access the Twoffein.com API easily',
       author       = 'Malte Bublitz',
       author_email = 'me@malte-bublitz.de',
       url          = 'http://twoffein.malte-bublitz.de/python',
       py_modules   = ['twoffein'],
		 data_files   = [
			 ("share/doc/python-twoffein",
		       ["AUTHOR", "CHANGELOG", "LICENSE", "README.md"]
		    )
			 ],
       license      = 'License :: OSI Approved :: BSD License',
       classifiers  = [
                       'Development Status :: 4 - Beta',
                       'Environment :: Plugins',
							  'Intended Audience :: Developers',
							  'License :: OSI Approved :: BSD License',
							  'Operating System :: Microsoft :: Windows',
							  'Operating System :: Microsoft :: Windows :: Windows 7',
							  'Operating System :: Microsoft :: Windows :: Windows Server 2003',
							  'Operating System :: Microsoft :: Windows :: Windows Server 2008',
							  'Operating System :: Microsoft :: Windows :: Windows Vista',
							  'Operating System :: Microsoft :: Windows :: Windows XP',
							  'Operating System :: POSIX',
							  'Operating System :: POSIX :: Linux',
							  'Programming Language :: Python',
							  'Topic :: Software Development :: Libraries :: Python Modules',
							  ]
     )
