#include "logger.h"

// Simple function to clear the log
void TimeLog::clear_log(std::string file_name)
{
	std::ofstream ofs(file_name, std::ofstream::out | std::ofstream::trunc);
	ofs.close();
}

// Time Logger function
// Empty call returns a time_point
// Full writes in log 
// args: > file: file stream to write in 
//		 > t: time_point to mark as the end time for the log 
//		 > func: name of the function / part of the code (include 'total' 
//				 to make it a total function
std::chrono::steady_clock::time_point TimeLog::TL(std::ofstream* file, std::chrono::steady_clock::time_point t, std::string func)
{
	std::chrono::steady_clock::time_point current = std::chrono::steady_clock::now();
	if (file == nullptr)
		return current;
	else
		*file << func << ": " << std::chrono::duration_cast<std::chrono::microseconds>(current - t).count()/1000000. << " sec\n";
	return current;
}
