from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A python application for image encryption decryption'
LONG_DESCRIPTION = 'A package that allows you to encrypt and decrypt Images'
# Setting up
setup(
    name="image_enc_dec",
    version=VERSION,
    author="Tejas Dixit(PANDATD)",
    author_email="<coddersclub@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/CodderscluB/Image_Encryption_Decryption/",
    project_urls={
        "Bug Tracker": "https://github.com/CodderscluB/Image_Encryption_Decryption/issues",
        "Maintainer": "https://github.com/pandatd/",
        "Blog":"https://medium.com/coddersclub",   
    },
    long_description=long_description,
    packages=find_packages(),
    install_requires=['tk'],
    keywords=['python', 'encryption', 'decryption', 'encryptiondecryption',],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
