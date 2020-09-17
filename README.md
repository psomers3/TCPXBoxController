This is a simple module to forward the signals created from the [Xbox-Controller-for-Python](https://github.com/r4dian/Xbox-Controller-for-Python) package for an Xbox controller to a TCP port using the [DataSocket](https://github.com/psomers3/PyDataSocket) package for use with python and matlab. This code only works on Windows, but the sent signals may be received on any platform, since DataSocket is platform independent.

### Install
```
git clone https://github.com/psomers3/TCPXBoxController.git
cd TCPXboxController
pip install -r requirements.txt
pip install .
```

### Usage
This may be used as an object in a python script with 
```python
from TCPXboxController import TCPXboxController
controller = TCPXboxController(dev_num=0, send_socket_port=63636, rec_socket_port=63637, socket_ip='localhost')
```

or 

As a standalone script with python as follows (the `-h` flag brings up the help menu)
```
python -m TCPXboxController -h
```

or 

Using the setup.spec file with pyinstaller, a standalone (no python environment required) executable can be created. See next section.

### Executable
Make the executable using 
```
pyinstaller setup.spec
```
See [Releases](https://github.com/psomers3/TCPXBoxController/releases) for compiled versions for Windows 10. Usage is the same as running as standalone script.
