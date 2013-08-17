#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname

import scholar 

setup(name='scholar',
      version = scholar.__version__,
      author = scholar.__author__ , 
      author_email = scholar.__email__,
      url = 'http://github.com/johnjosephhorton/Scholar',
      packages = [''],
      #package_data = {'':['']},
      package_dir= {'':'.'}, 
      entry_points={
          'console_scripts':
              ['scholar = scholar:main',
               ]}, 
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ),
      install_requires=['BeautifulSoup>=3.2.1'],
      )
