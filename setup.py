from setuptools import setup, find_packages

setup(
    name='chx_free_likes',
    version='1.0.0',
    author='Chx 🇮🇳',
    author_email='manishop1234g@gmail.com',
    description='🇮🇳 Free Fire Indian Likes API Wrapper by Chx',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chxapiDev01/Chxlikes',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Utilities'
    ],
    python_requires='>=3.6',
)
