
for f in ~/Videos/*.mp4;
do
#    echo $f
#    echo ${f%.h264}.mp4
	 aws s3 cp $f s3://semyonovtest/Videos/

done
