Summary:	A library to aid daemonizing ruby programs
Name:		ruby-daemons
Version:	1.0.7
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/daemons-%{version}.gem
# Source0-md5:	33d0e02514281f7f29b19a594382fc61
#Patch0: %{name}-nogems.patch
URL:		http://daemons.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Daemons provides an easy way to wrap existing ruby scripts (for
example a self-written server) to be run as a daemon and to be
controlled by simple start/stop/restart commands.

If you want, you can also use daemons to run blocks of ruby code in a
daemon process and to control these processes from the main
application.

Besides this basic functionality, daemons offers many advanced
features like exception backtracing and logging (in case your ruby
script crashes) and monitoring and automatic restarting of your
processes if they crash.

Daemons includes the daemonize.rb script written by Travis Whitton to
do the daemonization process.


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
