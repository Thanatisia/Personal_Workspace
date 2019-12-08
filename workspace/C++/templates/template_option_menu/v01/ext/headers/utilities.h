#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <string>
#include <list>
#include <vector>
#include <sstream>
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

class utilities
{
private:
public:
  //Constructor
  utilities()
  {
    cout << "utilities library imported" << endl;
  }
  //Deconstructor
  ~utilities()
  {
    cout << "utilities library deconstructed" << endl;
  }
  string get_user_input()
  {
    string tmp = "";
    getline(cin, tmp);
    return tmp;
  }

  int finish()
  {
    int token = 0;
    string tmp = "";
    cout << "Press 'c' to confirm exit:" << " " << endl;
    getline(cin, tmp);
    if(strstr(tmp.c_str(), "c")) //Present
    {
      token = 1;
    }
    else
    {
      token = 0;
    }
    return token;
  }

  /* Polymorphism - conversion */
  int convert_string_to_integer(string str_text)
  {
    int out_num = 0;
    out_num = stoi(str_text);
    return out_num;
  }

  string convert_int_to_string(int in_num)
  {
    string out_text = "";
    out_text = to_string(in_num);
    return out_text;
  }

  string connect_vector_to_string(string connector, vector<string> dataset)
  {
    string compilation = "";
    int vector_size = 0;

    vector_size = dataset.size();
    int i = 0;

    while(i != vector_size)
    {
      compilation += dataset[i];
      if(i != vector_size-1)
      {
        compilation += " " + connector + " ";
      }
      i++;
    }

    return compilation;
  }
};
