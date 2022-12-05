#!/bin/bash

if [ -d $1 ]
then
   cp -p dayxx-y.py $1/day${1}-1.py
   cp -p dayxx-y.py $1/day${1}-2.py

   cd $1

   ../fetch-input
fi
