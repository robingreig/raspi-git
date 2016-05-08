#!/bin/bash

cd /tmp

doBackup() {
  cd $1
  echo -n " $2: "
  if [ -f $2.bak ]; then
    echo "Backup of $2 exists, not overwriting"
  else
    mv $2 $2.bak
    mv /tmp/$2 .
    echo "OK"
  fi
}

echo "Setting up Raspberry Pi to make it work with the Gertboard"
echo "and the ATmega chip on-board with the Arduino IDE."
echo ""
echo "Checking ..."

echo -n "  Avrdude: "
if [ ! -f /etc/avrdude.conf ]; then
  echo "Not installed. Please install it first"
  exit 1
fi

fgrep -sq GPIO /etc/avrdude.conf
if [ $? != 0 ]; then
  echo "No GPIO support. Please make sure you install the right version"
  exit 1
fi
echo "OK"

echo -n "  Arduino IDE: "
if [ ! -f /usr/share/arduino/hardware/arduino/programmers.txt ]; then
  echo "Not installed. Please install it first"
  exit 1
fi
echo "OK"

echo "Fetching files:"
for file in boards.txt programmers.txt avrsetup ; do
  echo "  $file"
  rm -f $file
  wget -q http://project-downloads.drogon.net/gertboard/$file
done

echo "Replacing/updating files:"

rm -f /usr/local/bin/avrsetup
mv /tmp/avrsetup /usr/local/bin
chmod 755 /usr/local/bin/avrsetup

cd /etc
echo -n "inittab: "
if [ -f inittab.bak ]; then
  echo "Backup exists: not overwriting"
else
  cp -a inittab inittab.bak
  sed -e 's/^.*AMA0.*$/#\0/' < inittab > /tmp/inittab.$$
  mv /tmp/inittab.$$ inittab
  echo "OK"
fi

cd /boot
echo -n "cmdline.txt: "
if [ -f cmdline.txt.bak ]; then
  echo "Backup exists: not overwriting"
else
  cp -a cmdline.txt cmdline.txt.bak
  cat cmdline.txt					|	\
		sed -e 's/console=ttyAMA0,115200//'	|	\
		sed -e 's/console=tty1//'		|	\
		sed -e 's/kgdboc=ttyAMA0,115200//' > /tmp/cmdline.txt.$$
  mv /tmp/cmdline.txt.$$ cmdline.txt
  echo "OK"
fi

doBackup /usr/share/arduino/hardware/arduino boards.txt
doBackup /usr/share/arduino/hardware/arduino programmers.txt

echo "All Done."
echo "Check and reboot now to apply changes."
exit 0
