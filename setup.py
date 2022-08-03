from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='deenorm',
    version='2.0.0',    
    description='Python package for convert text to phoneme ipa, use for cross language embedding Text-to-speech Reseach',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['deenorm'],
    include_package_data=True,
    install_requires=["vinorm", "underthesea", "eng_to_ipa"],

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Free for non-commercial use',
        'Natural Language :: Vietnamese',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],  
)
