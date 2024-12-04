import pkg_resources, subprocess, sys

print(f"""
This script will install all dependencies for the following scripts in the readership data workflow.
      
      Press Enter to continue.
      """)
input()

# check which packages are missing
print()
print("Checking required packages for script to run.")
required  = {'jellyfish','selenium', 'openpyxl', 'pandas'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

# install the missing packages
print()
print("Installing missing packages.")
if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

print()
print("Packages installed. System ready to start readership data process.")
print()
input("Script finished. \nPress enter to close.")