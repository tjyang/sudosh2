##############################################################################
# rpm making automation for CentOS/RHEL.

ARCH ?= $(shell arch)
ifeq ($(ARCH),x86_64)
RPM_ARCH := x86_64
else
    ifeq ($(ARCH),i686)
RPM_ARCH := i386
    else
$(error Unknown arch "$(ARCH)".)
    endif
endif

MWD=/tmp


clean:
	@(sudo rm -f ../sudosh2-1.0.6.tgz *.rpm *~ ../*~)

rpm:
	# create sudosh2 tar ball.
	@(cd ..;rm -f sudosh2-1.0.6)
	@(cd ..;ln -s . sudosh2-1.0.6)
	@(cd ..;tar czhf  sudosh2-1.0.6.tgz --exclude sudosh2-1.0.6/sudosh2-1.0.6.tgz --exclude sudosh2-1.0.6/sudosh2-1.0.6  --exclude *~ --exclude .git* sudosh2-1.0.6/)
	@(cd ..;rm -f sudosh2-1.0.6)
	# build the rpm using rpmbuild from ./rmbuild as topdir
	@sudo rm -rf *.rpm ${MWD}/rpmbuild && mkdir -p ${MWD}/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	@cp  ../sudosh2-1.0.6.tgz ${MWD}/rpmbuild/SOURCES/sudosh2-1.0.6.tgz
	@sudo rpmbuild -ba --define "_topdir ${MWD}/rpmbuild"   ../sudosh.spec
	@sudo mv ${MWD}/rpmbuild/RPMS/$(RPM_ARCH)/*.rpm .
	@ls -l *.rpm
