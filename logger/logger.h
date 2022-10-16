#ifndef LOGGER
#define LOGGER

#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>

// Simple function to clear the log
void clear_log(std::string file_name)
{
    std::ofstream ofs(file_name, std::ofstream::out | std::ofstream::trunc);
    ofs.close();
}

auto TL(std::ofstream* file=nullptr, std::chrono::steady_clock::time_point t = std::chrono::steady_clock::now(), std::string func = "")
{
    std::chrono::steady_clock::time_point current = std::chrono::steady_clock::now();
    if (file == nullptr)
        return current;
    else
        *file << func << ": " << std::chrono::duration_cast<std::chrono::microseconds>(current - t).count()/1000000. << " sec\n";
    return current;
}

#endif // LOGGER

