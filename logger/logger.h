#ifndef LOGGER
#define LOGGER

#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>
#include <string>

namespace TimeLog {
	void clear_log(std::string file_name);
	std::chrono::steady_clock::time_point TL(std::ofstream* file=nullptr, std::chrono::steady_clock::time_point t = std::chrono::steady_clock::now(), std::string func = "");
}

#endif // LOGGER

