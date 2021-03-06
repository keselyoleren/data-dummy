import dummy
from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()



setup(
    name=dummy.__title__,
    version=dummy.__version__,
    author=dummy.__author__,
    url="https://github.com/keselyoleren/data-dummy",
    description="Generate random data dummy",
    long_description_content_type='text/markdown',
    long_description='\n\n'.join((
        readme,
    )),
    license=dummy.__license__,
    packages=find_packages(),
    package_data={'dummy': ['dist.*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'dummy = dummy.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='test_dummy',
)


