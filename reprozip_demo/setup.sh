#!/bin/sh

set -e


mkdir /experimentroot; cd /experimentroot
tar zpxf /vagrant/data.tgz --numeric-owner --strip=1 DATA

mkdir -p /experimentroot/dev
mkdir -p /experimentroot/proc

cp /etc/resolv.conf /experimentroot/etc/resolv.conf

cp /vagrant/busybox /experimentroot/busybox
chmod +x /experimentroot/busybox
mkdir -p /experimentroot/bin
[ -e /experimentroot/bin/sh ] || \
    ln -s /busybox /experimentroot/bin/sh
