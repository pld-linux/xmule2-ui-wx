Summary:	xMule2 New Generation
Summary(pl):	xMule2 Nowa Generacja
Name:		xmule2-ui-wx
Version:	0.1.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xmule2/%{name}-%{version}-src.tar.gz
# Source0-md5:	96c0f70551fc9383250a2c20efc01f73
Patch0:		%{name}-makefile.patch
URL:		http://xmule2.sf.net
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRequires:  gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xMule2 is a Linux port of eMule client.

%description -l pl
xMule2 to linuksowy port klienta eMule.

%prep
%setup -q -n %{name}

%patch0 -p1 

%build
cd src

%{__make} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc Changelog TODO
%attr(755,root,root) %{_bindir}/*
