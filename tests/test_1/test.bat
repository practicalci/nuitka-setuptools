mkdir build
cd build
cmake ../package1/subpackage3/swigpkg

if not %errorlevel%==0 exit /b 1

make all

if not %errorlevel%==0 exit /b 1

cd ..
pip install .

if not %errorlevel%==0 exit /b 1

python main.py

if not %errorlevel%==0 exit /b 1

