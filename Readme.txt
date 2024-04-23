

Calc.py file >>> do the basic maths. - adding and multiplication

test.py >>> is unit to unit test the calc.py


Jenkins file has 3 stages
1) Checkout: checkout of the git repo
2) Build: git branch and build or run the calc.py file
3) Testing: Execute the test.py for unit testing. with command $python -m unittest -v test.py


Jenkins server should have git and python 

