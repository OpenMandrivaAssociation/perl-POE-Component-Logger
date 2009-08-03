%define upstream_name    POE-Component-Logger
%define upstream_version 1.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-Log-Dispatch-Config >= 0.100.0
BuildRequires:  perl-POE >= 0.110.0
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

Requires: 	perl-POE >= 0.11
Requires:   perl-Log-Dispatch-Config >= 0.10

%description 
%{upstream_name} module for perl.  A highly flexible logger component
for POE that uses Log::Dispatch and Log::Dispatch::Config for
ultimate flexibility and power.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
