from setuptools import setup, find_packages


setup(
    name='alfred-db',
    version='0.1.dev',
    license='ISC',
    description='Alfred models',
    url='https://github.com/alfredhq/alfred-db',
    author='Alfred Developers',
    author_email='team@alfredhq.com',
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy',
    ],
)
