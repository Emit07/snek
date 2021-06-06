from setuptools import setup, find_packages
import sys                                                                                                              
                                                                                                                        
if sys.version_info < (3, 5):                                                                                           
    sys.exit('Python 3.5 or greater is required for Snek')  

setup(
    name="SnekDB",
    version="0.0.1",
    author="Alessandro De Leo",
    author_email="emit07@protonmail.com",
    description="A very small and leightweight nosql database written in pure python",
    packages=find_packages(),
    keywords=['python', 'database', 'local', 'json', 'object oriented'],
    url="https://github.com/pypa/sampleproject",
)