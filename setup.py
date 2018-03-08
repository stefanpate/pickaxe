from setuptools import setup

setup(name='minedatabase',
      version='1.0',
      description='Metabolic In silico Network Expansions',
      url='http://github.com/JamesJeffryes/mine-database',
      author='James Jeffryes',
      author_email='jamesgjeffryes@gmail.com',
      license='MIT',
      packages=['minedatabase',
                'minedatabase.tests',
                'minedatabase.NP_Score'],
      install_requires=['pymongo'],
      package_data={'minedatabase': ['data/*'],
                    'minedatabase.NP_Score': ['*.gz'],
                    'minedatabase.tests': ['data/*'],
                    },
      include_package_data=True,
      extras_require={},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Scientific/Engineering :: Chemistry',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
      ],
      )