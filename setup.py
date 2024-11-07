import setuptools

install_requires = [
## to do
]

setuptools.setup(
    name="govy",
    version="0.0.1",
    license='Closed License',
    author="Daehan Won",
    author_email="daehan2lab@gmail.com",
    description="Software System for Project Govy",
    long_description=open('README.md').read(),
    #url="",
    packages=setuptools.find_packages(), 
    install_requires=install_requires, 
    #project_urls={
    #    "docs": ""
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"]
)