# Cracker Collection
Collection of password crackers for various file types

## Table of Contents

* [Zip file cracker](#zip-file-cracker)
* [More to be added...](#table-of-contents)

---

## Zip File Cracker

Password cracker for password-protected zipped files. ([ver. 2.0.0-1](#zip-file-cracker))

#### Requirements:

* Ubuntu 18.04
* Python 3
* dpkg
* debhelper
* gdebi

#### Building and Installation:

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

#### Running from Source:

See **README.md** in *zip-cracker* folder for details.

#### Usage & Examples:

For usage, run `zcracker -h` for more information. If you only see `Finished.` printed on the screen, this means that the program terminates without finding the correct password in the user-specified range.

*Examples* see **README.md** in *zip-cracker* folder.
