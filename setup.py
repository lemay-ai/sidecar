# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(

    name='lemay_ai_sidecar',

    version="0.0.1",

    packages=['lemay_ai_sidecar'],

    package_data={'': ['*.csv',]},

    include_package_data=True,

    install_requires=["pandas>=0.24.2","Keras>=2.2.4","sklearn","numpy>=1.16.2","fasttext>=0.9.1","gensim>=3.8.0"],

)
