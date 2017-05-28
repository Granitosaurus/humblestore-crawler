from distutils.core import setup

setup(
    name='humblebundle',
    version='1',
    packages=['humble'],
    install_requires=['requests'],
    url='https://github.com/Granitosaurus/humblestore-crawler',
    license='GPLv3',
    author='granitosaurus',
    author_email='bernardas.alisauskas@gmail.com',
    description='simple crawler for humble bundle store with reddit comments output.'
)
