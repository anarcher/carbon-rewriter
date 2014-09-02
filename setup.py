#!/usr/bin/env python
import sys
import os
import re
import glob
import ConfigParser

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO


#To parse package version 
for line in open("carbon-rewriter/version.py"):
    m = re.match('__version__ = "(.*)"', line)
    if m:
        version = m.group(1)
        break
    else:
        sys.exit("error: can't find version information")


with open("setup.cfg","r") as f:
    orig_setup_cfg = f.read()
cf = ConfigParser.ConfigParser()
cf.readfp(BytesIO(orig_setup_cfg),"setup.cfg")

if os.environ.get('GRAPHITE_NO_PREFIX'):
    cf.remove_section('install')
else:
    try:
        cf.add_section('install')
    except ConfigParser.DuplicateSectionError:
        pass
    cf.set('install','prefix','/opt/graphite')
    cf.set('install','install-lib','%(prefix)s/lib')

with open('setup.cfg','wb') as f:
    cf.write(f)

if os.environ.get('USE_SETUPTOOLS'):
    from setuptools import setup
    setup_kwargs = dict(zip_safe=0)
else:
    from disutils.core import setup
    setup_kwargs = dict()


requires = [
    "carbon"
]

conf_files = [ ('conf', glob('conf/*.example')) ]
install_files = conf_files

try:
    setup(
        name='carbon-rewriter',
        version=version,
        author='anarcher',
        author_email = 'anarcher@gmail.com',
        license='Apache Software License 2.0',
        description='Carbon-rewriter is rewriting metric name and then sending to destinations',
        long_description='Carbon-rewriter is rewriting metric name and then sending to destinations',
        packages=['carbon-rewriter'],
        scripts=glob('bin/*'),
        data_files=install_files,
        install_requires=requires,
        **setup_kwargs
    )
finally:
    with open('setup.cfg','w') as f:
        f.write(orig_setup_cfg)


