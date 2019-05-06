mkdir ~/download
sudo apt -y update

sudo apt -y install build-essential checkinstall
sudo apt -y install libreadline-gplv2-dev libncursesw5-dev

sudo apt -y install libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz

tar xvf Python-3.7.3.tar.xz
cd Python-3.7.3/
./configure
sudo make altinstall

