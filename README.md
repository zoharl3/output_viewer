
# Output Viewer
A viewer (written in python) that receives logging messages from a (C++/Python/Matlab) logger.

Motivation.
I write Maya and Matlab plugins. When they crash, I lose my logging output. Also, at times they are buggy and won't print anything.

The viewer

- `output_viewer.pyw`

It listens on a local socket port, receives, and prints messages.
Run with pythonw to avoid opening a command window.

The following API communicates with it in different languages.

## Python

A simple client example

- `python_client\output_client_example.py`

## Matlab

Use

- `matlab_client\mlog.m`
- `matlab_client\mlogn.m`

A settings file 

- `matlab_client\mlog.settings`

that holds a flag (0/1) if to send to the viewer or not.
The viewer has a convenient checkbox to set it. 
The file is in the same directory as the matlab client, and the path to it needs to be set in `output_viewer.json` so the viewer would know where to look.

## C++

A client example, which uses an elaborate logger class (e.g., has a method println)

- `cpp_client\test\test_logger.cpp`

Unlike the matlab interface, we use here a global Log variable, which has a method set_send_to_viewer() to turn on/off sending output to the viewer (so there's no need for a settings file). 

## screenshots
![img](https://github.com/zoharl3/output_viewer/blob/main/screenshots/screenshot.png?raw=true)

