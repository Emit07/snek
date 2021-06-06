from setuptools import setup, find_packages
import snek.__version__
import sys                                                                                                              
                                                                                                                        
if sys.version_info < (3, 5):                                                                                           
    sys.exit('Python 3.5 or greater is required for Snek')  

setup(
    name="SnekDB",
    version=snek.__version__,
    author="Alessandro De Leo",
    author_email="emit07@protonmail.com",
    description="A very small and leightweight nosql database written in pure python",
    packages=find_packages(),
    keywords=['python', 'database', 'local', 'json', 'object oriented'],
    url="https://github.com/pypa/sampleproject",
)
