# output_viewer
A (C++/Python/Matlab) logger that outputs formatted text to an external viewer.

Motivation.
I used to write Maya and Matlab plugins, and when they crashed, I would lose my logging output. Also, at times they are buggy and won't output.

I wrote a viewer purely in python that receives and output messages. It listens on a local socket port.

The following API communicate with it in different languages.

Python

Just a simple client example.
python_client\output_client_example.py

Matlab

Use
matlab_client\mlog.m
matlab_client\mlogn.m
from scripts. 

The file 
matlab_client\mlog.settings
holds a flag (0/1) if to send to the viewer or not.
The viewer has a convenient checkbox to set it, but the path to the settings file is currently hard-coded to my computer (change it, it's a python script, or just set the settings file manually).

C++

A client example
cpp_client\test\test_logger.cpp

