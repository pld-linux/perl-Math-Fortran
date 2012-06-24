%include	/usr/lib/rpm/macros.perl
Summary:	Math-Fortran perl module
Summary(pl):	Modu� perla Math-Fortran
Name:		perl-Math-Fortran
Version:	0.01
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-Fortran-%{version}.tar.gz
Patch0:		perl-Math-Fortran-man.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Fortran - Perl implimentations of Fortrans sign and log10.

%description -l pl
Math-Fortran dostarcza dw�ch funkcji pochodz�cych z Fortrana: sign i
log10.

%prep
%setup -q -n Math-Fortran-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Math/Fortran
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Math/Fortran.pm
%{perl_sitearch}/auto/Math/Fortran

%{_mandir}/man3/*
