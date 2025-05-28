Name:           my-admin-tools
Version:			 1.0.4
Release:        1
Summary:        Administration tools for MySQL

BuildArch:      noarch
License:			 GPL
Source0:			 my-admin-tools.tar.gz

%description
Administration tools for MySQL:
- Analyze all tables: my-analyze-all-tables
- Drop all schemas: my-drop-all-schemas
- Drop all tables: my-drop-all-tables
- Drop all triggers: my-drop-all-trigger
- Drop all users: my-drop-all-users
- Kill blocking sessions: my-kill-blockers
- Kill sessions: my-kill-sessions
- Mirror a database (copy objects/schemas): my-mirror
- Truncate all tables: my-truncate-all-tables

%prep
%setup -q
%build
%install
install -d -m 0755 $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-analyze-all-tables $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-compare-count $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-compare-data $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-schemas $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-tables $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-users $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-triggers $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-flush-all-tables $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-kill-blockers $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-kill-long-transactions $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-kill-sessions $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-mirror $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-repl-skip-failed-transaction $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-replace-table $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-truncate-all-tables $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-unlock-users $RPM_BUILD_ROOT/usr/bin


%files
/usr/bin/my-analyze-all-tables
/usr/bin/my-compare-count
/usr/bin/my-compare-data
/usr/bin/my-drop-all-schemas
/usr/bin/my-drop-all-tables
/usr/bin/my-drop-all-users
/usr/bin/my-drop-all-triggers
/usr/bin/my-flush-all-tables
/usr/bin/my-kill-blockers
/usr/bin/my-kill-long-transactions
/usr/bin/my-kill-sessions
/usr/bin/my-mirror
/usr/bin/my-repl-skip-failed-transaction
/usr/bin/my-replace-table
/usr/bin/my-truncate-all-tables
/usr/bin/my-unlock-users

%changelog

* Wed May 28 2025 Rodrigo Tassinari 1.0.4
- New try to fix target OS in RPM

* Wed May 28 2025 Rodrigo Tassinari 1.0.3
- Fix in RPM package (file list)

* Wed May 28 2025 Rodrigo Tassinari 1.0.2
- my-kill-blockers: added options to choose a specific type of lock

* Mon May 26 2025 Rodrigo Tassinari 1.0.1
- my-kill-sessions: fix in command line parsing

* Wed May 7 2025 Rodrigo Tassinari 1.0.0
- Initial release
