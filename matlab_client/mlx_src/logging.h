
#pragma once

#include "logger.h"

// Verbosity
const int L_LOW = 0; // alway showing
const int L_MED = 10;
const int L_MEDPLUS = 15;
const int L_HIGH = 20;
const int L_FREQ = 30;
extern Logger Log;

template< typename... Args >
Logger& emphasize( const char *st, Args&&... args ) {
    return Log.emphasize( st, std::forward<Args>(args)... );
}

template< typename... Args >
Logger& emphasize2( const char *st, Args&&... args ) {
    return Log.emphasize2( st, std::forward<Args>(args)... );
}

template< typename... Args >
Logger& emphasize3( const char *st, Args&&... args ) {
    return Log.emphasize3( st, std::forward<Args>(args)... );
}

template< typename... Args >
Logger& print( const char *st, Args&&... args ) {
    return Log.print( st, std::forward<Args>(args)... );
}

template< typename... Args >
Logger& println( const char *st = "", Args&&... args ) {
    return Log.println( st, std::forward<Args>(args)... );
}

template< typename... Args >
Logger& warn( const char *st, Args&&... args ) {
    return Log.warn( st, std::forward<Args>(args)... );
}

template< typename... Args >
Logger& error( const char *st, Args&&... args ) {
    return Log.error( st, std::forward<Args>(args)... );
}

template< typename... Args >
std::exception exception2( std::string st, Args&&... args ) {
    char msg[ 500 ];
    sprintf( msg, st.c_str(), std::forward<Args>(args)... );
    return std::exception( msg );
}

#define LOG_MESSAGE_BLOCK(level, message) const Logger::Block &_Log_Block = Log.block(level, message);

