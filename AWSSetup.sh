#!/bin/bash

read -p 'Username: ' uservar
read -sp 'Password' passvar
echo
echo Your username $uservar will be sent to the server to be created.

aws iam create-user --user-name $uservar
aws iam get-user --user-name $uservar > $uservar.json
aws iam create-access-key --user-name $uservar
aws s3api create-bucket --bucket semyonov$uservar
aws s3 cp $uservar.json s3://semyonov$uservar
