from setuptools import setup, find_packages

with open('./README.md', 'r') as file :
    long_description = file.read()
AUTHOR_USER_NAME = 'HarishKumarSedu'
AUTHOR_EMAIL = 'harishkumarsedu@gmail.com'
REPO_NAME = 'matrix'
setup(
    name=REPO_NAME,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    version='0.0.1',
    py_modules=['.'],
    description=[ 'text/markdown','text/x-rst',],
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    long_description=long_description,
    packages=find_packages(),
    include_dirs=['.'],
    
)