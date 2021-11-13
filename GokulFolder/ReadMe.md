Using the parser:
Download antlr from here, export all environment variables from here.

https://www.antlr.org/

To generate python tree traversers:
antlr4 -Dlanguage=Python3 -visitor  eqSolver.g4

To generate java (with gui) traversers:
antlr4 eqSolver.g4
javac eqSolver*.java
grun eqSolver program input.txt -gui

To generate user classes to inherit to python, we need antlr4-python3 libraries:
https://pypi.org/project/antlr4-python3-runtime/

