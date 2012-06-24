%include	/usr/lib/rpm/macros.perl
Summary:	Math-Fortran perl module
Summary(pl):	Modu� perla Math-Fortran
Name:		perl-Math-Fortran
Version:	0.01
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-Fortran-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Math/Fortran.pm
%{_mandir}/man3/*
