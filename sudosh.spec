#	$Id: sudosh.spec,v 1.2 2010/07/09 20:05:53 squash Exp $
#
%define origname sudosh2
%define name sudosh2
%define version 1.0.6
%define release 2.el5

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Logged root shell that can be used for auditing

Group: System/SDL-custom
License: OSL
URL: https://github.com/tjyang/sudosh2
Source: http://sudosh2.sourceforge.net/sudosh2-%{version}.tgz

Packager: John Barton <jbarton@technicalworks.net>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# BuildArch: i386
Requires: sudo
Provides: %{origname} = %{version}-%{release}, %{name} = %{version}-%{release}

%description
sudosh2 works directly with sudo to provide a fully functional shell that
users may use to obtain full root access. Unlike providing a team of system
administrators full root access through sudo, it guarantees that detailed
logs are kept. It uses the script command in conjunction with a secure FIFO
and comes with a utility to view sessions and drill down deeper and see the
actual session output. 

%prep
%setup -q -n %{origname}-%{version}

%{__cat} <<EOF >sudosh.conf.tmp
# sudosh Configuration File
logdir                  = /var/log/sudosh
default shell           = /bin/bash
delimiter               = -
syslog.priority         = LOG_NOTICE
syslog.facility         = LOG_DAEMON

# Allow sudosh to execute -c arguements?  If so, what?
-c arg allow = scp
-c arg allow = sftp
-c arg allow = /usr/libexec/openssh/sftp-server
-c arg allow = rsync

# or comment out above -c lines
# use following setting to allow all commands.
-c arg allow = *
EOF

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}/var/log/sudosh
install -m 0744 sudosh.conf.tmp %{buildroot}/etc/sudosh.conf

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/sudosh.1*
%doc %{_mandir}/man5/sudosh.conf*
%doc %{_mandir}/man8/sudosh-replay.8*
%{_bindir}/sudosh
%{_bindir}/sudosh-replay
%config(noreplace) %{_sysconfdir}/sudosh.conf
%dir %attr(0733 root root) /var/log/sudosh

%changelog
* Mon Feb 11 2019 - 1.0.6-2 tjyang2001@gmail.com
* Wed Apr 29 2015 - 1.0.6
- Version bumped to 1.0.6
* Fri Jul 09 2010 John Barton <jbarton@technicalworks.net> - 1.0.4-1
- Update for version 1.0.4



%pre
# https://stackoverflow.com/questions/18967389/rpm-post-scriptlet-best-practice
# https://www.golinuxhub.com/2018/05/how-to-execute-script-at-pre-post-preun-postun-spec-file-rpm.html
#1.%pre of new package  
#      (package install)
#2.%post of new package
#
#3.%preun of old package
#        (removal of old package)
#4.%postun of old package

if [ $1 == 1 ];then
    echo "-----------------------"
    echo "RPM is getting installed"
    echo "Put your script here"
    echo "-----------------------"
elif [ $1 == 2 ];then
    echo "-----------------------"
    echo "RPM is getting upgraded"
    echo "Put your script here"
    echo "-----------------------"
fi
#if [ "$1" = "2" ]; then
#  #Perform maintenance tasks before server upgrade begins.
#  #Determine if server is running, stops it.
#  /etc/init.d/postgres-9.1-openscg status &> /dev/null
#  if [ "$?" = "0" ];
#  then
#   /etc/init.d/postgres-9.1-openscg stop
#   touch /tmp/pg_9.1.stopped
#  fi
#fi


%post

if [ $1 == 1 ];then
    echo "-----------------------"
    echo "RPM is getting installed"
    echo "Put your script here"
    echo "-----------------------"
elif [ $1 == 2 ];then
    echo "-----------------------"
    echo "RPM is getting upgraded"
    echo "Put your script here"
    echo "-----------------------"
fi

#if type "/usr/bin/chcon" &> /dev/null ; then
#  /usr/bin/chcon -t textrel_shlib_t $RPM_INSTALL_PREFIX/lib/libedit.so &> /dev/null 
#fi
#
##Create a soft link to init script
#if [ ! -f /etc/init.d/postgres-9.1-openscg ]
#then
#  ln -s $RPM_INSTALL_PREFIX/bin/postgres-9.1-openscg /etc/init.d/postgres-9.1-openscg
#fi
#

%preun

if [ $1 == 1 ];then
    echo "-----------------------"
    echo "RPM is getting upgraded"
    echo "Put your script here which will be called when this rpm is removed"
    echo "-----------------------"
elif [ $1 == 0 ];then
    echo "--------------------"
    echo "RPM is getting removed/uninstalled"
    echo "Put your script here which will be called before uninstallation of this rpm"
    echo "--------------------"
fi


#if [ "$1" = "0" ]; then
#  #Action is uninstallation, not called due to upgrade of a new package
#
#  #Determine if server is running, stops it.
#  /etc/init.d/postgres-9.1-openscg status &> /dev/null
#  if [ "$?" = "0" ];
#  then
#   echo "Attempting to stop server..."
#   /etc/init.d/postgres-9.1-openscg stop
#  fi
#
#  echo "Attempting to update server startup status..." 
#  if type "/sbin/chkconfig" &> /dev/null ; then
#   /sbin/chkconfig --del postgres-9.1-openscg 
#  fi
#fi

%postun
if [ $1 == 1 ];then
    echo "-----------------------"
    echo "RPM is getting upgraded"
    echo "Put your script here which will be called when this rpm is removed"
    echo "-----------------------"
elif [ $1 == 0 ];then
    echo "--------------------"
    echo "RPM is getting removed/uninstalled"
    echo "Put your script here which will be called after uninstallation of this rpm"
    echo "--------------------"
fi

#if [ "$1" = "0" ]; then
#  #Action is uninstallation, not called due to upgrade of a new package
#  rm /etc/init.d/postgres-9.1-openscg
#  echo "Uninstallation complete."
#fi


