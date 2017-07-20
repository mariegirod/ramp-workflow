#! /usr/bin/env python

# Copyright (C) 2017 Balazs Kegl

import os

from setuptools import setup, find_packages


version = None
with open(os.path.join('rampwf', '__init__.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('\'')
            break
if version is None:
    raise RuntimeError('Could not determine version')


descr = """Toolkit for building analytics workflows on the top of pandas and
scikit-learn. Primarily intended to feed RAMPs."""

DISTNAME = 'ramp-workflow'
DESCRIPTION = descr
MAINTAINER = 'Balazs Kegl'
MAINTAINER_EMAIL = 'balazs.kegl@gmail.com'
URL = 'None'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/paris-saclay-cds/ramp-workflow'
VERSION = version


if __name__ == "__main__":
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          include_package_data=True,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=open('README.md').read(),
          zip_safe=False,  # the package can run out of an .egg file
          classifiers=['Intended Audience :: Science/Research',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved',
                       'Programming Language :: Python',
                       'Topic :: Software Development',
                       'Topic :: Scientific/Engineering',
                       'Operating System :: Microsoft :: Windows',
                       'Operating System :: POSIX',
                       'Operating System :: Unix',
                       'Operating System :: MacOS'],
          platforms='any',
          packages=find_packages(),
          entry_points={
              'console_scripts': [
                  'ramp_test_submission='
                  'rampwf.utils.command_line:ramp_test_submission',
                  'ramp_test_notebook='
                  'rampwf.utils.command_line:ramp_test_notebook',
              ]})
