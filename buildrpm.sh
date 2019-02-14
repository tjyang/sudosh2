#!/bin/bash
#Make sure your rpmbuild environment is ready.
./configure
cd contrib
make rpm
