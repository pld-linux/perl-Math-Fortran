%define	pdir	Math
%define	pnam	Fortran
%include	/usr/lib/rpm/macros.perl
Summary:	Math-Fortran perl module
Summary(pl):	Modu� perla Math-Fortran
Name:		perl-Math-Fortran
Version:	0.01
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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
