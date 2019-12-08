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

class sys
{
private:
public:
  sys()
  {
    cout << "sys library imported" << endl;
  }
  ~sys()
  {
    cout << "sys library deconstructed" << endl;
  }
};
