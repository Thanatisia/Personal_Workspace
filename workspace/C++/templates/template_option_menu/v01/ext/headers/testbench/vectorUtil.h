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

    //Vector Modification
    cout << "Type in a number to add: ";
    tmp_str = util.get_user_input();
    if(tmp_str != "")
    {
      try
      {
        tmp = util.convert_string_to_integer(tmp_str);

        cout << "Type in position to insert into: ";
        tmp_str = util.get_user_input();

        if(tmp_str != "")
        {
          try
          {
            position = util.convert_string_to_integer(tmp_str);

            if(position < 0)
            {
              cout << "==========================" << endl;
              cout << "Target position is smaller than 0" << endl;
              cout << "==========================" << endl;
            }
            else if(position >= MAX_SIZE_vec)
            {
              cout << "==========================" << endl;
              cout << "Target position exceeds maximum size of" << " " << "[" << MAX_SIZE_vec << "]" << endl;
              cout << "==========================" << endl;
            }
            else
            {
              vec[position] = tmp;
            }
          }
          catch(exception &ex)
          {
            //cout << "position is not numerical" << endl;
            //fprintf("Error caught [%s] : [%s]", ex.what(), "Position is not numerical");
            cout << "==========================" << endl;
            cout << "Error caught" << " " << "[" << ex.what() << "]" << " " << ":" << " " << "[" << "Position is not numerical" << "]" << endl;
            cout << "==========================" << endl;
            //cout << "Error caught :" << ex.what() << endl;
          }
        }
        else
        {
          cout << "==========================" << endl;
          cout << "Target position to add into the list is empty" << endl;
          cout << "==========================" << endl;
        }
      }
      catch(exception &ex)
      {
        //cout << "position is not numerical" << endl;
        cout << "==========================" << endl;
        cout << "Error caught" << " " << "[" << ex.what() << "]" << " " << ":" << " " << "[" << "Target value to insert is not numerical" << "]" << endl;
        cout << "==========================" << endl;
        //fprintf("Error caught [%s] : [%s]", ex.what(), "Target value to insert is not numerical");
        //cout << endl;
        //cout << "Error caught :" << ex.what() << endl;
      }
    }
    else
    {
      cout << "==========================" << endl;
      cout << "Target number to add into the list is empty" << endl;
      cout << "==========================" << endl;
    }

    //Display all data in vector
    get_vector_elements(vec);


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
  return 0;
}
