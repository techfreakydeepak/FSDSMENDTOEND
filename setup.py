from setuptools import find_packages, setup

setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='Deepak Singh',
    author_email='itsdeepaksingh00@gmail.com',
    description='A package for predicting diamond prices',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/DimondPricePrediction',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your dependencies here
        # 'numpy',
        # 'pandas',
        # 'scikit-learn',
    ],
)
