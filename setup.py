from setuptools import setup

setup(name='piratescrape',
      version='0.1',
      description='A scraper for pirate websites',
      url='http://github.com/bababakchod/piratescrape',
      author='Pirates of The World',
      author_email='bababakchod@protonmail.com',
      license='MIT',
      packages=['piratescrape'],
      install_requires=[
          'requests',
	  'beautifulsoup4'
      ],
      zip_safe=False)
