
CMAKE_MINIMUM_REQUIRED(VERSION 3.13)

set( PROJECT_NAME "test_logger" )
project( ${PROJECT_NAME} )

ADD_DEFINITIONS( /std:c++17 )

# Source Files
file(GLOB sources *.c *.cpp *.h *.hpp)

# source2
set( sources2
    ../logger.cpp
    ../logging.cpp
    )
include_directories( ".." )

add_executable( ${PROJECT_NAME} ${sources} ${sources2} )

set_property(TARGET ${PROJECT_NAME} PROPERTY FOLDER ${PROJECT_NAME})

# boost
find_package(Boost)
if(Boost_FOUND)
    message( "Boost found: ${Boost_INCLUDE_DIRS}" )
    target_include_directories( ${PROJECT_NAME} PRIVATE ${Boost_INCLUDE_DIRS} )
    target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES})
endif()

# VS properties
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ${PROJECT_NAME})





