#!/bin/bash

# Provide the directory you want to use as an argument to this command - otherwise, the current folder will be used.

DIRECTORY=""

if [ $# -eq 0 ]
then
        DIRECTORY=$(pwd)
else
        DIRECTORY=$1
fi

FILES=$(ls -1 ${DIRECTORY})

for FILE in ${FILES}
do
        i=${DIRECTORY}/${FILE}

        CS=$(md5sum ${i} | awk '{ print $1 }')

        OUTPUT+=${CS}": "

        STAT=`stat --format=%a ${i} | grep -E "[237]$"`

        if (( ${STAT} -ne "" ))
        then
                OUTPUT+="WARNING: FILE IS WORLD WRITABLE: "
        fi

        OUTPUT+=${i}
 
        echo ${OUTPUT}

        OUTPUT=""
done
