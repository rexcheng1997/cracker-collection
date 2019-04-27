## Zip File Cracker

Password cracker for password-protected zipped files. ([ver. 1.0.0-1](#zip-file-cracker))

#### Requirements:

* Ubuntu 18.04
* Python 3
* dpkg
* debhelper
* gdebi

#### Building and Installation:

1. To install the cracker, zcracker package, on your machine, first clone the repo by running `git clone link/to/this/repo` in your terminal.

2. Change to the directory just cloned by running `cd zip-cracker`. Next, from that directory, run the following command to build the package:

    `$ dpkg-buildpackage -b`

    **Note: root permission needed.**

    *Further issues about building failure will be listed here.*

    After successfully building the package, you should see some `.deb`, `.changes`, and `.buildinfo` files in the *parent* directory. (Don't change directory at this time!)

3. Then run the following command to install the built package:

    `$ sudo gdebi -n ../zcracker_1.0.0-1_all.deb`

    Up to now, zcracker should be successfully installed on your machine.

#### Usage & Examples:

For usage, run `zcracker -h` for more information.

*Examples will be listed here.*
