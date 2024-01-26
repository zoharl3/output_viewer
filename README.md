
# Output Viewer
A C++/Python/Matlab logger that outputs formatted text to an external viewer.

Motivation.
I write Maya and Matlab plugins. When they crash, I lose my logging output. Also, at times they are buggy and won't print anything.

I wrote a viewer purely in python that receives and outputs messages. 

- `output_viewer.pyw`

It listens on a local socket port.
Run with pythonw to avoid opening a command window.

The following API communicate with it in different languages.

## Python

Just a simple client example

- `python_client\output_client_example.py`

## Matlab

Use

- `matlab_client\mlog.m`
- `matlab_client\mlogn.m`

The file 

- `matlab_client\mlog.settings`

holds a flag (0/1) if to send to the viewer or not.
The viewer has a convenient checkbox to set it. 
The file is in the same dir as the matlab client, and the path to it needs to be set in `output_viewer.json` so the viewer would know where to look.

## C++

A client example, which uses an elaborate logger class

- `cpp_client\test\test_logger.cpp`

Unlike the matlab interface, we use here a global Log variable, which has a method set_send_to_viewer() to turn on/off sending output to the viewer (so there's no need for a settings file). 

## screenshots
![img](https://github.com/zoharl3/output_viewer/blob/main/screenshots/screenshot.png?raw=true)

