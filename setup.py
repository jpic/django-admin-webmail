#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-admin-email',
    version="0.0",
    author='James Pic',
    author_email='jamespic@gmail.com',
    description='Webmail in django-admin',
    url='http://github.com/jpic/django-admin-webmail',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    requires=[
        'django_mptt',
        'django_annoying',
        'django_ajax_selects',
    ],
)
