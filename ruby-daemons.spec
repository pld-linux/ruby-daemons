%define pkgname daemons
Summary:	A library to aid daemonizing Ruby programs
Summary(pl.UTF-8):	Biblioteka pomagająca w demonizacji programów w Rubym
Name:		ruby-%{pkgname}
Version:	1.0.10
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/daemons-%{version}.gem
# Source0-md5:	8e2fc7de08405b2d27ac96c82602c9ce
URL:		http://daemons.rubyforge.org
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Daemons provides an easy way to wrap existing Ruby scripts (for
example a self-written server) to be run as a daemon and to be
controlled by simple start/stop/restart commands.

If you want, you can also use daemons to run blocks of Ruby code in a
daemon process and to control these processes from the main
application.

Besides this basic functionality, daemons offers many advanced
features like exception backtracing and logging (in case your Ruby
script crashes) and monitoring and automatic restarting of your
processes if they crash.

Daemons includes the daemonize.rb script written by Travis Whitton to
do the daemonization process.

%description -l pl.UTF-8
daemons udostępnia prosty sposób obudowywania istniejących skryptów w
Rubym (na przykład samodzielne napisanego serwera) w celu uruchamiania
jako demon i sterowania przez proste polecenia start/stop/restart.

Jeśli chcemy, możemy także użyć daemons do uruchamiania bloków kodu w
Rubym jako procesu demona i sterować tymi procesami z głównej
aplikacji.

Poza tą podstawową funkcjonalnością daemons oferuje także wiele
zaawansowanych możliwości, takich jak ślady wyjątków oraz logowanie (w
przypadku padu skryptu), monitorowanie i automatyczne restartowanie
procesów.

daemons zawiera skrypt daemonize.rb napisany przez Travisa Whittona,
wykonujący proces demonizacji.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/cache.ri
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/daemons.rb
%{ruby_vendorlibdir}/daemons

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Daemonize
%{ruby_ridir}/Daemons
