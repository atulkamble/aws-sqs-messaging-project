```
SNS 

1. ec2 - amazon linux - SG-22 - ssh

2. 

sudo yum update -y 
sudo yum install git python -y 
sudo yum install pip 

git --version 
python --version 
pip --version 
aws --version 


sudo yum update -y
sudo yum groupinstall "Development Tools" -y
sudo yum install openssl-devel bzip2-devel libffi-devel wget tar -y

cd /usr/src
sudo wget https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz
sudo tar xzf Python-3.12.2.tgz
cd Python-3.12.2

sudo ./configure --enable-optimizations
sudo make altinstall
python3.12 --version



3. create user - atul >> group (admin) - FullAdminAccess 

atul >> create access key 

aws configure 

>> enter access key, secret access key, us-east-1, json 

4
 
git clone https://github.com/atulkamble/aws-sqs-messaging-project.git
cd aws-sqs-messaging-project
pip install -r ./requirements.txt

5

// create queue
chmod +x ./create_queue.sh
./create_queue.sh

// send message 
python ./send_message.py

// recieve message 
python ./receive_message.py

// delete message 
python ./delete_message.py

// delete queue 
chmod +x ./delete_queue.sh
./delete_queue.sh

```
