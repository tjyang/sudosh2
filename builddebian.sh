#!/bin/bash
#Make sure your Debian build environment is ready.
./configure
sudo debuild -b -uc -us
ls -l ../sudo*.deb
