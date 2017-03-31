Name     : apache-maven
Version  : 3.3.9
Release  : 12
URL      : http://mirrors.gigenet.com/apache/maven/maven-3/3.3.9/source/apache-maven-3.3.9-src.tar.gz
Source0  : http://mirrors.gigenet.com/apache/maven/maven-3/3.3.9/source/apache-maven-3.3.9-src.tar.gz
Source1  : maven-script
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires: apache-ant
BuildRequires: apache-maven
BuildRequires: apache-maven
BuildRequires: apache-maven2
BuildRequires: javapackages-tools
BuildRequires: jdk-aether
BuildRequires: jdk-aopalliance
BuildRequires: jdk-apache-parent
BuildRequires: jdk-apache-resource-bundles
BuildRequires: jdk-atinject
BuildRequires: jdk-base64coder
BuildRequires: jdk-bsh
BuildRequires: jdk-buildnumber-maven-plugin
BuildRequires: jdk-cdi-api
BuildRequires: jdk-cglib
BuildRequires: jdk-commons-cli
BuildRequires: jdk-commons-codec
BuildRequires: jdk-commons-collections
BuildRequires: jdk-commons-compress
BuildRequires: jdk-commons-io
BuildRequires: jdk-commons-jxpath
BuildRequires: jdk-commons-lang
BuildRequires: jdk-commons-lang3
BuildRequires: jdk-commons-logging
BuildRequires: jdk-doxia
BuildRequires: jdk-doxia-integration-tools
BuildRequires: jdk-doxia-sitetools
BuildRequires: jdk-easymock3
BuildRequires: jdk-enforcer
BuildRequires: jdk-enforcer
BuildRequires: jdk-file-management
BuildRequires: jdk-glassfish-servlet-api
BuildRequires: jdk-gossip
BuildRequires: jdk-guava
BuildRequires: jdk-guice
BuildRequires: jdk-hamcrest
BuildRequires: jdk-hamcrest
BuildRequires: jdk-httpcomponents-client
BuildRequires: jdk-httpcomponents-core
BuildRequires: jdk-jackson-annotations
BuildRequires: jdk-jackson-core
BuildRequires: jdk-jackson-databind
BuildRequires: jdk-jansi
BuildRequires: jdk-jdom
BuildRequires: jdk-jetty
BuildRequires: jdk-jna
BuildRequires: jdk-jsoup
BuildRequires: jdk-jsr-305
BuildRequires: jdk-junit4
BuildRequires: jdk-junit4
BuildRequires: jdk-log4j
BuildRequires: jdk-logback
BuildRequires: jdk-maven-archiver
BuildRequires: jdk-maven-artifact-resolver
BuildRequires: jdk-maven-assembly-plugin
BuildRequires: jdk-maven-checkstyle-plugin
BuildRequires: jdk-maven-common-artifact-filters
BuildRequires: jdk-maven-compiler-plugin
BuildRequires: jdk-maven-dependency-tree
BuildRequires: jdk-maven-filtering
BuildRequires: jdk-maven-install-plugin
BuildRequires: jdk-maven-invoker
BuildRequires: jdk-maven-jar-plugin
BuildRequires: jdk-maven-javadoc-plugin
BuildRequires: jdk-maven-javadoc-plugin
BuildRequires: jdk-maven-parent
BuildRequires: jdk-maven-parent
BuildRequires: jdk-maven-plugin-testing
BuildRequires: jdk-maven-plugin-tools
BuildRequires: jdk-maven-remote-resources-plugin
BuildRequires: jdk-maven-reporting-api
BuildRequires: jdk-maven-reporting-exec
BuildRequires: jdk-maven-repository-builder
BuildRequires: jdk-maven-resources-plugin
BuildRequires: jdk-maven-scm
BuildRequires: jdk-maven-shared-incremental
BuildRequires: jdk-maven-shared-io
BuildRequires: jdk-maven-shared-utils
BuildRequires: jdk-maven-site-plugin
BuildRequires: jdk-maven-site-plugin
BuildRequires: jdk-mockito
BuildRequires: jdk-modello
BuildRequires: jdk-objectweb-asm
BuildRequires: jdk-parboiled
BuildRequires: jdk-pegdown
BuildRequires: jdk-plexus-archiver
BuildRequires: jdk-plexus-build-api
BuildRequires: jdk-plexus-cipher
BuildRequires: jdk-plexus-classworlds
BuildRequires: jdk-plexus-classworlds
BuildRequires: jdk-plexus-cli
BuildRequires: jdk-plexus-compiler
BuildRequires: jdk-plexus-containers
BuildRequires: jdk-plexus-i18n
BuildRequires: jdk-plexus-interactivity
BuildRequires: jdk-plexus-interpolation
BuildRequires: jdk-plexus-io
BuildRequires: jdk-plexus-resources
BuildRequires: jdk-plexus-sec-dispatcher
BuildRequires: jdk-plexus-utils
BuildRequires: jdk-plexus-velocity
BuildRequires: jdk-qdox
BuildRequires: jdk-sisu
BuildRequires: jdk-sisu-mojos
BuildRequires: jdk-slf4j
BuildRequires: jdk-snakeyaml
BuildRequires: jdk-snappy-java
BuildRequires: jdk-surefire
BuildRequires: jdk-velocity
BuildRequires: jdk-wagon
BuildRequires: jdk-xbean
BuildRequires: jdk-xmlunit
BuildRequires: jdk-xmlunit
BuildRequires: lxml
BuildRequires: maven-dep
BuildRequires: openjdk-dev
BuildRequires: python3
BuildRequires: six
BuildRequires: xmvn

%description
# Maven
Maven is available under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt)

%prep
%setup -q -n apache-maven-3.3.9

# Issue https://issues.apache.org/jira/browse/MRRESOURCES-72
rm apache-maven/src/main/appended-resources/META-INF/LICENSE.vm

%build
mkdir %{buildroot}
cp -r /usr/share/apache-maven/.m2 %{buildroot}/.m2
mvn install -Dmaven.repo.local=%{buildroot}/.m2/repository

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/apache-maven
tar -xf apache-maven/target/apache-maven-3.3.9-bin.tar.gz -C %{buildroot}/usr/share/apache-maven --strip-components=1

# Add helper scripts
mkdir -p %{buildroot}/usr/bin
for cmd in mvnDebug mvnyjp; do
    sed s/@@CMD@@/$cmd/ %{SOURCE1} >%{buildroot}/usr/bin/$cmd
    chmod +x %{buildroot}/usr/bin/$cmd
done

sed s/@@CMD@@/mvn/ %{SOURCE1} >%{buildroot}/usr/share/apache-maven/bin/mvn-script
ln -sf ../share/apache-maven/bin/mvn-script %{buildroot}/usr/bin/mvn
chmod +x %{buildroot}/usr/share/apache-maven/bin/mvn-script

%files
%defattr(-,root,root,-)
/usr/bin/mvn
/usr/bin/mvnDebug
/usr/bin/mvnyjp
/usr/share/apache-maven/LICENSE
/usr/share/apache-maven/NOTICE
/usr/share/apache-maven/README.txt
/usr/share/apache-maven/bin/m2.conf
/usr/share/apache-maven/bin/mvn
/usr/share/apache-maven/bin/mvn-script
/usr/share/apache-maven/bin/mvn.cmd
/usr/share/apache-maven/bin/mvnDebug
/usr/share/apache-maven/bin/mvnDebug.cmd
/usr/share/apache-maven/bin/mvnyjp
/usr/share/apache-maven/boot/plexus-classworlds-2.5.2.jar
/usr/share/apache-maven/conf/logging/simplelogger.properties
/usr/share/apache-maven/conf/settings.xml
/usr/share/apache-maven/conf/toolchains.xml
/usr/share/apache-maven/lib/aether-api-1.0.2.v20150114.jar
/usr/share/apache-maven/lib/aether-connector-basic-1.0.2.v20150114.jar
/usr/share/apache-maven/lib/aether-impl-1.0.2.v20150114.jar
/usr/share/apache-maven/lib/aether-spi-1.0.2.v20150114.jar
/usr/share/apache-maven/lib/aether-transport-wagon-1.0.2.v20150114.jar
/usr/share/apache-maven/lib/aether-util-1.0.2.v20150114.jar
/usr/share/apache-maven/lib/aopalliance-1.0.jar
/usr/share/apache-maven/lib/cdi-api-1.0.jar
/usr/share/apache-maven/lib/commons-cli-1.2.jar
/usr/share/apache-maven/lib/commons-io-2.2.jar
/usr/share/apache-maven/lib/commons-lang-2.6.jar
/usr/share/apache-maven/lib/commons-lang3-3.4.jar
/usr/share/apache-maven/lib/ext/README.txt
/usr/share/apache-maven/lib/guava-18.0.jar
/usr/share/apache-maven/lib/guice-4.0-no_aop.jar
/usr/share/apache-maven/lib/javax.inject-1.jar
/usr/share/apache-maven/lib/jsoup-1.7.2.jar
/usr/share/apache-maven/lib/jsr250-api-1.0.jar
/usr/share/apache-maven/lib/maven-aether-provider-3.3.9.jar
/usr/share/apache-maven/lib/maven-artifact-3.3.9.jar
/usr/share/apache-maven/lib/maven-builder-support-3.3.9.jar
/usr/share/apache-maven/lib/maven-compat-3.3.9.jar
/usr/share/apache-maven/lib/maven-core-3.3.9.jar
/usr/share/apache-maven/lib/maven-embedder-3.3.9.jar
/usr/share/apache-maven/lib/maven-model-3.3.9.jar
/usr/share/apache-maven/lib/maven-model-builder-3.3.9.jar
/usr/share/apache-maven/lib/maven-plugin-api-3.3.9.jar
/usr/share/apache-maven/lib/maven-repository-metadata-3.3.9.jar
/usr/share/apache-maven/lib/maven-settings-3.3.9.jar
/usr/share/apache-maven/lib/maven-settings-builder-3.3.9.jar
/usr/share/apache-maven/lib/org.eclipse.sisu.inject-0.3.2.jar
/usr/share/apache-maven/lib/org.eclipse.sisu.plexus-0.3.2.jar
/usr/share/apache-maven/lib/plexus-cipher-1.7.jar
/usr/share/apache-maven/lib/plexus-component-annotations-1.6.jar
/usr/share/apache-maven/lib/plexus-interpolation-1.21.jar
/usr/share/apache-maven/lib/plexus-sec-dispatcher-1.3.jar
/usr/share/apache-maven/lib/plexus-utils-3.0.22.jar
/usr/share/apache-maven/lib/slf4j-api-1.7.5.jar
/usr/share/apache-maven/lib/slf4j-simple-1.7.5.jar
/usr/share/apache-maven/lib/wagon-file-2.10.jar
/usr/share/apache-maven/lib/wagon-http-2.10-shaded.jar
/usr/share/apache-maven/lib/wagon-http-shared-2.10.jar
/usr/share/apache-maven/lib/wagon-provider-api-2.10.jar
