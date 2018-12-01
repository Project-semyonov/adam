#!/bin/sh

for f in ~/Videos/*.h264;
do
if [ ! -f "${f%.h264}.mp4" ]
then
#    echo $f
#    echo ${f%.h264}.mp4
    ffmpeg -i $f -c copy ${f%.h264}.mp4
fi
done
