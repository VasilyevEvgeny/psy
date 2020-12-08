# Psycological 

## Usage

The program is supposed to be used under the OS Windows

There are 2 ways to run the program:
* Create virtual environment **.venv**, install libs: **pandas**, **numpy==1.19.3**, **openpyxl**. 
Then run `python main.py` or execute `run.bat`
* Make **.exe**-file using lib **pyinstaller**
    * Install pyinstaller: `pip install pyinstaller`
    * Run command: 
   
   ```pyinstaller.exe --windowed --onefile --icon=icon.ico main.py```
   
   The resulting file will weigh several hundred MB and run for about a minute.