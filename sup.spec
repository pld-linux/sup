Summary:	Sup is a console-based email client for people with a lot of email
Summary(hu.UTF-8):	Sup egy konzolos email kliens azoknak, akiknek sok emailjük van
Name:		sup
Version:	0.6
Release:	0.1
License:	GPL v2
Source0:	http://rubyforge.org/frs/download.php/40736/%{name}-%{version}.tgz
# Source0-md5:	322d3d1c57ac46b342bde2b0342f5c27
Group:		Applications/Mail
URL:		http://sup.rubyforge.org/
Patch0:		%{name}-locale.patch
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-Ncurses
Requires:	ruby-ferret
Requires:	ruby-highline
Requires:	ruby-lockfile
Requires:	ruby-mail
Requires:	ruby-mime-types
Requires:	ruby-net-ssh
Requires:	ruby-trollop
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Sup is a console-based email client for people with a lot of email. It
supports tagging, very fast full-text search, automatic contact- list
management, and more.

%description -l hu.UTF-8
Sup egy konzolos email kliens azoknak, akiknek sok emailjük van.
Támogatja a cimkézést, nagy gyors szövegkeresővel és automatikus
kapcsolat-listával rendelkezés, sőt, még többel.

%package rdoc
Summary:	Documentation files for sup email client
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for sup email client

%prep
%setup -q
%patch0 -p1

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir},%{_bindir}}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}
%doc CONTRIBUTORS HACKING History.txt ReleaseNotes README.txt doc/FAQ.txt doc/Hooks.txt doc/NewUserGuide.txt doc/Philosophy.txt
%attr(755,root,root) %{_bindir}/sup
%attr(755,root,root) %{_bindir}/sup-add
%attr(755,root,root) %{_bindir}/sup-config
%attr(755,root,root) %{_bindir}/sup-dump
%attr(755,root,root) %{_bindir}/sup-recover-sources
%attr(755,root,root) %{_bindir}/sup-sync
%attr(755,root,root) %{_bindir}/sup-sync-back
%attr(755,root,root) %{_bindir}/sup-tweak-labels


%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}
