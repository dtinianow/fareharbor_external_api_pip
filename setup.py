import os
import sys
from setuptools import setup

setup(
  name = 'fareharbor_external_api',
  version = '0.1.0',
  description = 'A Python wrapper for the FareHarbor External API',
  url = 'GITHUB URL',
  author = ["David Tinianow", "Caleb Cowen", "Zack Forbing"]
  author_email = "support@fareharbor.com",
  license = "MIT",
  keywords = "fareharbor external api wrapper",
  packages = find_packages(exclude=['contrib', 'docs', 'tests*']),
  install_requires = ['requests']
)
