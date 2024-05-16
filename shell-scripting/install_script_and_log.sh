package=htop

date >> apt_install_history.log

sudo apt install $package >> apt_install_history.log

if [ $? -eq 0 ]
then
  echo "The installation of $package was successful"
  echo "The new command is available here:"
  which $package
else
  echo "$package failed to install"
fi
