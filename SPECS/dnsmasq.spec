%define testrelease 0
%define releasecandidate 0
%if 0%{testrelease}
  %define extrapath test-releases/
  %define extraversion test%{testrelease}
%endif
%if 0%{releasecandidate}
  %define extrapath release-candidates/
  %define extraversion rc%{releasecandidate}
%endif

%define _hardened_build 1

Name:           dnsmasq
Version:        2.79
Release:        26%{?extraversion:.%{extraversion}}%{?dist}
Summary:        A lightweight DHCP/caching DNS server

License:        GPLv2 or GPLv3
URL:            http://www.thekelleys.org.uk/dnsmasq/
Source0:        http://www.thekelleys.org.uk/dnsmasq/%{?extrapath}%{name}-%{version}%{?extraversion}.tar.xz
Source1:        %{name}.service
Source2:        dnsmasq-systemd-sysusers.conf

# https://bugzilla.redhat.com/show_bug.cgi?id=1495409
Patch1:         dnsmasq-2.77-underflow.patch
Patch3:         dnsmasq-2.78-fips.patch
Patch4:         dnsmasq-2.80-dnssec.patch
Patch5:         dnsmasq-2.79-rh1602477.patch
# Few changes not yet in upstream
Patch6:         dnsmasq-2.79-rh1602477-2.patch
# commit 60ac10d8d86e6f95ab0f06abe6c42596adcedcb8
Patch7:         dnsmasq-2.76-rh1752569.patch
# Report failure when no release would be sent
Patch8:         dnsmasq-2.79-rh1749092-fail.patch
Patch9:         dnsmasq-2.76-rh1728698-1.patch
Patch10:        dnsmasq-2.79-rh1728698-2.patch
Patch11:        dnsmasq-2.76-rh1728698-3.patch
Patch12:        dnsmasq-2.79-rh1728698-4.patch
Patch13:        dnsmasq-2.79-rh1746411.patch
Patch14:        dnsmasq-2.79-rh1700916.patch
Patch15:        dnsmasq-2.80-rh1795370.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1779187
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=97f876b64c22b2b18412e2e3d8506ee33e42db7c
Patch16:        dnsmasq-2.80-unaligned-addresses-in-DHCPv6-packet.patch
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=f064188032a829efdcf3988b24ac795ff52785ec
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=137286e9baecf6a3ba97722ef1b49c851b531810
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=79aba0f10ad0157fb4f48afbbcb03f094caff97a
Patch17:        dnsmasq-2.81-prefix-ranges-or-list-of-ipv6-addresses.patch
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=52ec7836139e7a11374971905e5ac0d2d02e32c0
Patch18:        dnsmasq-2.81-tag-filtering-of-dhcp-host-directives.patch
Patch19:        dnsmasq-2.81-correct-range-check-of-dhcp-host-prefix.patch
Patch20:        dnsmasq-2.81-optimize-fds-close.patch
Patch21:        dnsmasq-2.81-rh1829448.patch
Patch22:        dnsmasq-2.79-CVE-2020-25681.patch
Patch23:        dnsmasq-2.79-CVE-2020-25684.patch
Patch24:        dnsmasq-2.79-CVE-2020-25685.patch
Patch25:        dnsmasq-2.79-CVE-2020-25686.patch
Patch26:        dnsmasq-2.79-CVE-2020-25686-2.patch
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=3f535da79e7a42104543ef5c7b5fa2bed819a78b
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=04490bf622ac84891aad6f2dd2edf83725decdee
Patch27:        dnsmasq-2.79-mixed-family-failed.patch
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=b2ed691eb3ca6488a8878f5f3dd950a07b14a9db
Patch28:        dnsmasq-2.81-netlink-table.patch
Patch29:        dnsmasq-2.84-bind-dynamic-netlink.patch
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=74d4fcd756a85bc1823232ea74334f7ccfb9d5d2
Patch30:        dnsmasq-2.85-CVE-2021-3448.patch
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=03212e533b1e07aba30d2f4112009dc3af867ea5
Patch31:        dnsmasq-2.80-man-nameing.patch
Patch32:        dnsmasq-2.79-alternative-lease.patch
Patch33:        dnsmasq-2.86-dhcpv6-client-arch.patch
# Downstream only patch; https://bugzilla.redhat.com/show_bug.cgi?id=1919894
# Similar functionality is implemented since 2.86 in upstream, but introduced
# several regressions. This implements just limited change in different way.
Patch34:        dnsmasq-2.79-server-domain-rh1919894.patch
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=03345ecefeb0d82e3c3a4c28f27c3554f0611b39
Patch35:        dnsmasq-2.87-CVE-2022-0934.patch
# http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=commit;h=dded78b2338147daf69064d6d48c16b12744e441
Patch36:        dnsmasq-2.81-option6-ntp-server-suboption.patch
# https://thekelleys.org.uk/gitweb/?p=dnsmasq.git;h=3052ce208acf602f0163166dcefb7330d537cedb
Patch37:        dnsmasq-2.81-linux-SIOCGSTAMP.patch
# Downstream only patch; fixes Patch34 change
Patch38:        dnsmasq-2.79-server-domain-fixup.patch
# https://thekelleys.org.uk/gitweb/?p=dnsmasq.git;h=f8c77edbdffb8ada7753ea9fa104f0f6da70cfe3
Patch39:        dnsmasq-2.81-dhcpv6-relay-link-address.patch

# This is workaround to nettle bug #1549190
# https://bugzilla.redhat.com/show_bug.cgi?id=1549190
Requires:       nettle >= 3.4

BuildRequires:  dbus-devel
BuildRequires:  pkgconfig
BuildRequires:  libidn2-devel
BuildRequires:  nettle-devel
Buildrequires:  gcc

BuildRequires:  systemd
%{?systemd_requires}

%description
Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server.
It is designed to provide DNS and, optionally, DHCP, to a small network.
It can serve the names of local machines which are not in the global
DNS. The DHCP server integrates with the DNS server and allows machines
with DHCP-allocated addresses to appear in the DNS with names configured
either in each host or in a central configuration file. Dnsmasq supports
static and dynamic DHCP leases and BOOTP for network booting of diskless
machines.

%package        utils
Summary:        Utilities for manipulating DHCP server leases

%description    utils
Utilities that use the standard DHCP protocol to query/remove a DHCP
server's leases.


%prep
%setup -q -n %{name}-%{version}%{?extraversion}
%patch1 -p1 -b .underflow
%patch3 -p1 -b .fips
%patch4 -p1 -b .dnssec
%patch5 -p1 -b .rh1602477
%patch6 -p1 -b .rh1602477-2
%patch7 -p1 -b .rh1752569
%patch8 -p1 -b .rh1752569
%patch9 -p1 -b .rh1728698-1
%patch10 -p1 -b .rh1728698-2
%patch11 -p1 -b .rh1728698-3
%patch12 -p1 -b .rh1728698-4
%patch13 -p1 -b .rh1746411
%patch14 -p1 -b .rh1700916
%patch15 -p1 -b .rh1795370
%patch16 -p1 -b .rh1779187-1
%patch17 -p1 -b .rh1779187-2
%patch18 -p1 -b .rh1779187-3
%patch19 -p1 -b .rh1779187-4
%patch20 -p1 -b .rh1816613
%patch21 -p1 -b .rh1829448
%patch22 -p1 -b .CVE-2020-25681
%patch23 -p1 -b .CVE-2020-25684
%patch24 -p1 -b .CVE-2020-25685
%patch25 -p1 -b .CVE-2020-25686
%patch26 -p1 -b .CVE-2020-25686-2
%patch27 -p1 -b .rh1921153
%patch28 -p1 -b .rh1887649-table
%patch29 -p1 -b .rh1887649
%patch30 -p1 -b .CVE-2021-3448
%patch31 -p1 -b .rh1947039
%patch32 -p1 -b .rh1998448
%patch33 -p1 -b .dhcpv6-client-arch
%patch34 -p1 -b .rh1919894
%patch35 -p1 -b .CVE-2022-0934
%patch36 -p1 -b .rh2049691
%patch37 -p1 -b .SIOCGSTAMP
%patch38 -p1 -b .rh2120357
%patch39 -p1 -b .rh2169355

# use /var/lib/dnsmasq instead of /var/lib/misc
for file in dnsmasq.conf.example man/dnsmasq.8 man/es/dnsmasq.8 src/config.h; do
    sed -i 's|/var/lib/misc/dnsmasq.leases|/var/lib/dnsmasq/dnsmasq.leases|g' "$file"
done

# fix the path to the trust anchor
sed -i 's|%%%%PREFIX%%%%|%{_prefix}|' dnsmasq.conf.example

#set dnsmasq user / group
sed -i 's|#user=|user=dnsmasq|' dnsmasq.conf.example
sed -i 's|#group=|group=dnsmasq|' dnsmasq.conf.example
#set default user /group in src/config.h
sed -i 's|#define CHUSER "nobody"|#define CHUSER "dnsmasq"|' src/config.h
sed -i 's|#define CHGRP "dip"|#define CHGRP "dnsmasq"|' src/config.h

# optional parts
sed -i 's|^COPTS[[:space:]]*=|\0 -DHAVE_DBUS -DHAVE_LIBIDN2 -DHAVE_DNSSEC|' Makefile

#enable /etc/dnsmasq.d fix bz 526703, ignore RPM backup files
cat << EOF >> dnsmasq.conf.example

# Include all files in /etc/dnsmasq.d except RPM backup files
conf-dir=/etc/dnsmasq.d,.rpmnew,.rpmsave,.rpmorig
EOF


%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%make_build -C contrib/lease-tools CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
# normally i'd do 'make install'...it's a bit messy, though
mkdir -p $RPM_BUILD_ROOT%{_sbindir} \
        $RPM_BUILD_ROOT%{_mandir}/man8 \
        $RPM_BUILD_ROOT%{_var}/lib/dnsmasq \
        $RPM_BUILD_ROOT%{_sysconfdir}/dnsmasq.d \
        $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d
install src/dnsmasq $RPM_BUILD_ROOT%{_sbindir}/dnsmasq
install dnsmasq.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/dnsmasq.conf
install dbus/dnsmasq.conf $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d/
install -m 644 man/dnsmasq.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install -D trust-anchors.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/trust-anchors.conf

# utils sub package
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
         $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 contrib/lease-tools/dhcp_release $RPM_BUILD_ROOT%{_bindir}/dhcp_release
install -m 644 contrib/lease-tools/dhcp_release.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_release.1
install -m 755 contrib/lease-tools/dhcp_release6 $RPM_BUILD_ROOT%{_bindir}/dhcp_release6
install -m 644 contrib/lease-tools/dhcp_release6.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_release6.1
install -m 755 contrib/lease-tools/dhcp_lease_time $RPM_BUILD_ROOT%{_bindir}/dhcp_lease_time
install -m 644 contrib/lease-tools/dhcp_lease_time.1 $RPM_BUILD_ROOT%{_mandir}/man1/dhcp_lease_time.1

# Systemd
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}
rm -rf %{buildroot}%{_initrddir}

#install systemd sysuser file
install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysusersdir}/dnsmasq.conf

%pre
#precreate users so that rpm can install files owned by that user
%sysusers_create_package %{name} %{SOURCE2}

%post
#https://fedoraproject.org/wiki/Changes/SystemdSysusers
%systemd_post dnsmasq.service

%preun
%systemd_preun dnsmasq.service

%postun
%systemd_postun_with_restart dnsmasq.service

%files
%doc CHANGELOG FAQ doc.html setup.html dbus/DBus-interface
%license COPYING COPYING-v3
%defattr(0644,root,dnsmasq,0755)
%config(noreplace) %{_sysconfdir}/dnsmasq.conf
%dir %{_sysconfdir}/dnsmasq.d
%dir %{_var}/lib/dnsmasq
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/dnsmasq.conf
%{_unitdir}/%{name}.service
%{_sbindir}/dnsmasq
%{_mandir}/man8/dnsmasq*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/trust-anchors.conf
%{_sysusersdir}/dnsmasq.conf

%files utils
%license COPYING COPYING-v3
%{_bindir}/dhcp_*
%{_mandir}/man1/dhcp_*

%changelog
* Wed Feb 15 2023 Petr Menšík <pemensik@redhat.com> - 2.79-26
- Avoid DHCPv6 relayed replies with Client Link-Layer Address (#2169355)

* Thu Jan 26 2023 Petr Menšík <pemensik@redhat.com> - 2.79-25
- Use upstream change for CVE-2022-0934 (#2164859)

* Mon Aug 22 2022 Petr Menšík <pemensik@redhat.com> - 2.79-24
- Prevent endless loop in forward_query (#2120357)

* Thu May 12 2022 Petr Menšík <pemensik@redhat.com> - 2.79-23
- Add IPv6 ntp-server suboptions support (#2049691)

* Fri Mar 25 2022 Petr Menšík <pemensik@redhat.com> - 2.79-22
- Prevent use after free in dhcp6_no_relay (CVE-2022-0934)

* Thu Jan 27 2022 Petr Menšík <pemensik@redhat.com> - 2.79-21
- Send queries only to best domain-specific server (#1919894)

* Mon Sep 20 2021 Petr Menšík <pemensik@redhat.com> - 2.79-20
- Offer alternate DHCPv6 address if requested is already leased (#1998448)

* Tue Jun 29 2021 Petr Menšík <pemensik@redhat.com> - 2.79-19
- Correct typo in man page (#1947039)

* Thu Mar 18 2021 Petr Menšík <pemensik@redhat.com> - 2.79-18
- Properly randomize outgoing ports also with bound interface (CVE-2021-3448)

* Fri Feb 12 2021 Petr Menšík <pemensik@redhat.com> - 2.79-17
- Fix sporadic bind-dynamic failures (#1887649)

* Wed Jan 27 2021 Petr Menšík <pemensik@redhat.com> - 2.79-16
- Fix network errors on queries both from ipv4 and ipv6 (#1921153)

* Wed Nov 25 2020 Petr Menšík <pemensik@redhat.com> - 2.79-15
- Fix various issues in dnssec validation (CVE-2020-25681)
- Accept responses only on correct sockets (CVE-2020-25684)
- Use strong verification on queries (CVE-2020-25685)

* Wed Aug 26 2020 Tomas Korbar <tkorbar@redhat.com> - 2.79-14
- Honor sysusers.d during installation (#1819684)

* Tue May 05 2020 Petr Menšík <pemensik@redhat.com> - 2.79-13
- Fix mixed address family reservations on DHCP (#1829448)

* Mon Mar 30 2020 Tomas Korbar <tkorbar@redhat.com> - 2.79-12
- Minimize count of close syscalls on startup (#1816613)

* Mon Mar 02 2020 Petr Menšík <pemensik@redhat.com> - 2.79-11
- Support multiple static leases for single mac on IPv6 (#1779187)

* Mon Feb 17 2020 Tomas Korbar <tkorbar@redhat.com> - 2.79-10
- Fix memory leak in helper.c (#1795370)

* Tue Dec 10 2019 Tomas Korbar <tkorbar@redhat.com> - 2.79-9
- Fix replies to non-recursive queries (#1700916)

* Mon Dec 09 2019 Tomas Korbar <tkorbar@redhat.com> - 2.79-8
- Fix dhcp_lease_time (#1746411)

* Mon Dec 09 2019 Tomas Korbar <tkorbar@redhat.com> - 2.79-7
- Fix TCP queries after interface recreation (#1728698)

* Mon Sep 30 2019 Petr Menšík <pemensik@redhat.com> - 2.79-6
- Send dhcp_release even for addresses not on local network (#1749092)

* Thu Jul 18 2019 Petr Menšík <pemensik@redhat.com> - 2.79-5
- Fix Coverity detected issues (#1602477)

* Thu Jul 26 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.79-4
- Fix %%pre scriptlet (#1548050)

* Mon Jul 02 2018 Petr Menšík <pemensik@redhat.com> - 2.79-3
- Make dnsmasq leases writeable by root again (#1554390)

* Mon Jul 02 2018 Petr Menšík <pemensik@redhat.com> - 2.79-2
- Fix passing of dnssec enabled queries (#1597309)

* Thu Mar 15 2018 Petr Menšík <pemensik@redhat.com> - 2.79-1
- Rebase to 2.79
- Stop using nettle_hashes directly, use access function (#1548060)
- Do not break on cname with spaces (#1498667)
- Require nettle 3.4+
- Do not own sysusers.d directory, already depends on systemd providing it

* Fri Mar 02 2018 Petr Menšík <pemensik@redhat.com> - 2.78-7
- Emit warning with dnssec enabled on FIPS system (#1549507)

* Sun Feb 25 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.78-6
- Create user before installing files (#1548050)

* Fri Feb 23 2018 Petr Menšík <pemensik@redhat.com> - 2.78-5
- Create user first and then restart service

* Thu Feb 22 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.78-4
- add gcc into buildrequires
- deliver an extra sysusers.d file to create dnsmasq user/group
- set CHUSER and CHGRP to dnsmasq in src/config.h

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Petr Menšík <pemensik@redhat.com> - 2.78-2
- DNSSEC fix for wildcard NSEC records (CVE-2017-15107)

* Tue Oct 03 2017 Petr Menšík <pemensik@redhat.com> - 2.78-1
- Rebase to 2.78

* Tue Oct 03 2017 Petr Menšík <pemensik@redhat.com> - 2.77-9
- More patches related to CVE-2017-14491

* Mon Oct 02 2017 Petr Menšík <pemensik@redhat.com> - 2.77-8
- Security fix, CVE-2017-14491, DNS heap buffer overflow
- Security fix, CVE-2017-14492, DHCPv6 RA heap overflow
- Security fix, CVE-2017-14493, DHCPv6 - Stack buffer overflow
- Security fix, CVE-2017-14494, Infoleak handling DHCPv6
- Security fix, CVE-2017-14496, Integer underflow in DNS response creation
- Security fix, CVE-2017-14495, OOM in DNS response creation
- Misc code cleanups arising from Google analysis
- Do not include stdio.h before dnsmasq.h

* Thu Sep 14 2017 Petr Menšík <pemensik@redhat.com> - 2.77-7
- Fix CVE-2017-13704

* Mon Aug 14 2017 Petr Menšík <pemensik@redhat.com> - 2.77-6
- Own the /usr/share/dnsmasq dir (#1480856)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Petr Menšík <pemensik@redhat.com> - 2.77-3
- Update to 2.77

* Fri May 12 2017 Petr Menšík <pemensik@redhat.com> - 2.77-2.rc2
- Fix dhcp

* Thu May 11 2017 Petr Menšík <pemensik@redhat.com> - 2.77-1
- Update to 2.77rc2

* Thu May 11 2017 Petr Menšík <pemensik@redhat.com>
- Include dhcp_release6 tool and license in utils
- Support for IDN 2008 (#1449150)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.76-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Pavel Šimerda <psimerda@redhat.com> - 2.76-2
- Resolves: #1373485 - dns not updated after sleep and resume laptop

* Fri Jul 15 2016 Pavel Šimerda <psimerda@redhat.com> - 2.76-1
- New version 2.76

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Tomas Hozza <thozza@redhat.com> - 2.75-3
- Fixed minor bug in dnsmasq.conf (#1295143)

* Fri Oct 02 2015 Pavel Šimerda <psimerda@redhat.com> - 2.75-2
- Resolves: #1239256 - install trust-anchors.conf

* Wed Aug 05 2015 Pavel Šimerda <psimerda@redhat.com> - 2.75-1
- new version 2.75

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 06 2014 Nils Philippsen <nils@redhat.com> - 2.72-3
- don't include /etc/dnsmasq.d in triplicate, ignore RPM backup files instead
- package is dual-licensed GPL v2 or v3
- drop %%triggerun, we're not supposed to automatically migrate from SysV to
  systemd anyway

* Mon Oct 06 2014 Tomas Hozza <thozza@redhat.com> - 2.72-2
- Fix typo in default configuration (#1149459)

* Thu Sep 25 2014 Tomas Hozza <thozza@redhat.com> - 2.72-1
- Update to 2.72 stable

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Tomas Hozza <thozza@redhat.com> - 2.71-1
- Update to 2.71 stable

* Fri Apr 25 2014 Tomas Hozza <thozza@redhat.com> - 2.70-1
- Update to 2.70 stable

* Fri Apr 11 2014 Tomas Hozza <thozza@redhat.com> - 2.69-1
- Update to 2.69 stable

* Mon Mar 24 2014 Tomas Hozza <thozza@redhat.com> - 2.69-0.1.rc1
- Update to 2.69rc1
- enable DNSSEC implementation

* Mon Dec 09 2013 Tomas Hozza <thozza@redhat.com> - 2.68-1
- Update to 2.68 stable

* Tue Nov 26 2013 Tomas Hozza <thozza@redhat.com> - 2.68-0.1.rc3
- Update to 2.68rc3

* Fri Nov 01 2013 Tomas Hozza <thozza@redhat.com> - 2.67-1
- Update to 2.67 stable
- Include one post release upstream fix for CNAME

* Fri Oct 18 2013 Tomas Hozza <thozza@redhat.com> - 2.67-0.9.rc4
- update to 2.67rc4

* Wed Oct 02 2013 Tomas Hozza <thozza@redhat.com> - 2.67-0.8.rc2
- update to 2.67rc2

* Thu Sep 12 2013 Tomas Hozza <thozza@redhat.com> - 2.67-0.7.test13
- update to 2.67test13
- use .tar.xz upstream archives

* Thu Aug 15 2013 Tomas Hozza <thozza@redhat.com> - 2.67-0.6.test7
- Use SO_REUSEPORT and SO_REUSEADDR if possible for DHCPv4/6 (#981973)

* Mon Aug 12 2013 Tomas Hozza <thozza@redhat.com> - 2.67-0.5.test7
- Don't use SO_REUSEPORT on DHCPv4 socket to prevent conflicts with ISC DHCP (#981973)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.67-0.4.test7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Tomas Hozza <thozza@redhat.com> - 2.67-0.3.test7
- update to 2.67test7
- drop merged patch
- use _hardened_build macro instead of hardcoded flags

* Fri May 17 2013 Tomas Hozza <thozza@redhat.com> - 2.67-0.2.test4
- Fix failure to start with ENOTSOCK (#962874)

* Wed May 15 2013 Tomas Hozza <thozza@redhat.com> - 2.67-0.1.test4
- update to the latest testing release 2.67test4 (#962246)
- drop mergerd patches

* Tue Apr 30 2013 Tomas Hozza <thozza@redhat.com> - 2.66-5
- dnsmasq unit file cleanup
  - drop forking Type and PIDfile and rather start dnsmasq with "-k" option
  - drop After syslog.target as this is by default

* Thu Apr 25 2013 Tomas Hozza <thozza@redhat.com> - 2.66-4
- include several fixes from upstream repo:
  - Send TCP DNS messages in one packet
  - Fix crash on SERVFAIL when using --conntrack option
  - Fix regression in dhcp_lease_time utility
  - Man page typos fixes
  - Note that dhcp_lease_time and dhcp_release work only for IPv4
  - Fix for --dhcp-match option to work also with BOOTP protocol

* Sat Apr 20 2013 Tomas Hozza <thozza@redhat.com> - 2.66-3
- Use Full RELRO when linking the daemon
- compile the daemon with PIE
- include two fixes from upstream git repo

* Thu Apr 18 2013 Tomas Hozza <thozza@redhat.com> - 2.66-2
- New stable version dnsmasq-2.66
- Drop of merged patch

* Fri Apr 12 2013 Tomas Hozza <thozza@redhat.com> - 2.66-1.rc5
- Update to latest dnsmasq-2.66rc5
- Include fix for segfault when lease limit is reached

* Fri Mar 22 2013 Tomas Hozza <thozza@redhat.com> - 2.66-1.rc1
- Update to latest dnsmasq-2.66rc1
- Dropping unneeded patches
- Enable IDN support

* Fri Mar 15 2013 Tomas Hozza <thozza@redhat.com> - 2.65-5
- Allocate dhcp_buff-ers also if daemon->ra_contexts to prevent SIGSEGV (#920300)

* Thu Jan 31 2013 Tomas Hozza <thozza@redhat.com> - 2.65-4
- Handle locally-routed DNS Queries (#904940)

* Thu Jan 24 2013 Tomas Hozza <thozza@redhat.com> - 2.65-3
- build dnsmasq with $RPM_OPT_FLAGS, $RPM_LD_FLAGS explicitly (#903362) 

* Tue Jan 22 2013 Tomas Hozza <thozza@redhat.com> - 2.65-2
- Fix for CVE-2013-0198 (checking of TCP connection interfaces) (#901555)

* Sat Dec 15 2012 Tomas Hozza <thozza@redhat.com> - 2.65-1
- new version 2.65

* Wed Dec 05 2012 Tomas Hozza <thozza@redhat.com> - 2.64-1
- New version 2.64
- Merged patches dropped

* Tue Nov 20 2012 Tomas Hozza <thozza@redhat.com> - 2.63-4
- Remove EnvironmentFile from service file (#878343)

* Mon Nov 19 2012 Tomas Hozza <thozza@redhat.com> - 2.63-3
- dhcp6 support fixes (#867054)
- removed "-s $HOSTNAME" from .service file (#753656, #822797)

* Tue Oct 23 2012 Tomas Hozza <thozza@redhat.com> - 2.63-2
- Introduce new systemd-rpm macros in dnsmasq spec file (#850096)

* Thu Aug 23 2012 Douglas Schilling Landgraf <dougsland@redhat.com> - 2.63-1
- Use .tar.gz compression, in upstream site there is no .lzma anymore
- New version 2.63

* Sat Feb 11 2012 Pádraig Brady <P@draigBrady.com> - 2.59-5
- Compile DHCP lease management utils with RPM_OPT_FLAGS

* Thu Feb  9 2012 Pádraig Brady <P@draigBrady.com> - 2.59-4
- Include DHCP lease management utils in a subpackage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 26 2011 Douglas Schilling Landgraf <dougsland@redhat.com> - 2.59-2
- do not enable service by default

* Fri Aug 26 2011 Douglas Schilling Landgraf <dougsland@redhat.com> - 2.59-1
- New version 2.59
- Fix regression in 2.58 (IPv6 issue) - bz 744814

* Fri Aug 26 2011 Douglas Schilling Landgraf <dougsland@redhat.com> - 2.58-1
- Fixed License
- New version 2.58

* Mon Aug 08 2011 Patrick "Jima" Laughton <jima@fedoraproject.org> - 2.52-5
- Include systemd unit file

* Mon Aug 08 2011 Patrick "Jima" Laughton <jima@fedoraproject.org> - 2.52-3
- Applied Jóhann's patch, minor cleanup

* Tue Jul 26 2011 Jóhann B. Guðmundsson <johannbg@gmail.com> - 2.52-3
- Introduce systemd unit file, drop SysV support

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 26 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.52-1
- New Version 2.52
- fix condrestart() in initscript bz 547605
- fix sed to enable DBUS(the '*' need some escaping) bz 553161

* Sun Nov 22 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.51-2
- fix bz 512664

* Sat Oct 17 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.51-1
- move initscript from patch to a plain text file
- drop (dnsmasq-configuration.patch) and use sed instead
- enable /etc/dnsmasq.d fix bz 526703
- change requires to package name instead of file
- new version 2.51

* Mon Oct  5 2009 Mark McLoughlin <markmc@redhat.com> - 2.48-4
- Fix multiple TFTP server vulnerabilities (CVE-2009-2957, CVE-2009-2958)

* Wed Aug 12 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.48-3
- Use lzma compressed upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.48-1
- Bugfix/feature enhancement update
- Fixing BZ#494094

* Fri May 29 2009 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.47-1
- Bugfix/feature enhancement update

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Matěj Cepl <mcepl@redhat.com> - 2.45-2
- rebuilt

* Mon Jul 21 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.45-1
- Upstream release (bugfixes)

* Wed Jul 16 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.43-2
- New upstream release, contains fixes for CVE-2008-1447/CERT VU#800113
- Dropped patch for newer glibc (merged upstream)

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.41-0.8
- Added upstream-authored patch for newer glibc (thanks Simon!)

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.41-0.7
- New upstream release

* Wed Jan 30 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.41-0.6.rc1
- Release candidate
- Happy Birthday Isaac!

* Wed Jan 23 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.41-0.5.test30
- Bugfix update

* Mon Dec 31 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.41-0.4.test26
- Bugfix/feature enhancement update

* Thu Dec 13 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.41-0.3.test24
- Upstream fix for fairly serious regression

* Tue Dec 04 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.41-0.2.test20
- New upstream test release
- Moving dnsmasq.leases to /var/lib/dnsmasq/ as per BZ#407901
- Ignoring dangerous-command-in-%%post rpmlint warning (as per above fix)
- Patch consolidation/cleanup
- Removed conditionals for Fedora <= 3 and Aurora 2.0

* Tue Sep 18 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.40-1
- Finalized upstream release
- Removing URLs from patch lines (CVS is the authoritative source)
- Added more magic to make spinning rc/test packages more seamless

* Sun Aug 26 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.40-0.1.rc2
- New upstream release candidate (feature-frozen), thanks Simon!
- License clarification

* Tue May 29 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.39-1
- New upstream version (bugfixes, enhancements)

* Mon Feb 12 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.38-1
- New upstream version with bugfix for potential hang

* Tue Feb 06 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.37-1
- New upstream version

* Wed Jan 24 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.36-1
- New upstream version

* Mon Nov 06 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.35-2
- Stop creating /etc/sysconfig on %%install
- Create /etc/dnsmasq.d on %%install

* Mon Nov 06 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.35-1
- Update to 2.35
- Removed UPGRADING_to_2.0 from %%doc as per upstream change
- Enabled conf-dir in default config as per RFE BZ#214220 (thanks Chris!)
- Added %%dir /etc/dnsmasq.d to %%files as per above RFE

* Tue Oct 24 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.34-2
- Fixed BZ#212005
- Moved %%postun scriptlet to %%post, where it made more sense
- Render scriptlets safer
- Minor cleanup for consistency

* Thu Oct 19 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.34-1
- Hardcoded version in patches, as I'm getting tired of updating them
- Update to 2.34

* Mon Aug 28 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.33-2
- Rebuild for FC6

* Tue Aug 15 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.33-1
- Update

* Sat Jul 22 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.32-3
- Added pkgconfig BuildReq due to reduced buildroot

* Thu Jul 20 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.32-2
- Forced update due to dbus version bump

* Mon Jun 12 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.32-1
- Update from upstream
- Patch from Dennis Gilmore fixed the conditionals to detect Aurora Linux

* Mon May  8 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 2.31-1
- Removed dbus config patch (now provided upstream)
- Patched in init script (no longer provided upstream)
- Added DBus-interface to docs

* Tue May  2 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 2.30-4.2
- More upstream-recommended cleanups :)
- Killed sysconfig file (provides unneeded functionality)
- Tweaked init script a little more

* Tue May  2 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 2.30-4
- Moved options out of init script and into /etc/sysconfig/dnsmasq
- Disabled DHCP_LEASE in sysconfig file, fixing bug #190379
- Simon Kelley provided dbus/dnsmasq.conf, soon to be part of the tarball

* Thu Apr 27 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 2.30-3
- Un-enabled HAVE_ISC_READER, a hack to enable a deprecated feature (request)
- Split initscript & enable-dbus patches, conditionalized dbus for FC3
- Tweaked name field in changelog entries (trying to be consistent)

* Mon Apr 24 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 2.30-2
- Disabled stripping of binary while installing (oops)
- Enabled HAVE_ISC_READER/HAVE_DBUS via patch
- Added BuildReq for dbus-devel

* Mon Apr 24 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 2.30-1
- Initial Fedora Extras RPM
