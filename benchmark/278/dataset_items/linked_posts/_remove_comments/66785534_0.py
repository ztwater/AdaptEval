import pyparsing

test = """
/* Code my code
xx to remove comments in C++
or C or python */

include <iostream> // Some comment

int main (){
    cout << "hello world" << std::endl; // comment
}
"""
commentFilter = pyparsing.cppStyleComment.suppress()
# To filter python style comment, use
# commentFilter = pyparsing.pythonStyleComment.suppress()
# To filter C style comment, use
# commentFilter = pyparsing.cStyleComment.suppress()

newtest = commentFilter.transformString(test)
print(newest)
