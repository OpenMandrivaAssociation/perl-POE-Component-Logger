%define upstream_name    POE-Component-Logger
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group: 		Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Log::Dispatch::Config)
BuildRequires:	perl(POE)
BuildArch:	noarch

Requires:	perl(POE)
Requires:	perl(Log::Dispatch::Config)

%description 
%{upstream_name} module for perl.  A highly flexible logger component
for POE that uses Log::Dispatch and Log::Dispatch::Config for
ultimate flexibility and power.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
CFLAGS="%{optflags}" make PREFIX=%{_prefix}


%install
make PREFIX="%{buildroot}%{_prefix}" install

%files
%defattr(444,root,root,755)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/POE/Component


%changelog
* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 596634
- update to 1.10

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-2mdv2010.0
+ Revision: 430529
- rebuild

  + JÃ©rÃ´me Quelin <jquelin@mandriva.org>
    - rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.00-8mdv2009.0
+ Revision: 258272
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.00-7mdv2009.0
+ Revision: 246326
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.00-5mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.00-5mdv2008.0
+ Revision: 25175
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.00-4mdk
- Fix According to perl Policy
	- Source URL
	- URL
- use mkrel

* Fri Jul 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.00-3mdk
- rebuild

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-2mdk
- rebuild for new auto{prov,req}

