%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Fortran
Summary:	Math::Fortran perl module
Summary(pl):	Modu³ perla Math::Fortran
Name:		perl-Math-Fortran
Version:	0.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Fortran - Perl implimentations of Fortrans sign and log10.

%description -l pl
Math::Fortran dostarcza dwóch funkcji pochodz±cych z Fortrana: sign i
log10.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Fortran.pm
%{_mandir}/man3/*
