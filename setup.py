#python setup.py build
#python -m build

from setuptools import setup, find_packages

setup{
	name='twittercounter',
	version='1.0',
	author='bhargav',
	author_email='bhargav.vummadi@ou.edu',
	packages=find_packages(exclude=('test','docs')),
	setup_requires=['pytest-runner'],
	test_require=['pytest']

}
