#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <string>
#include <list>
#include <vector>
#include <sstream>
#include <stdio.h>
#include <ctype.h>
#include <cstring>
#include "ext/headers/sys.h"
#include "ext/headers/utilities.h"
#include "ext/headers/os.h"
using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::string;
using std::list;
using std::vector;
using std::stringstream;
using std::to_string;
using std::stoi;
using std::isdigit;
using std::exception;

//Setup
utilities util;
sys sysComm;
OSUtil osUtil;

/* Linked List */
struct linked_list
{
  char name[50];
  struct linked_list *next;
} linked_list;
typedef struct linked_list ll;
typedef ll *ll_pointer;

/* Vector functions */
string get_vector_elements(const vector<int>& Vec)
{
  string elements;
  for (size_t i = 0; i < Vec.size(); i++)
  {
    cout<< "Vec["<< i << "] = " << Vec[i]<< endl;
    elements += Vec[i];
  }
  return elements;
}

string convert_char_to_string(char *input_text)
{
  //using stringstream
  string output_text = "";
  stringstream ss;
  ss << input_text;
  output_text = ss.str();
  return output_text;
}

//int main(int argc, char const *argv[])
int main(int argc, char **argv)
{
  /* Define : Ending option*/
#ifndef OPTION_END
  #define OPTION_END 5
#endif

  int valid_type = 0; /* For checking if a intended type is valid */
  int position = 0; //Index of vector
  int tmp = 0; //Temporary integer container for user input converted to integer
  string tmp_str = ""; //Temporary string container for user input
  int exit_token = 0;

  int MAX_SIZE_vec = 20;
  std::vector<int> vec(MAX_SIZE_vec);
  // if(argc == 3)
  // {
  //
  // }
  // else
  // {
  //   cout << "No Param: " << endl;
  //   vec[0] = 20;
  //   vec[1] = 40;
  //   vec[2] = 60;
  // }
  cout << "Param Size: " << util.convert_int_to_string(argc) << endl;
  for(int i=1; i < argc; i++)
  {
    vec[i-1] = util.convert_string_to_integer(argv[i]);
  }

  while(exit_token != 1) //While user does not confirm exit
  {
    osUtil.run_sys_command("cls");
    /* code */
    //Start
    cout << "=================" << endl;
    cout << "Link Start" << endl;
    cout << "=================" << endl;

    //Body
    string command_compilation = osUtil.collect_commands({"cls", "dir", "cd"});

    cout << "Hello World" << endl;

    //Test here
    cout << "Please select an option (Type) :" << endl;
    cout << "1. " << "Testbench 1" << endl <<
            "2. " << "Testbench 2" << endl <<
            "3. " << "Testbench 3" << endl <<
            "4. " << "Help" << endl <<
            "5. " << "Exit" << endl;
    getline(cin, tmp_str);
    try
    {
      tmp = util.convert_string_to_integer(tmp_str);

      if(tmp != 1 && tmp != 2 && tmp != 3 && tmp != 4 && tmp != OPTION_END)
      {
        //End
        cout << "=================" << endl;
        cout << "Program ending..." << endl;
        cout << "================" << endl;
        exit_token = util.finish();
        if(exit_token == 1)
        {
          osUtil.run_sys_command("cls");
          break;
        }
      }
      else
      {
        osUtil.run_sys_command("cls");
        cout << "==============================" << endl;
        switch (tmp)
        {
          case 1:
            cout << "Testbench 1" << endl;
            cout << "This is TestingBench Room Number 1, Codes to be display here - This is a placeholder text" << endl;
            break;
          case 2:
            cout << "Testbench 2" << endl;
            cout << "This is TestingBench Room Number 2, Codes to be display here - This is a placeholder text" << endl;
            break;
          case 3:
            cout << "Testbench 3" << endl;
            cout << "This is TestingBench Room Number 3, Codes to be display here - This is a placeholder text" << endl;
            break;
          case 4:
            cout << "Help:" << endl;
            cout << "Summary: Please type a number for the appropriate Option you wish to choose." << endl;
            break;
          case OPTION_END:
            exit_token = 1;
            cout << "Program closed" << endl;
            break;
        }
        cout << "==============================" << endl;
        getline(cin, tmp_str);
      }
    }
    catch(exception &ex)
    {
      cout << "==========================" << endl;
      cout << "Error caught" << " " << "[" << ex.what() << "]" << " " << ":" << " " << "[" << "Target option is not numerical" << "]" << endl;
      cout << "==========================" << endl;
      getline(cin, tmp_str);
    }
  }
  return 0;
}
