Summary:	A library to aid daemonizing Ruby programs
Summary(pl.UTF-8):	Biblioteka pomagająca w demonizacji programów w Rubym
Name:		ruby-daemons
Version:	1.0.10
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/daemons-%{version}.gem
# Source0-md5:	8e2fc7de08405b2d27ac96c82602c9ce
#Patch0: %{name}-nogems.patch
URL:		http://daemons.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
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

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
#%patch0 -p1
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/daemons.rb
%{ruby_rubylibdir}/daemons
%{ruby_ridir}/Daemonize
%{ruby_ridir}/Daemons
