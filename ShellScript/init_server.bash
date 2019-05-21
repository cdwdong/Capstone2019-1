sudo add-apt-repository ppa:ubuntu-ko
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update
sudo apt-get install build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev
sudo apt-get install python3-pip python3.7-dev
sudo apt-get install python3.7

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2

sudo update-alternatives --config python3