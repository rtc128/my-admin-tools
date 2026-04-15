Name:           my-admin-tools
Version:			 1.5.3
Release:        1
Summary:        Administration tools for MySQL

BuildArch:      noarch
License:			 GPL
Source0:			 my-admin-tools.tar.gz

%description
Administration tools for MySQL:
- Analyze all tables: my-analyze-all-tables
- Compare databases: my-db-compare
- Drop all constraints: my-drop-all-constraints
- Drop all events: my-drop-all-events
- Drop all indexes: my-drop-all-indexes
- Drop all primary keys: my-drop-all-pks
- Drop all routines: my-drop-all-routines
- Drop all schemas: my-drop-all-schemas
- Drop all tables: my-drop-all-tables
- Drop all triggers: my-drop-all-trigger
- Drop all users: my-drop-all-users
- Kill blocking sessions: my-kill-blockers
- Kill sessions: my-kill-sessions
- Mirror a database (copy objects/schemas): my-mirror
- Truncate all tables: my-truncate-all-tables
- Validate a replica created with my-mirror: my-val-mirror

%prep
%setup -q
%build
%install
install -d -m 0755 $RPM_BUILD_ROOT/usr/bin
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/man/man1
install -m 0755 src/my-analyze-all-tables $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-compare-count $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-compare-data $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-db-compare $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-constraints $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-events $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-indexes $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-pks $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-routines $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-schemas $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-tables $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-users $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-drop-all-triggers $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-fix-definer-events $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-fix-definer-routines $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-fix-definer-triggers $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-fix-definer-views $RPM_BUILD_ROOT/usr/bin
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
install -m 0755 src/my-update-dirty-stats $RPM_BUILD_ROOT/usr/bin
install -m 0755 src/my-val-mirror $RPM_BUILD_ROOT/usr/bin
install -m 0644 my-kill-blockers.1.gz $RPM_BUILD_ROOT/usr/share/man/man1
install -m 0644 my-mirror.1.gz $RPM_BUILD_ROOT/usr/share/man/man1

%files
/usr/share/man/man1/my-kill-blockers.1.gz
/usr/share/man/man1/my-mirror.1.gz
/usr/bin/my-analyze-all-tables
/usr/bin/my-compare-count
/usr/bin/my-compare-data
/usr/bin/my-db-compare
/usr/bin/my-drop-all-constraints
/usr/bin/my-drop-all-events
/usr/bin/my-drop-all-indexes
/usr/bin/my-drop-all-pks
/usr/bin/my-drop-all-routines
/usr/bin/my-drop-all-schemas
/usr/bin/my-drop-all-tables
/usr/bin/my-drop-all-users
/usr/bin/my-drop-all-triggers
/usr/bin/my-fix-definer-events
/usr/bin/my-fix-definer-routines
/usr/bin/my-fix-definer-triggers
/usr/bin/my-fix-definer-views
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
/usr/bin/my-update-dirty-stats
/usr/bin/my-val-mirror

%changelog

* Wed Apr 15 2026 Rodrigo Tassinari 1.5.3
- my-mirror: Allow unit definitions in partition size limit

* Fri Apr 10 2026 Rodrigo Tassinari 1.5.2
- my-kill-blockers: Added support for AWS RDS.
- New tool: my-update-dirty-stats

* Tue Apr 7 2026 Rodrigo Tassinari 1.5.1
my-mirror: Use work dir for temp files, instead of /tmp.
my-mirror: Create indexes and constraints using multi-thread.

* Tue Mar 31 2026 Rodrigo Tassinari 1.5.0
- New tool: my-drop-all-constraints
- New tool: my-drop-all-indexes
- New tool: my-drop-all-pks

* Thu Mar 26 2026 Rodrigo Tassinari 1.4.14
- my-mirror: create indexes using multithread
- my-db-comapre: don't stop when a diff is found

* Wed Mar 25 2026 Rodrigo Tassinari 1.4.13
- my-mirror: In AWS mode, always create tables without indexes and constraints, and then create them after copying data.

* Wed Mar 18 2026 Rodrigo Tassinari 1.4.12
- my-mirror: if data copy can be resumed, user can't use command line option, they are gonna be automatically asked

* Tue Mar 17 2026 Rodrigo Tassinari 1.4.11
- my-drop-all-tables: Added support for Windows systems

* Tue Mar 17 2026 Rodrigo Tassinari 1.4.10
- my-drop-all-tables: Minor fixes

* Thu Mar 5 2026 Rodrigo Tassinari 1.4.9
- my-drop-all-tables: Better logs
- my-mirror: Support for defering indexes when copying full database from AWS RDS
- New tool: my-db-compare

* Thu Feb 12 2026 Rodrigo Tassinari 1.4.8
- my-mirror: New procedure for better partitioning performance

* Tue Oct 28 2025 Rodrigo Tassinari 1.4.6
- my-mirror: When copying tables, do not disable keys in destination, to reduce locks
- my-val-mirror: Fixed a bug in interval definition
- my-val-mirror: New sort definition in queries, to allow the use of indexes

* Mon Oct 27 2025 Rodrigo Tassinari 1.4.5
- my-mirror: Added support for some env vars
- my-val-mirror: Compare only last 180 days

* Fri Oct 24 2025 Rodrigo Tassinari 1.4.4
- my-mirror: copy virtual columns: fixed blocking bug
- my-val-mirror: new validation architecture

* Wed Oct 22 2025 Rodrigo Tassinari 1.4.3
- my-mirror: Fix in random generation

* Wed Oct 22 2025 Rodrigo Tassinari 1.4.2
- my-mirror: copy tables in random order, to avoid locks

* Wed Oct 22 2025 Rodrigo Tassinari 1.4.1
- my-mirror: new environment variable: MY_MIRROR_TXN_LEN_FORCE_LIMIT

* Wed Oct 22 2025 Rodrigo Tassinari 1.4.0
- New tool: my-val-mirror

* Mon Oct 20 2025 Rodrigo Tassinari 1.3.4
- my-mirror: More friendly logs

* Tue Oct 14 2025 Rodrigo Tassinari 1.3.3
- New tool: my-drop-all-events
- my-mirror: When copying events, copy only non-existing in destination

* Thu Oct 9 2025 Rodrigo Tassinari 1.3.2
- my-kill-blockers: new option - do not exclude root user

* Wed Oct 8 2025 Rodrigo Tassinari 1.3.1
- my-mirror: fix when copying with AWS mode disabled

* Mon Oct 6 2025 Rodrigo Tassinari 1.3.0
- New tool: my-drop-all-routines
- my-mirror: Partition length is now full size (rows * avg row length)

* Fri Sep 19 2025 Rodrigo Tassinari 1.2.2
- my-mirror: New max allowed packet size: 4Mb

* Wed Sep 17 2025 Rodrigo Tassinari 1.2.1
- my-mirror: Added number of threads to log

* Tue Sep 16 2025 Rodrigo Tassinari 1.2.0
- my-mirror: Support table partitioning by a timestamp column
- my-mirror: Added support for resuming table data copy

* Tue Aug 26 2025 Rodrigo Tassinari 1.1.7
- New tool: my-fix-definer-routines
- New tool: my-fix-definer-triggers

* Mon Aug 25 2025 Rodrigo Tassinari 1.1.6
- my-mirror: fix - in RDS mode, do not copy triggers
- New tool: my-fix-definer-events
- New tool: my-fix-definer-views

* Tue Aug 19 2025 Rodrigo Tassinari 1.1.5
- my-mirror: allow multi-threading in table splitting phase

* Tue Jul 22 2025 Rodrigo Tassinari 1.1.4
- my-drop-all-tables: print drop script execution

* Mon Jul 21 2025 Rodrigo Tassinari 1.1.3
- my-mirror: fix in cancelling operation
- my-mirror: no more need for a spool when copying data with limited batch size

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
