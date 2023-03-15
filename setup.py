from setuptools import setup, find_packages
from main import VERSION

setup(
    name= "GetComics API",
    version= VERSION,
    description= "An Unofficial API for Getcomics.info, built on FastAPI and BeautifulSoup",
    author= "Faseeh Shahzad Memon",
    author_email= "faseehshahzad2@gmail.com",
    url= "https://github.com/Jupiee/getcomics-api",
    packages= find_packages(),
    install_requires= [
        "fastapi",
        "uvicorn",
        "bs4",
        "aiohttp"
    ],
    classifiers= [
        "Programming Language :: Python :: 3.10"
    ],
    python_requires= ">3.9",
)