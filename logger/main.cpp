#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>
#include "logger.h"

// dummy func to spend time
void loop_wait(const size_t n, const int millisecs)
{
    for (size_t i = 0; i<n; i++)
    {
        std::this_thread::sleep_for(std::chrono::milliseconds(millisecs));
    }
}

// big func including sub-funcs
void total_func()
{
    // file to save
    std::string file_name = "../data/mylog.tl";
    std::ofstream file(file_name, std::ios_base::app); /// < open the stream

    auto t = TL(); /// < start time
    loop_wait(1, 1890); /// < func 1
    TL(&file, t, "loop_wait1"); /// < log time

    t = TL(); /// < check point time
    loop_wait(1, 5203);
    TL(&file, t, "loop_wait2");

    t = TL();
    loop_wait(7, 101.89);
    TL(&file, t, "loop_wait3");

    // unincluded - time untracked
    loop_wait(2, 250.4);

    file.close();
}

int main()
{
    // file to save
    std::string file_name = "../data/mylog.tl";
    clear_log(file_name); /// < put this to clear the log prior to write
    std::ofstream file(file_name, std::ios_base::app);

    auto tbegin = TL(); /// < start time
    total_func(); /// < call function
    TL(&file, tbegin, "Total [total_func]"); /// < log time
    file.close(); /// < close stream

    return 0;
}

