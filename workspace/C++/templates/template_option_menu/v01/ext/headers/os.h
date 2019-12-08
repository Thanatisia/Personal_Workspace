#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <string>
#include <list>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cstdarg> /* C standard argument library */
using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::string;
using std::list;
using std::vector;
using std::stringstream;
using std::find;  //std::find returns an iterator to the first occurrence of x, or an iterator to one-past the end of the range if x is not found.
using std::begin; //Starting index of a iterator - list, array etc.
using std::end; //Last index of a iterator - list, array etc.

class OSUtil
{
private:
public:
  //Constructor
  OSUtil()
  {
    cout << "OS library imported" << endl;
  }
  //Deconstructor
  ~OSUtil()
  {
    cout << "OS library deconstructed" << endl;
  }

  string getOsName()
  {
    #ifdef _WIN32
    return "Windows 32-bit";
    #elif _WIN64
    return "Windows 64-bit";
    #elif __APPLE__ || __MACH__
    return "Mac OSX";
    #elif __linux__
    return "Linux";
    #elif __FreeBSD__
    return "FreeBSD";
    #elif __unix || __unix__
    return "Unix";
    #else
    return "Other";
    #endif
  }


  vector<string> window_commands{
    "cls",
    "dir",
    "pause"
  };

  int window_commands_size = window_commands.size();

  vector<string> linux_commands{
    "clear",
    "ls",
    "pause"
  };

  int linux_commands_size = linux_commands.size();

  string collect_commands(vector<string> command_set)
  {
    string command_compilation = "";
    int vector_size = 0;

    vector_size = command_set.size();
    int i = 0;

    while(i != vector_size)
    {
      command_compilation += command_set[i];
      if(i != vector_size-1)
      {
        command_compilation += " && ";
      }
      i++;
    }

    return command_compilation;
  }

  void run_sys_command(string command, bool multi_command=false)
  {
    string os_name = "";
    string os_version = "";

    int position = 0;
    bool search_token = false;

    const char *sys_command_formatted = command.c_str();
    #ifdef _WIN32
      os_name = "Windows";
      os_version = "32-bit";
      if(!multi_command)
      {
        if(find(window_commands.begin(), window_commands.end(), command) != window_commands.end())
        {
          system(sys_command_formatted);
        }
        else
        {
          cout << "Invalid command" << endl;
        }
      }
      else
      {
        system(sys_command_formatted);
      }
      cout << os_name << " " << os_version << endl;
    #elif _WIN64
      os_name = "Windows";
      os_version = "64-bit";

      if(!multi_command)
      {
        if(find(window_commands.begin(), window_commands.end(), command) != window_commands.end())
        {
          system(sys_command_formatted);
        }
        else
        {
          cout << "Invalid command" << endl;
        }
      }
      else
      {
        system(sys_command_formatted);
      }
    #elif __APPLE__ || __MACH__
      os_name = "Mac OSX";
      os_version = "64-bit";
    #elif __linux__
      os_name = "Linux";
      os_version = "Base"

      if(!multi_command)
      {
        if(find(linux_commands.begin(), linux_commands.end(), command) != linux_commands.end())
        {
          system(sys_command_formatted);
        }
        else
        {
          cout << "Invalid command" << endl;
        }
      }
      else
      {
        system(sys_command_formatted);
      }
    #elif __FreeBSD__
      os_name = "Unix";
      os_version = "FreeBSD";
    #elif __unix || __unix__
      os_name = "Unix";
      os_version = "Base"
    #else
      //Invalid
      os_name = "Other"
      os_version = "None";
    #endif
    // if(os == "windows")
    // {
    //
    // }
    // else if(os == "linux")
    // {
    //   if(version == "ubuntu")
    //   {
    //
    //   }
    //   else if(version == "arch")
    //   {
    //
    //   }
    //   else if(version == "debian")
    //   {
    //
    //   }
    //   else if(version == "fedora")
    //   {
    //
    //   }
    //   else
    //   {
    //     /* Invalid version
    //       i.e.
    //         1. Linux Ubuntu
    //         2. Linux Debian
    //         3. Arch Linux
    //         4. Linux fedora
    //     */
    //   }
    // }
  }
};
