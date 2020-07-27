from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

DESCRIPTION = """
            Detection of outlier with mahanalobis distance 
            which have access of the parameters (means and precision matrice) with algo GMM or Bayesian GMM provide by sklearn
            """
setup(
    name="MDO",
    version="1.0.3",
    author="Jonathan Ndamba",
    author_email="jonathan.ndamba.pro@gmail.com",
    url="https://github.com/JonathanNdambaPro/MDO",
    description=DESCRIPTION,
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas>=1.0.5',
                      'scikit-learn>=0.23.1',
                      'sklearn>=0.0'
                      ]
)



