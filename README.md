# C++ Runtime Analyzer
Set of methods in python and C++ to analyze a C++ code runtime

## Overview
The package proposes a runtime logger and a runtime analyzer. The included classes and methods are very simple to use and provide a clean way to visualize efficiently
runtime data.

## Requirements
Basic setup:
- Tested on Windows
- Python 3
- C++14

Additional requirements (python):
- Numpy
- Matplotlib

## Usage
There are two parts: a first one involving the C++ code you want to analyze; the second one for the analysis and report.

### Recording the runtime
To use the library, simply include "logger.h" to the current code file. logger.cpp and logger.h have to be correctly targetted by the software.
The logging occurs within a simple text file. Usually, it is recommended that you start the logging with:
```c++
 std::string filename = "full_path_to_log_file";
 TimeLog::clear_log(filename); // clear the log file
 std::ofstream ios(filename, std::ios_base::app); // open a stream to the log file
```

The basic commands sequence reads as follow:

```c++
#include "logger.h"

int main
{
  std::string filename = "full_path_to_log_file";
  TimeLog::clear_log(filename); // clear the log file
  std::ofstream ios(filename, std::ios_base::app); // open a stream to the log file
  
  auto t_total = TimeLog::TL(); // starting point
  
  auto t = TimeLog::TL(); // time point
  func1();
  TimeLog::TL(&ios, t, "func1"); // log runtime for func1
  
  t = TimeLog::TL(); // time point
  func2();
  TimeLog::TL(&ios, t, "func2"); // log runtime for func2
  
  TimeLog::TL(&ios, t_total, "total [main]"); // log total runtime
  ios.close(); // close the stream
  
  return 0
}
```
The previous snippet demonstrates how to log several sub-functions within a part of the code (which can be a larger method).
You can also time-log different functions at various parts of the code, but you'll have to use other log files.
**You must always specify the full runtime log by writing "total [name_of_the_total_part]" in the TimeLog::TL writer.**

### Analyze and report the runtime
The analysis is performed with a python script. You can simply call the runtime_analyzer method from analyzer.py:
```python
from analyzer import runtime_analyzer
```

Then, simply directly use the method in python with your log file:
```python
runtime_analyzer(log_file_path, report_path, plot=False)
```
The report will be saved in `report_path` and you can display the graph directly before saving by setting `plot` to `True`.

You can also directly launch the code by using the `example.py' file.
For instance:

```bash
python example.py -f "logs/mylog.tl" -g "reports/report.png"
```

The report includes two pie charts:
- A full runtime of the total method
- Details of the sub-functions runtimes
