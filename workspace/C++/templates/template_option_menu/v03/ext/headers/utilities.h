#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <string>
#include <list>
#include <vector>
#include <sstream>
#include <typeinfo> /* For Type Information */
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
  string get_user_input(string pointer_icon="")
  {
    string tmp = "";
    cout << pointer_icon;
    getline(cin, tmp);
    return tmp;
  }

  int finish(string pointer_icon="")
  {
    int token = 0;
    string tmp = "";
    cout << "Press 'c' to confirm exit:" << " " << endl;
    cout << pointer_icon;
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

  template<typename T> /* Awesome declaration for variable-type variables */
  bool validate_proper_type(string target_type, T uInput)
  {
    /*
      target_type : What type is the correct type you want to check for
      uInput: Your variable
    */
    bool validator_token = false;
    string variable_type = "";

    variable_type = typeid(uInput).name();

    cout << "TypeID:" << variable_type << endl;

    if(variable_type != "string" && variable_type != "int" && variable_type != "float" && variable_type != "char")
    {
      cout << "Invalid Type" << endl <<
              "Supported types include:" << endl <<
              "1. 'string' for string" << endl <<
              "2. 'int' for Integer" << endl <<
              "3. 'float' for Float" << endl <<
              "4. 'char' for Character" << endl;
    }
    else
    {
      if(variable_type == target_type)
      {
        validator_token = true;
      }
    }
    return validator_token;
  }
};
