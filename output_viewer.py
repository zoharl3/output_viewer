
# obsolete website
# http://forums.cgsociety.org/showthread.php?f=89&t=1322430

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineCore import *
import sys, os, time, psutil, json
import socketserver
import webbrowser

# suppress output
if 0:
    sys.stdout = open("output_viewer.console", "a", 0)
    sys.stderr = open("output_viewer.console", "a", 0)

g_port = 32313

g_vtype = 0 # viewer type: 0 - QTextEdit, 1 - QWebView (slow)

# need to print something (e.g. '.') for the style to take effect (else it prints with spaces)
g_header = '''
<body bgcolor="black">
<font size="6" face="Consolas" color="silver">.<br>
'''
g_modifier = '''<font size="6" face="Consolas" color="silver">'''

class MyWindow(QWidget):
    sig_new_input = Signal( str )

    def __init__(self, *args): 
        QWidget.__init__(self, *args)
        
        # mlog.settings
        self.mlog_settings = r"C:\prj\confstruct\scripts\mlog.settings"
        with open( 'output_viewer.json' ) as f:
            data = json.load( f )
            self.mlog_settings = data["mlog_settings"]

        # layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.data_len = 0
        self.modifier = g_modifier # style
        text = g_header
        if g_vtype:
            self.view = QWebView() # obsolete: too slow
            self.frame = self.view.page().mainFrame()
            self.view.setHtml(text)
        else:
            self.view = QTextEdit()
            #self.view.setText(text)
            self.view.setHtml(text)
            self.view.setReadOnly(True)
            #self.view.setFontPointSize(12)
            #self.view.setTextColor(QColor(192,1,1))
        layout.addWidget(self.view)

        layout2 = QHBoxLayout()
        layout.addLayout(layout2)

        button = QPushButton('Clear')
        layout2.addWidget(button)
        button.clicked.connect(self.clear_pressed)

        button = QPushButton('Save output_viewer.html')
        layout2.addWidget(button)
        button.clicked.connect(self.save_pressed)

        button = QPushButton("'hi'")
        layout2.addWidget(button)
        button.clicked.connect(self.hi_pressed)

        button = QPushButton('Kill matlab')
        layout2.addWidget(button)
        button.clicked.connect(self.kill_proc_pressed)

        checkb = QCheckBox('mlog')
        layout2.addWidget(checkb)
        checkb.stateChanged.connect(self.cb_mlog_pressed)
        state = 1
        with open( self.mlog_settings, 'r' ) as f:
            fstate = f.read(1)
            if fstate == '1':
                state = 2
            else:
                state = 0
        checkb.setCheckState( Qt.CheckState( state ) )

        checkb = QCheckBox('Wrap Text')
        layout2.addWidget(checkb)
        checkb.stateChanged.connect(self.wrap_text_pressed)
        checkb.setCheckState( Qt.CheckState( 2 ) )

        self.checkb_auto_scroll = QCheckBox('Auto-scroll')
        layout2.addWidget(self.checkb_auto_scroll)
        self.checkb_auto_scroll.stateChanged.connect(self.checkb_auto_scroll_pressed)
        self.checkb_auto_scroll.setCheckState( Qt.CheckState( 2 ) )

        self.sig_new_input.connect( self.parse_input )

    def signal_new_input(self, html):
        # connected to parse_input
        self.sig_new_input.emit( html )

    def parse_input(self, data):
        if self.data_len > 500000:
            self.clear_pressed()
        self.data_len += len(data)
    
        #print( "received data:", data )
        meta, text = data.split('|', 1)
        #print( "received: meta='%s', text='%s'" % (meta, text) )
        if len(meta):
            if meta == 'clear':
                self.clear_pressed()
                return
            self.modifier = meta

        if text:
            print(text)
            if not len(self.modifier):
                #text = text + '\n'
                self.add_content(text, 1)
            else:
                text = text.replace('\n', '<br>')
                #if data == '\n': # a lonely \n doesn't output in <pre>
                #    data = '<br>'
                text = "<pre>" + text + "</pre>"
                html = self.modifier + text
                self.add_content(html, 0)
                self.modifier = ''

    def add_content(self, data, bTextOnly):
        old_scrollbar_value = self.view.verticalScrollBar().value()
        if g_vtype:
            #self.view.setHtml(self.text)
            self.frame.setScrollPosition(QPoint(0, self.frame.contentsSize().height()))
        else:
            self.view.moveCursor(QTextCursor.End)
            if bTextOnly:
                #self.view.append(data)
                self.view.textCursor().insertText(data)
                #self.view.insertPlainText(data)
            else: # slower
                #self.view.setHtml(self.text)
                self.view.insertHtml(data)
            self.view.moveCursor(QTextCursor.End)
        if not self.checkb_auto_scroll.checkState().value:
            self.view.verticalScrollBar().setValue(old_scrollbar_value)
        
    def checkb_auto_scroll_pressed(self):
        if self.checkb_auto_scroll.checkState().value:
            self.view.verticalScrollBar().setValue(self.view.verticalScrollBar().maximum())
        
    def clear_pressed(self):
        text = g_header
        self.modifier = g_modifier
        if g_vtype:
            self.view.setHtml(text)
        else:
            self.view.setHtml(text)
        self.data_len = 0
        
    def save_pressed(self):
        path = os.path.dirname(os.path.realpath(__file__))
        fname = path + '/output_viewer.html'
        of = open(fname, 'w')
        of.write(self.view.toHtml())
        webbrowser.open('file://'+fname, new=1)

    def hi_pressed(self):
        #s = '<font color="lime" size="6" face="Consolas">hi<br>'
        s = 'hi'

        self.view.moveCursor(QTextCursor.End)
        
        #self.view.insertHtml(s)
        #self.view.append(s)
        self.view.textCursor().insertText(s)

    def kill_proc_pressed(self):
        pname = "MATLAB.exe"
        # get latest process
        proc = []
        create_time = 0
        for proc2 in psutil.process_iter( attrs=['pid', 'name'] ):
            #print(proc2.info)
            if proc2.name() == pname and proc2.create_time() > create_time:
                proc = proc2
                create_time = proc2.create_time()
                msg = "Found %d" % proc.pid
                print(msg)
                self.view.moveCursor(QTextCursor.End)
                self.view.textCursor().insertText(msg + "\n")
                
        if not proc:
            msg = "Process '%s' couldn't be found" % pname
            print(msg)
            st = '<font color="red" size="6" face="Consolas">%s<br>' % msg
            self.view.moveCursor(QTextCursor.End)
            self.view.insertHtml(st)
            return
            
        proc.kill()

    def cb_mlog_pressed(self, state):
        with open( self.mlog_settings, 'w' ) as f:
            if state == 0:
                f.write('0')
            else:
                f.write('1')

    def wrap_text_pressed(self, state):
        if state == 0:
            self.view.setLineWrapMode(QTextEdit.NoWrap)
        else:
            self.view.setLineWrapMode(QTextEdit.WidgetWidth)

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        win = self.server.win

        data = b''
        it = 0
        while 1:
            buf = self.request.recv(100000)
            ld = len(buf)
            #print( "Received (%d)" % it, ld, "bytes; buf:", buf )
            if ld == 0:
                break
            data = data + buf
            it = it + 1
        #self.request.sendall('got it')
        if len(data) > 0:
            win.signal_new_input( data.decode("utf-8") )

class MyServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, win):
        print( f'Listening on {server_address}' )
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)
        self.win = win

class ServerThread(QThread):
    def __init__(self, win):
        QThread.__init__(self)
        self.win = win

    def run(self):
        host = "localhost"
        server = MyServer((host, g_port), MyTCPHandler, self.win)
        server.serve_forever()

def main():
    print("Started on " + time.strftime("%c"))
    app = QApplication(sys.argv)

    win = MyWindow()
    win.setWindowTitle('Output viewer')
    win.showMaximized()
    icon = QIcon('output_viewer.png')
    app.setWindowIcon(icon)
    win.setWindowIcon(icon)

    serverThread = ServerThread(win)
    serverThread.start()

    app.exec()
    
    serverThread.terminate()
    serverThread.wait()
        
if __name__ == "__main__":
    main()
    

