#!/bin/sh

for file in $(find . -maxdepth 3 -iname '[0-9]*' -type d -exec test -e '{}'/Makefile \; -print)
do
  make -C "$file";
done
