## Zip File Cracker

Password cracker for password-protected zipped files. ([ver. 2.0.0-1](#zip-file-cracker))

### Requirements:

* Ubuntu 18.04
* Python 3
* dpkg
* debhelper
* gdebi

### Building and Installation:

1. To install the cracker, zcracker package, on your machine, first clone the repo by running `git clone link/to/this/repo` in your terminal.

2. Change to the directory just cloned by running `cd zip-cracker`.  
   Next, from that directory, run the following command to build the package:  
   `$ dpkg-buildpackage -b`  
   **Note: root permission needed.**

   *Further issues about building failure will be listed here.*

   After successfully building the package, you should see some `.deb`, `.changes`, and `.buildinfo` files in the *parent* directory. (Don't change directory at this time!)

3. Then run the following command to install the built package:  
   `$ sudo gdebi -n ../zcracker_2.0.0-1_all.deb`  
   Up to now, zcracker should be successfully installed on your machine.

### Running from Source:

1. Go to *zip-cracker* folder by running `cd zip-cracker`.

2. Run the following command in the terminal for detailed usage for *driver.py*:  
   `$ python3 driver.py -h`

### Usage & Examples:

For usage, run `zcracker -h` for more information. If you only see `Finished.` printed on the screen, this means that the program terminates without finding the correct password in the user-specified range.

#### Examples:

**Note**: *If running from source, simply replace* `zcracker` *with* `python3 driver.py`. By default, the program will automatically unzip the file if the correct password is found.  
**Format of password list**: One password per line (i.e. separate passwords with a new line character).

1. Cracking using passwords of length 3 with combination of lower-case English letters (a-z) and digits (0-9), no forcing (i.e. not using all computation resources), and printing the password to stdout (i.e. on the screen):  
   `$ zcracker filename.zip 3 -l -d -p`

2. Cracking using passwords of length 5 with combination of upper-case English letters (A-Z) and special characters (!@#$%^&\*), forcing, and writing the password to default output file (i.e. pwd.txt):  
   `$ zcracker filename.zip 5 -u -s -f`

3. Cracking using user-specified password list, forcing, and printing the password to stdout:  
   `$ zcracker filename.zip 2 -w wordlist.txt -f -p`  
   **Note**: You need to specify the length of the passwords though it is just used to occupy the argument and has nothing to do with the length of passwords in the list.

*Order of all the flags and arguments doesn't matter in the examples above.*
