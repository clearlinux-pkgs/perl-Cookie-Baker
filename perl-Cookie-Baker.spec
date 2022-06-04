#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Cookie-Baker
Version  : 0.11
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cookie-Baker-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cookie-Baker-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libcookie-baker-perl/libcookie-baker-perl_0.09-1.debian.tar.xz
Summary  : 'Cookie string generator / parser'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Cookie-Baker-license = %{version}-%{release}
Requires: perl-Cookie-Baker-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
# NAME
Cookie::Baker - Cookie string generator / parser
# SYNOPSIS
use Cookie::Baker;

%package dev
Summary: dev components for the perl-Cookie-Baker package.
Group: Development
Provides: perl-Cookie-Baker-devel = %{version}-%{release}
Requires: perl-Cookie-Baker = %{version}-%{release}

%description dev
dev components for the perl-Cookie-Baker package.


%package license
Summary: license components for the perl-Cookie-Baker package.
Group: Default

%description license
license components for the perl-Cookie-Baker package.


%package perl
Summary: perl components for the perl-Cookie-Baker package.
Group: Default
Requires: perl-Cookie-Baker = %{version}-%{release}

%description perl
perl components for the perl-Cookie-Baker package.


%prep
%setup -q -n Cookie-Baker-0.11
cd %{_builddir}
tar xf %{_sourcedir}/libcookie-baker-perl_0.09-1.debian.tar.xz
cd %{_builddir}/Cookie-Baker-0.11
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Cookie-Baker-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Cookie-Baker
cp %{_builddir}/Cookie-Baker-0.11/LICENSE %{buildroot}/usr/share/package-licenses/perl-Cookie-Baker/3974dccbc4afd3a0f00ad1f2d510bbf5d862bda7
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Cookie-Baker/80c8efff028b1bcdbfff7c5e90ea30cbeed692c5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Cookie::Baker.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Cookie-Baker/3974dccbc4afd3a0f00ad1f2d510bbf5d862bda7
/usr/share/package-licenses/perl-Cookie-Baker/80c8efff028b1bcdbfff7c5e90ea30cbeed692c5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
