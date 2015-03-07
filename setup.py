from distutils.core import setup

setup(
	name='rietref',
	version='0.1dev',
	url='http://github.com/jsiples/rietref',
	license='Creative Commons Attribution-Noncommercial-Share Alike license',
	author='Justin Siples',
	install_requires=[
		'numpy >= 1.9.2',
		'scipy >= 0.15.1'],
	author_email='jsiples@gmail.com',
	description='Minimizes XRD using rietfeld refinement',
	long_description=open('README.md').read(),
	packages=['rietref'],
	platforms='any',
	classifiers = [
		'Programming Language :: Python',
		'Development Status :: 4 - Beta',
		'Natural Language :: English',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: MacOS :: MacOS X'
		],
)