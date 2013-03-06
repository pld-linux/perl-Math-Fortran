%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Fortran
Summary:	Math::Fortran - Perl implementations of Fortrans sign and log10.
Summary(pl.UTF-8):	Math::Fortran - perlowe implementacje funkcji Fortranu sign i log10
Name:		perl-Math-Fortran
Version:	0.01
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9369eaa198ba8eab337e90e57f273dc
Patch0:		%{name}-man.patch
URL:		http://search.cpan.org/dist/Math-Fortran/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Fortran contains Perl implementations of Fortrans sign and
log10.

%description -l pl.UTF-8
Math::Fortran dostarcza dwie funkcje pochodzące z Fortranu: sign i
log10.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Fortran.pm
%{_mandir}/man3/Math::Fortran.3pm*
