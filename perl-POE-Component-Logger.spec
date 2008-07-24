%define module  POE-Component-Logger
%define version 1.00
%define release %mkrel 7
%define	pdir	POE


Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source0: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/POE/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Requires: 	perl-POE >= 0.11
Requires:       perl-Log-Dispatch-Config >= 0.10
BuildRequires:	perl-devel
BuildRequires:  perl-POE >= 0.11
BuildRequires:  perl-Log-Dispatch-Config >= 0.10

%description 
%{module} module for perl.  A highly flexible logger component
for POE that uses Log::Dispatch and Log::Dispatch::Config for
ultimate flexibility and power.

%prep
%setup -q -n %{module}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
CFLAGS="$RPM_OPT_FLAGS" make PREFIX=%{_prefix}


%install
rm -rf $RPM_BUILD_ROOT
make PREFIX="$RPM_BUILD_ROOT%{_prefix}" install

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(444,root,root,755)
%doc README
%_mandir/*/*
%{perl_vendorlib}/POE/Component

