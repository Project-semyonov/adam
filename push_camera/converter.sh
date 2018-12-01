#!/bin/sh

for f in ~/Videos/*.h264;
do
if [ ! -f "${f%.h264}.mp4" ] 
then
#    echo $f
#    echo ${f%.h264}.mp4
    MP4Box -add $f ${f%.h264}.mp4
fi
done
