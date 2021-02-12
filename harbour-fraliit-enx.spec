Name:          harbour-fraliit-enx
Version:       0.3.0
Release:       3
Summary:       EnglishX
Obsoletes:     english-arw englishx harbour-englishx
Conflicts:      english-arw englishx harbour-englishx
Requires:      sailfish-version >= 2.1.0, harbour-fraliit-common >= 0.1.0-1
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3

%description
English keyboard with arrows and numbers.

%files
/usr/share/maliit/plugins/com/jolla/layouts/enx.conf
/usr/share/maliit/plugins/com/jolla/layouts/enx.qml
/usr/share/maliit/plugins/com/jolla/layouts/enx_arw.conf
/usr/share/maliit/plugins/com/jolla/layouts/enx_arw.qml
/usr/share/maliit/plugins/com/jolla/layouts/enx_123.conf
/usr/share/maliit/plugins/com/jolla/layouts/enx_123.qml

%post
systemctl-user restart maliit-server.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm /usr/share/maliit/plugins/com/jolla/layouts/enx.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/enx.qml
rm /usr/share/maliit/plugins/com/jolla/layouts/enx_arw.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/enx_arw.qml
rm /usr/share/maliit/plugins/com/jolla/layouts/enx_123.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/enx_123.qml
systemctl-user restart maliit-server.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
systemctl-user restart maliit-server.service
fi
fi

%changelog
* Sat Jun 9 2018 0.3.0-1
- Uses fraliit-common.

* Sat Oct 22 2016 0.2.0
- english-arw and englishx packages merged.

* Thu Sep 15 2015 0.1
- First build.
