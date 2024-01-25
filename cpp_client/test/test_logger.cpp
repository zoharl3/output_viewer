
#include "../logging.h"
#include <iostream>
#include <cstdlib>

int main(int argc, char **argv)
{
    int level = 3;
    if (argc == 2)
        level = atoi(argv[1]);
    Log.set_level(level);
    std::cout << "Outputting at level " << Log.level() << std::endl;

	Log.set_send_to_viewer(true);
	//Log.send_to_viewer("hi viewer\n");
	Log << "hi " << 0;
	Log << std::endl;

    Logger::Block block = Log.block(2, "Block()");

    ////////////////////////////////////////////////////////////
    Log.println("FORMATTED OUTPUT");

    Log.println("Hi");
    Log.start_block(4, "Hi 4");
    Log.start_block(1, "Hi 1");
    Log.println(2, "Hi 2");
    Log.println(3, "Hi 3");
    Log.end_block(1, "Hi 1");
    Log.println(4, "Hi 4");
    Log.end_block(4, "Hi 4");

    Log.error("Error1");

    // Start outputting to a log file
//    Log.use_file("testing.log");

    Log.start_block("Stuff");
        Log.println("indented?");
    Log.end_block("Stuff");

    Log.println(0, "Test1 0");
    Log.start_block(0, "Stuff 0");
        Log.println(0, "indented? 0");
    Log.end_block(0, "Stuff 0");

    Log.println(1, "med Test1 1");
    Log.start_block(1, "med STUFF 1");
        Log.println(2, "high indented again? 2");
        Log.println(3, "ultra indented again? 3");
        Log.warn("Test1");
    Log.end_block(1, "med STUFF 1");

    ////////////////////////////////////////////////////////////
    Log.use_stream(std::cout);
    Log.print() << "OSTREAM OUTPUT" << std::endl;

    Log.print() << "Hi" << std::endl;
    Log.start_block(4) << "Hi 4" << std::endl;
    Log.start_block(1) << "Hi 1" << std::endl;
    Log.print(2) << "Hi 2" << std::endl;
    Log.print(3) << "Hi 3" << std::endl;
    Log.end_block(1) << "Hi 1" << std::endl;
    Log.print(4) << "Hi 4" << std::endl;
    Log.end_block(4) << "Hi 4" << std::endl;

    // Start outputting to a log file
//    Log.use_file("testing_stream.log");

    Log.error() << "Test1" << std::endl;
    Log.start_block() << "Stuff" << std::endl;
        Log.print() << "indented?" << std::endl;
    Log.end_block() << "Stuff" << std::endl;

    Log.print(0) << "Test1 0" << std::endl;
    Log.start_block(0) << "Stuff 0" << std::endl;
        Log.print(0) << "indented? 0" << std::endl;
    Log.end_block(0) << "Stuff 0" << std::endl;

    Log.print(1) << "med Test1 1" << std::endl;
    Log.start_block(1) << "med STUFF 1" << std::endl;
        Log.print(2) << "high indented again? 2" << std::endl;
        Log.print(3) << "ultra indented again? 3" << std::endl;
        Log.warn() << "Test1" << std::endl;
    Log.end_block(1) << "med STUFF 1" << std::endl;

    ////////////////////////////////////////////////////////////
    // Go back to cout before the block finishes
    Log.use_stream(std::cout);
}

