from setuptools import setup


setup(
    name="TCPXboxController",
    version="0.0.1",
    author="Peter Somers",
    author_email="peter.somers@isys.uni-stuttgart.de",
    description="A module to forward xbox controller signals over TCP Sockets",
    # url="https://github.tik.uni-stuttgart.de/ac121730/JetsonEV",
    packages=['TCPXboxController'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires='>=3.4',
    install_requires=['PyDataSocket',
                      'xinput',
                      'pyglet']
)