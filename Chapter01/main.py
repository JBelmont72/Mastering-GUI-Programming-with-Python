'''


'''
import sys
def main():
    print("Hello, World!")
    print(sys.version)
    print(sys.executable,'executable')## this shows we are in the virtual environment   
    print(sys.platform,'platform')
    print(sys.path,'path\n')
    print(sys.argv,'argv')
    print('''
          ''')
    print(sys.modules,'modules\n')
    print(sys.getdefaultencoding(),'default encoding')
    print(sys.getfilesystemencoding(),'filesystem encoding')
    print(sys.getrecursionlimit(),'recursion limit')
    print(sys.getrefcount(main),'reference count')
    
if __name__ == "__main__":
    main()
    print(sys.exit(0))  # !/usr/bin/env python3

# This is a simple Python script that prints "Hello, World!" and some system information.
# It uses the sys module to access system-specific parameters and functions.
# The script defines a main function that prints the message and system information, and then calls the main function if the script is run as the main module.
# The script also includes a shebang line to specify the Python interpreter to use when running the script.
# The shebang line is a special comment at the top of the script that starts with "#!" and is followed by the path to the Python interpreter.
# The shebang line is used in Unix-like operating systems to indicate which interpreter should be used to run the script.
# The shebang line is not necessary on Windows, but it is a good practice to include it for portability.
# The script also includes a docstring that describes the purpose of the script and its functionality.
# The docstring is a string literal that appears at the beginning of the script and is used to provide documentation for the script.
# The docstring is not executed as part of the script, but it can be accessed using the __doc__ attribute of the module.
# The script also includes a comment that describes the purpose of the script and its functionality.
# The comment is a line that starts with "#" and is ignored by the Python interpreter.
# The comment is used to provide additional information about the script and its functionality.
# The script also includes a print statement that prints the message "Hello, World!" to the console.
# The print statement is a built-in function in Python that outputs the specified message to the console.
# The print statement can take multiple arguments, which are separated by commas.
# The print statement can also take optional keyword arguments, such as sep and end, which specify the separator and end character for the output.
# The script also includes a call to the sys.exit() function, which is used to exit the script with a specified exit status.
# The sys.exit() function takes an optional argument, which is the exit status.
# The exit status is an integer value that indicates the success or failure of the script.
# The exit status is 0 if the script completed successfully, and a non-zero value if the script encountered an error.
# The script also includes a call to the main() function, which is the entry point of the script.
# The main() function is defined at the beginning of the script and contains the main logic of the script.
# The main() function is called if the script is run as the main module, which means that the script is being executed directly and not imported as a module.
# The script also includes a shebang line to specify the Python interpreter to use when running the script.
