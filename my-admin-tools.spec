Name:           my-admin-tools
Version:			 1.1.2
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
install -m 0755 src/my-get-digest $RPM_BUILD_ROOT/usr/bin
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
/usr/bin/my-get-digest
/usr/bin/my-kill-blockers
/usr/bin/my-kill-long-transactions
/usr/bin/my-kill-sessions
/usr/bin/my-mirror
/usr/bin/my-repl-skip-failed-transaction
/usr/bin/my-replace-table
/usr/bin/my-truncate-all-tables
/usr/bin/my-unlock-users

%changelog

* Thu Jul 10 2025 Rodrigo Tassinari 1.1.2
- my-kill-blockers: fix in single execution (-n 1): a bug in timestamp calculation was preventing execution

* Mon Jul 7 2025 Rodrigo Tassinari 1.1.1
- my-kill-blockers: Log fully-qualified table name
- my-mirror: Minor fix in SLEEP call

* Mon Jun 23 2025 Rodrigo Tassinari 1.1.0
- New tool: my-dump-triggers

* Thu Jun 12 2025 Rodrigo Tassinari 1.0.9
- my-kill-blockers: better timeouts and error logging

* Wed Jun 11 2025 Rodrigo Tassinari 1.0.8
- my-mirror: before first table for each thread, wait a little, to avoid deadlock

* Tue Jun 10 2025 Rodrigo Tassinari 1.0.7
- my-mirror: when retrying to copy a table, use the same command, because in first attempt, it's not surely created

* Tue Jun 03 2025 Rodrigo Tassinari 1.0.6
- my-kill-blockers: support for active session count filtering

* Tue Jun 03 2025 Rodrigo Tassinari 1.0.5
- New tool: my-get-digest

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
