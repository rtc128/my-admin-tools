R = $(shell cat RELEASE)

rpm:
	mkdir -p ~/rpmbuild/BUILDROOT
	mkdir -p ~/rpmbuild/SOURCES
	mkdir -p ~/rpmbuild/SPECS
	rm -fr /tmp/my-admin-tools-$(R)
	cp -a . /tmp/my-admin-tools-$(R)
	tar -C /tmp -c -z -f /tmp/my-admin-tools.tar.gz my-admin-tools-$(R)
	mv /tmp/my-admin-tools.tar.gz ~/rpmbuild/SOURCES
	cp my-admin-tools.spec ~/rpmbuild/SPECS
	rpmbuild --define "_target_os linux" -bb ~/rpmbuild/SPECS/my-admin-tools.spec
	mkdir -p ~/rpm
	rm -fr ~/rpm/*
	mv ~/rpmbuild/RPMS/noarch/*.rpm ~/rpm
	rm -fr /tmp/my-admin-tools-$(R)
