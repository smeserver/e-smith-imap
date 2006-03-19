Summary: Module for configuring the IMAP server
%define name e-smith-imap
Name: %{name}
%define version 1.4.0
%define release 02
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-imap-1.4.0-concurrency_control.patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: daemontools
Requires: ipsvd
Requires: stunnel-tls
Requires: mailfront
Requires: dovecot
Requires: e-smith-cvm-unix-local
Requires: e-smith-lib >= 1.15.1-33
Obsoletes: imap
Obsoletes: e-smith-wu-imap
Obsoletes: e-smith-ssl-imap
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
AutoReqProv: no
%define stunnelid 451
%define imaplogid 1001

%description
Module for configuring the IMAP server

%changelog
* Sun Mar 19 2006 Charlie Brady <charlie_brady@mitel.com> 1.4.0-02
- Fix per IP concurrency control. [SME: 1081]

* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.4.0-01
- Roll stable stream version. [SME: 1016]

* Fri Feb 24 2006 Charlie Brady <charlie_brady@mitel.com> 1.3.1-17
- Add default initializers for imap & imaps db records. [SME: 561]
- Add db driven global and per IP concurrency controls. [SME: 884]

* Fri Feb 24 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.1-16
- Add /sbin/e-smith/merge_maildirs which can be run if you need
  to merge two maildirs [SME: 875]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.3.1-15
- Bump release number only

* Mon Oct 17 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.3.1-14]
- Fix typo in env setup in imaps run script - Thanks Andre Duclos [SF: 1327437]

* Wed Sep 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-13]
- Ensure that ./peers/0 is only readable if "access" is set to
  "public". This change allows a "localhost" setting to do the
  right thing. [SF: 1294719]

* Wed Aug 10 2005 Shad Lords <slords@mail.com>
- [1.3.1-12]
- Move db entries to e-smith-email [SF: 1256055]

* Thu Jun 23 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-11]
- Switch to using stunnel-tls package. [SF: 1225972]

* Mon Jun 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-10]
- Add Obsoletes header for e-smith-ssl-imap. [SF: 1219069]

* Tue Mar 29 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-09]
- Create empty template-begin template fragments for tcpsvd
  ACL files.

* Tue Mar 29 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-08]
- Run ./control/1 from run script, to ensure that ACLs
  are set at startup. Don't bother with sigusr1 at
  bootstrap-console-save, as it will be ignored.
- Fix imap folder relocations.

* Sat Mar 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-07]
- Fix SystemName lookup in imap/control/1 script.

* Sat Mar 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-06]
- Use imap sigusr1 handler script to update network ACLs
  for both imap and imaps.
- Be more careful about permissions for copied pem cert.
- Remove dead imap-conf symlinks.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-05]
- Remove imapd.pem templates, and just copy system pem file, via
  sigusr1 handler script.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-04]
- Fix ownership of /var/log/imaps

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-03]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]
- Convert from tcpserver to tcpsvd for imap service. Manage
  network ACLs and daemon environment using peers directory.
- Update maildir relocate script to use standard dovecot
  hierarchy separator ('.').

* Thu Jan 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-02]
- Fix spelling in IMAP_CAPABILITY setting. [MN00040881]
- Create imapd.pem via template expansion, and merge into
  imap-conf action.
- Add db default values for imaps service - to come later.
- Clean up genfilelist call - remove sed invocation.

* Fri Dec 31 2004 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-01]
- Rolling new development stream - 1.3.1

* Fri Dec 24 2004 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-05]
- Fix quoting in IMAP_CAPABILITIES setting, and clean env before
  running envdir from run script. [MN00040881]

* Wed Dec 22 2004 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-04]
- Add IMAP_CAPABILITIES variable to imapd's environment [MN00040881]

* Fri May 14 2004 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-03]
- Remove misplaced root/var/service/runenv [MN00029842, MN00033394]

* Fri May 14 2004 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-02]
- Provide new backend imap script so that setting of imapdpath in
  environment by tcpserver is effective. [MN00029842, MN00033394]

* Tue Jan 27 2004 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-01]
- rolling to dev - 1.3.0

* Tue Jan 27 2004 Michael Soulier <msoulier@e-smith.com>
- [1.2.0-01]
- rolling to stable - 1.2.0

* Fri Nov 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-02]
- Move setup of cvm environment variables into CDB file. Saves
  execution of envdir, and allows customisation per IP address.
  [charlieb 10960]

* Fri Nov 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-01]
- Changing version to development stream number - 1.1.0

* Wed Aug 27 2003 Michael Soulier <msoulier@e-smith.com>
- [1.0.0-03]
- Added K* init symlinks for runlevels 0, 1 and 6. [msoulier 9761]

* Wed Jul  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.0.0-02]
- Remove event name check in email-relocate-maildirs [gordonr 9337]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.0.0-01]
- Changing version to stable stream number - 1.0.0

* Mon Jun 23 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.5-07]
- Template /etc/dovecot.conf and runenv/* dovecot environment setup files.
  Rename conf-imap-tcprules to conf-imap to cover additional template
  expansions.  [charlieb 587]
- Increase default ulimit setting to 128MB. [charlieb 9113]

* Thu Jun 19 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.5-06]
- Update tcpserver's cdb file in email-update and remoteaccess-update.
  [charlieb 9068]

* Wed Jun  4 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.5-05]
- Use create-system-user to create imaplog user. Add Requires header to ensure
  that %pre script can run. [charlieb 6033]

* Tue Jun  3 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.5-04]
- Fix %pre script so that uid other than expected generates warning,
  but install proceeds. [charlieb 6033]

* Thu Apr 24 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.5-03]
- Do maildir relocation in two steps, first move top level folders into
  ~/Mail, then do depthwise move and rename into Maildir. Much faster too.
  [charlieb 8273]

* Thu Apr 24 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.5-02]
- Redo maildir relocation to account for leading ;. [charlieb 8272]
- Rewrite subscription files contents, to change hierarchy separator, and to
  omit leading Mail/. [charlieb 8272]
- For now, do not relocate ~admin maildirs - we need to work out how to avoid walking
  all of /home/e-smith/files. [charlieb 8273]

* Thu Apr 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.0.5-01]
- Rebuild tarball [gordonr 587]

* Tue Apr 22 2003 Mark Knox <markk@e-smith.com>
- [0.0.4-01]
- Updated Summary to reflect actual contents [markk 8272]
- Fixed file list generation to include all files [markk 8272]

* Fri Apr 18 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.3-01]
- Break runenv into runenv and imapfront.env - we don't need export
  this way. [charlieb 8281]
- Make sure that PRNG file is initialisedbefore we run tcpserver.
  [charlieb 8281]

* Fri Apr 18 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-15]
- Ensure that runenv environment is exported (we should break this
  into exportenv and runenv). [charlieb 8281]

* Fri Apr 18 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-14]
- Remove %post creation of SSL PRNG seed file, and change filelist
  from %ghost to %config(noreplace). [charlieb 8281]
- Setup SASL evvironment for imap run file via runenv directory.
  Allow override of imap path from runenv. [charlieb 587]

* Thu Apr 17 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-13]
- Remove group write permission on SSL PRNG seed file. [charlieb 8281]

* Thu Apr 17 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-12]
- Fix chown => chmod typo. [charlieb 8281]
- Move .mailboxlist files to Maildir/.subscriptions. [charlieb 8274]

* Tue Apr 15 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-11]
- Fix permissions problem in imapd certificate file. [charlieb 8281]
- Add maildir relocate script (from e-smith-email) and rewrite it
  to provide new locations compatible with dovecot. [charlieb 8273]

* Thu Apr  3 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-10]
- Remove email-relocate-maildirs script - it lives in e-smith-email, and
  we haven't modified it yet. [charlieb 587]

* Thu Apr  3 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-09]
- Remove "-D debug" from stunnel args in imap/run - we can't have
  passwords logged in plaintext. [charlieb 587]

* Tue Apr  1 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-08]
- Fix rpm build problem with last change - missing directories. [charlieb 587]

* Tue Apr  1 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-07]
- Create imapd.pem certificate in the place where it is required. Add
  rc7.d startup script so that imap runs on startup. [charlieb 587]

* Fri Mar 21 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-06]
- Fix tcpserver CDB file name. [charlieb 587]
- Ansure that stunnel user is created in %pre. [charlieb 587]
- Allow various settings for run script to be set from
  an envdir, including imap daemon executable path. [charlieb 587]

* Fri Mar 21 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-05]
- Fix spec file to generate filelist from repository (where possible).
  [charlieb 687]

* Fri Mar 21 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-04]
- Include action scripts in RPM file list. [charlieb 587]

* Fri Mar 21 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-03]
- Add minimal chroot jail for stunnel [charlieb 587]

* Fri Mar 21 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-02]
- Add dependency on e-smith-cvm-unix-local - which itself depends
  on cvm. [charlieb 587]

* Fri Mar 21 2003 Charlie Brady <charlieb@e-smith.com>
- [0.0.2-01]
- Add PEM certificate create/update action. Add tcprules update action.
  [charlieb 587]
- Add Obsoletes headers to force removal of e-smith-wu-imap and imap RPMs.
  Add dependency on dovecot RPM. [charlieb 587]

* Thu Mar 20 2003 Charlie Brady <charlieb@e-smith.com>
- Initial

%prep
%setup
%patch0 -p1

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
mkdir -p $RPM_BUILD_ROOT/service
ln -s /var/service/imap $RPM_BUILD_ROOT/service/imap

mkdir -p $RPM_BUILD_ROOT/var/log/imap
touch $RPM_BUILD_ROOT/var/service/imap/down
mkdir -p $RPM_BUILD_ROOT/var/service/imap/ssl/{dev,usr/share/ssl}
mkdir -p $RPM_BUILD_ROOT/var/service/imap/peers
mkdir -p $RPM_BUILD_ROOT/etc/e-smith/templates/var/service/imap/peers
touch $RPM_BUILD_ROOT/etc/e-smith/templates/var/service/imap/peers/{0,local}/template-begin
touch $RPM_BUILD_ROOT/var/service/imap/ssl/seed

mkdir -p $RPM_BUILD_ROOT/etc/e-smith/templates/var/service/imap/config
echo SSLUID=%{stunnelid} > $RPM_BUILD_ROOT/etc/e-smith/templates/var/service/imap/config/SSLUID
echo SSLGID=%{stunnelid} > $RPM_BUILD_ROOT/etc/e-smith/templates/var/service/imap/config/SSLGID

ln -s /var/service/imaps $RPM_BUILD_ROOT/service/imaps

mkdir -p $RPM_BUILD_ROOT/var/log/imaps
touch $RPM_BUILD_ROOT/var/service/imaps/down
mkdir -p $RPM_BUILD_ROOT/var/service/imaps/peers

mkdir -p $RPM_BUILD_ROOT/etc/e-smith/templates/var/service/imaps/config
echo SSLUID=%{stunnelid} > $RPM_BUILD_ROOT/etc/e-smith/templates/var/service/imaps/config/SSLUID
echo SSLGID=%{stunnelid} > $RPM_BUILD_ROOT/etc/e-smith/templates/var/service/imaps/config/SSLGID

/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/imap 'attr(1755,root,root)' \
    --file /var/service/imap/run 'attr(0755,root,root)' \
    --file /var/service/imap/control/1 'attr(0755,root,root)' \
    --dir /var/service/imap/log 'attr(0755,root,root)' \
    --file /var/service/imap/log/run 'attr(0755,root,root)' \
    --file /var/service/imap/imapd 'attr(0755,root,root)' \
    --file /var/service/imap/ssl/seed 'config(noreplace) %attr(0600,stunnel,stunnel)' \
    --dir /var/service/imap/ssl 'attr(0755,root,root)' \
    --dir /var/service/imap/ssl/usr 'attr(0755,root,root)' \
    --dir /var/service/imap/ssl/dev 'attr(0755,root,root)' \
    --dir /var/log/imap 'attr(0755,imaplog,imaplog)' \
    --file /var/service/imap/ssl/usr/share/ssl/openssl.cnf 'attr(0644,root,root)' \
    --dir /var/service/imaps 'attr(1755,root,root)' \
    --file /var/service/imaps/run 'attr(0755,root,root)' \
    --file /var/service/imaps/control/1 'attr(0755,root,root)' \
    --file /var/service/imaps/control/2 'attr(0755,root,root)' \
    --dir /var/service/imaps/log 'attr(0755,root,root)' \
    --file /var/service/imaps/log/run 'attr(0755,root,root)' \
    --dir /var/log/imaps 'attr(0755,imaplog,imaplog)' \
    --file /sbin/e-smith/merge_maildirs 'attr(0755,root,root)' \
    > %{name}-%{version}-%{release}-filelist

%pre
/sbin/e-smith/create-system-user stunnel %{stunnelid} \
    'chrooted stunnel user user' /var/log/imap/ssl /bin/false
/sbin/e-smith/create-system-user imaplog %{imaplogid} \
    'imap output log user' /var/log/imap /bin/false

%preun

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
