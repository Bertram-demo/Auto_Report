sudo apt-get install libxss1 libappindicator1 libindicator7

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome*.deb

sudo apt-get install -f

sudo apt-get install xvfb

sudo apt-get install unzip

wget -N http://npm.taobao.org/mirrors/chromedriver/88.0.4324.27/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

sudo mv -f chromedriver /usr/local/share/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

# sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

