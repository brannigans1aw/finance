import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="dc-campaign-finance-data",
    version="0.1.0",
    py_modules = ['dc_campaign_finance_data'],
    entry_points={
        'console_scripts': [
            'dc-campaign-finance-data=dc_campaign_finance_data:cli'
        ]
    },
    install_requires=[
        'requests',
        'click'
    ],

    # metadata for upload to PyPI
    long_description=open('README.md').read(),
    author="Saul Shanabrook",
    author_email="s.shanabrook@gmail.com",
    description="Provides data from http://www.ocf.dc.gov/serv/download.asp in a nicer way",
    keywords="finance DC campaign elissa",
    url="http://github.com/techforelissa/finance-scraper",
)
