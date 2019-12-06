from setuptools import setup, find_packages
import os

#-Write Versions File-#
# Major-Minor-Patch (release-status)
VERSION = '0.0.1a'

def write_version_py(filename=None):
    """
    This constructs a version file for the project
    """
    doc = "\"\"\"\nThis is a VERSION file and should NOT be manually altered\n\"\"\""
    doc += "\nversion = '%s'\n" % VERSION

    if not filename:
        filename = os.path.join(os.path.dirname(__file__), 'transcripty', 'version.py')

    fl = open(filename, 'w')
    try:
        fl.write(doc)
    finally:
        fl.close()

# This is a file used to control the transcripty.__version__ attribute
write_version_py()

#-Meta Information-#
#~~~~~~~~~~~~~~~~~~#

DESCRIPTION = "Transcripty is a package for replicating section 2 of Hendricks Leukhina 2017"

LONG_DESCRIPTION = """
Transcripty is a package for replicating section 2 of _How risky is college
investment_ by Lutz Hendricks and Oksana Leukhina.

Section 2 presents a model of college credit accumulation. The probability
that a student passes a particular course is governed by a probability
that is conditional on a student's innate ability.

- A student\'s ability given by `a \\sim N(0, 1)`
- A student\'s GPA given by `GPA = a + \\varepsilon`  where  `\\varepsilon \\sim N(0, \\sigma^2)`
- A student enrolls in 12 courses per year which are each worth 3 credits
- A student passes each course with probability p(a)
- Student graduates if they accumulate 125 credits by the end of year 6
"""

LICENSE = 'MIT'

#-Classifier Strings-#
#-https://pypi.python.org/pypi?%3Aaction=list_classifiers-#
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
]

#-Setup-#
#~~~~~~~#

setup(
    name='transcripty',
    packages=find_packages(),
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    author='Chase Coleman',
    author_email='cc7768@gmail.com',
    url='https://github.com/cc7768/transcripty',
    project_urls={
        'Documentation': 'http://transcripty.readthedocs.io/en/latest',
        'NYU Predoctoral repo': 'https://github.com/nyupredocs'
    },
    keywords=['transcript', 'college', 'quantitative', 'economics'],
    install_requires=[
        'numpy',
        'scipy>=1.0.0',
    ],
    include_package_data=True
)

