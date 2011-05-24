Summary:	Sup is a console-based email client for people with a lot of email
Summary(hu.UTF-8):	Sup egy konzolos email kliens azoknak, akiknek sok emailjük van
Name:		sup
Version:	0.12.1
Release:	0.1
License:	GPL v2
Source0:	http://rubyforge.org/frs/download.php/74067/%{name}-%{version}.tgz
# Source0-md5:	a16f5511900ef4e6daccfdc78fc9c1db
Group:		Applications/Mail
URL:		http://sup.rubyforge.org/
Patch0:		%{name}-locale.patch
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-Ncurses
Requires:	ruby-RubyGems
Requires:	ruby-ferret
Requires:	ruby-gettext
Requires:	ruby-highline
Requires:	ruby-lockfile
Requires:	ruby-mime-types
Requires:	ruby-net-ssh
Requires:	ruby-rmail
Requires:	ruby-trollop
Requires:	ruby-xapian
Suggests:	gnupg
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

%prep
%setup -q
# %patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{_bindir}}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS History.txt ReleaseNotes README.txt
%attr(755,root,root) %{_bindir}/sup
%attr(755,root,root) %{_bindir}/sup-add
%attr(755,root,root) %{_bindir}/sup-cmd
%attr(755,root,root) %{_bindir}/sup-config
%attr(755,root,root) %{_bindir}/sup-dump
%attr(755,root,root) %{_bindir}/sup-import-dump
%attr(755,root,root) %{_bindir}/sup-recover-sources
%attr(755,root,root) %{_bindir}/sup-server
%attr(755,root,root) %{_bindir}/sup-sync
%attr(755,root,root) %{_bindir}/sup-sync-back
%attr(755,root,root) %{_bindir}/sup-tweak-labels
%{ruby_rubylibdir}
