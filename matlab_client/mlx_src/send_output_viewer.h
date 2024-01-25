
#pragma once

#include "logging.h"

using namespace std;

struct OutputViewer {
    OutputViewer::OutputViewer() {
        Log.set_send_to_viewer( 1 );
    }
    
    void print( string st ) {
        //::print( st.c_str() );
        Log.send_to_viewer( st, 1 );
    }
};
