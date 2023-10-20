from setuptools import setup, find_packages

setup(
    name='Tipster',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'charset-normalizer==3.1.0',
        'fastapi==0.100.1',
        'fastjsonschema==2.16.3',
        'Jinja2==3.1.2',
        'joblib==1.2.0',
        'jsonschema==4.17.3',
        'jupyter-client==7.3.0',
        'jupyter-core==4.10.0',
        'matplotlib==3.5.3',
        'matplotlib-inline==0.1.3',
        'nltk==3.8.1',
        'numpy==1.21.6',
        'pandas==1.3.5',
        'regex==2023.5.5',
        'requests==2.28.2',
        'requests-oauthlib==1.3.1',
        'scikit-learn==1.0.2',
        'scipy==1.7.3',
        'seaborn==0.12.2',
        'uvicorn==0.22.0',
        'wordcloud==1.9.2'
        
    ],
    entry_points={
        'console_scripts': [
            'Tipster = Tipster.main:main'
        ]
    },
)