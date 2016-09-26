Name     : apache-maven
Version  : 3.3.9
Release  : 6
URL      : http://mirrors.gigenet.com/apache/maven/maven-3/3.3.9/source/apache-maven-3.3.9-src.tar.gz
Source0  : http://mirrors.gigenet.com/apache/maven/maven-3/3.3.9/source/apache-maven-3.3.9-src.tar.gz
Source1  : maven-script
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires: openjdk-dev
BuildRequires: apache-ant
BuildRequires: apache-maven
BuildRequires: apache-maven2
BuildRequires: xmvn
BuildRequires: python3
BuildRequires: apache-maven
BuildRequires: javapackages-tools
BuildRequires: six
BuildRequires: lxml
BuildRequires: jdk-plexus-classworlds
BuildRequires: jdk-maven-parent
BuildRequires: jdk-apache-parent
BuildRequires: jdk-maven-javadoc-plugin
BuildRequires: jdk-maven-remote-resources-plugin
BuildRequires: jdk-maven-site-plugin
BuildRequires: jdk-maven-checkstyle-plugin
BuildRequires: jdk-enforcer
BuildRequires: jdk-junit4
BuildRequires: jdk-hamcrest
BuildRequires: jdk-maven-dependency-tree
BuildRequires: jdk-plexus-utils
BuildRequires: jdk-aether
BuildRequires: jdk-aopalliance
BuildRequires: jdk-commons-cli
BuildRequires: jdk-commons-io
BuildRequires: jdk-commons-lang
BuildRequires: jdk-commons-lang3
BuildRequires: jdk-commons-codec
BuildRequires: jdk-commons-jxpath
BuildRequires: jdk-commons-logging
BuildRequires: jdk-apache-resource-bundles
BuildRequires: jdk-atinject
BuildRequires: jdk-buildnumber-maven-plugin
BuildRequires: jdk-cglib
BuildRequires: jdk-easymock3
BuildRequires: jdk-guice
BuildRequires: jdk-hamcrest
BuildRequires: jdk-httpcomponents-core
BuildRequires: jdk-httpcomponents-client
BuildRequires: jdk-jsoup
BuildRequires: jdk-jsr-305
BuildRequires: jdk-junit4
BuildRequires: jdk-maven-assembly-plugin
BuildRequires: jdk-maven-compiler-plugin
BuildRequires: jdk-enforcer
BuildRequires: jdk-maven-install-plugin
BuildRequires: jdk-maven-jar-plugin
BuildRequires: jdk-maven-javadoc-plugin
BuildRequires: jdk-maven-parent
BuildRequires: jdk-maven-resources-plugin
BuildRequires: jdk-maven-site-plugin
BuildRequires: jdk-surefire
BuildRequires: jdk-wagon
BuildRequires: jdk-objectweb-asm
BuildRequires: jdk-plexus-cipher
BuildRequires: jdk-plexus-classworlds
BuildRequires: jdk-plexus-containers
BuildRequires: jdk-plexus-interpolation
BuildRequires: jdk-plexus-sec-dispatcher
BuildRequires: jdk-sisu
BuildRequires: jdk-sisu-mojos
BuildRequires: jdk-slf4j
BuildRequires: jdk-xmlunit
BuildRequires: jdk-mockito
BuildRequires: jdk-modello
BuildRequires: jdk-gossip
BuildRequires: jdk-jansi
BuildRequires: jdk-maven-shared-utils
BuildRequires: jdk-xbean
BuildRequires: jdk-guava
BuildRequires: jdk-maven-common-artifact-filters
BuildRequires: jdk-bsh
BuildRequires: jdk-plexus-i18n
BuildRequires: jdk-maven-plugin-testing
BuildRequires: jdk-plexus-archiver
BuildRequires: jdk-plexus-io
BuildRequires: jdk-commons-compress
BuildRequires: jdk-snappy-java
BuildRequires: jdk-maven-filtering
BuildRequires: jdk-maven-artifact-resolver
BuildRequires: jdk-plexus-resources
BuildRequires: jdk-plexus-velocity
BuildRequires: jdk-velocity
BuildRequires: jdk-plexus-build-api
BuildRequires: jdk-commons-collections
BuildRequires: jdk-doxia
BuildRequires: jdk-jetty
BuildRequires: jdk-maven-archiver
BuildRequires: jdk-doxia-sitetools
BuildRequires: jdk-maven-reporting-api
BuildRequires: jdk-maven-reporting-exec
BuildRequires: jdk-xmlunit
BuildRequires: jdk-pegdown
BuildRequires: jdk-glassfish-servlet-api
BuildRequires: jdk-parboiled
BuildRequires: jdk-doxia-integration-tools
BuildRequires: jdk-jackson-core
BuildRequires: jdk-snakeyaml
BuildRequires: jdk-jackson-databind
BuildRequires: jdk-jackson-annotations
BuildRequires: jdk-base64coder
BuildRequires: jdk-maven-shared-incremental
BuildRequires: jdk-plexus-compiler
BuildRequires: jdk-maven-plugin-tools
BuildRequires: jdk-qdox
BuildRequires: jdk-jdom
BuildRequires: jdk-plexus-cli
BuildRequires: jdk-jna
BuildRequires: jdk-maven-scm
BuildRequires: jdk-logback
BuildRequires: jdk-file-management
BuildRequires: jdk-maven-shared-io
BuildRequires: jdk-maven-repository-builder
BuildRequires: jdk-log4j
BuildRequires: jdk-maven-invoker
BuildRequires: jdk-plexus-interactivity
BuildRequires: jdk-cdi-api

%description
# Maven
Maven is available under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt)

%prep
%setup -q -n apache-maven-3.3.9

# Update shell scripts to use unversioned classworlds
sed -i -e s:'-classpath "${M2_HOME}"/boot/plexus-classworlds-\*.jar':'-classpath "${M2_HOME}"/boot/plexus-classworlds.jar':g \
        apache-maven/src/bin/mvn*

# Disable QA plugins which are not useful for us
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :animal-sniffer-maven-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :apache-rat-plugin


# logback is not really needed by maven in typical use cases, so set
# its scope to provided
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject "pom:dependency[pom:artifactId='logback-classic']" "<scope>provided</scope>" maven-embedder

python3 /usr/share/java-utils/mvn_package.py :apache-maven __noinstall

%build
python3 /usr/share/java-utils/mvn_file.py ":{*}:jar:" maven/@1 /usr/share/apache-maven/lib/@1
python3 /usr/share/java-utils/mvn_build.py -f

%install
rm -rf %{buildroot}
xmvn-install  -R .xmvn-reactor -n maven -d %{buildroot}

# Uncompress tarball 
tar -xf apache-maven/target/apache-maven-3.3.9-bin.tar.gz
cp -pr apache-maven-3.3.9/lib/* %{buildroot}/usr/share/apache-maven/lib
cp -pr apache-maven-3.3.9/conf %{buildroot}/usr/share/apache-maven
cp -pr apache-maven-3.3.9/bin %{buildroot}/usr/share/apache-maven

# Install javadoc
mkdir -p %{buildroot}/usr/share/javadoc/maven
cp -pr .xmvn/apidocs/* %{buildroot}/usr/share/javadoc/maven

# Add helper scripts
mkdir -p %{buildroot}/usr/bin
for cmd in mvnDebug mvnyjp; do
    sed s/@@CMD@@/$cmd/ %{SOURCE1} >%{buildroot}/usr/bin/$cmd
    chmod +x %{buildroot}/usr/bin/$cmd
done

sed s/@@CMD@@/mvn/ %{SOURCE1} >%{buildroot}/usr/share/apache-maven/bin/mvn-script
ln -sf ../share/apache-maven/bin/mvn-script %{buildroot}/usr/bin/mvn
chmod +x %{buildroot}/usr/share/apache-maven/bin/mvn-script

# Link plexus-classworlds
mkdir -p  %{buildroot}/usr/share/apache-maven/boot/
ln -sf $(build-classpath plexus/classworlds) \
    %{buildroot}/usr/share/apache-maven/boot/plexus-classworlds.jar

%files
%defattr(-,root,root,-)
/usr/bin/mvn
/usr/bin/mvnDebug
/usr/bin/mvnyjp
/usr/share/apache-maven/bin/m2.conf
/usr/share/apache-maven/bin/mvn
/usr/share/apache-maven/bin/mvn-script
/usr/share/apache-maven/bin/mvn.cmd
/usr/share/apache-maven/bin/mvnDebug
/usr/share/apache-maven/bin/mvnDebug.cmd
/usr/share/apache-maven/bin/mvnyjp
/usr/share/apache-maven/boot/plexus-classworlds.jar
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
/usr/share/apache-maven/lib/asm-any.jar
/usr/share/apache-maven/lib/commons-cli-1.2.jar
/usr/share/apache-maven/lib/commons-io-2.2.jar
/usr/share/apache-maven/lib/commons-lang-2.6.jar
/usr/share/apache-maven/lib/commons-lang3-3.4.jar
/usr/share/apache-maven/lib/ext/README.txt
/usr/share/apache-maven/lib/guava-18.0.jar
/usr/share/apache-maven/lib/guice-4.0-no_aop.jar
/usr/share/apache-maven/lib/javax.inject-1.jar
/usr/share/apache-maven/lib/jsoup-1.7.2.jar
/usr/share/apache-maven/lib/maven-aether-provider-3.3.9.jar
/usr/share/apache-maven/lib/maven-aether-provider.jar
/usr/share/apache-maven/lib/maven-artifact-3.3.9.jar
/usr/share/apache-maven/lib/maven-artifact.jar
/usr/share/apache-maven/lib/maven-builder-support-3.3.9.jar
/usr/share/apache-maven/lib/maven-builder-support.jar
/usr/share/apache-maven/lib/maven-compat-3.3.9.jar
/usr/share/apache-maven/lib/maven-compat.jar
/usr/share/apache-maven/lib/maven-core-3.3.9.jar
/usr/share/apache-maven/lib/maven-core.jar
/usr/share/apache-maven/lib/maven-embedder-3.3.9.jar
/usr/share/apache-maven/lib/maven-embedder.jar
/usr/share/apache-maven/lib/maven-model-3.3.9.jar
/usr/share/apache-maven/lib/maven-model-builder-3.3.9.jar
/usr/share/apache-maven/lib/maven-model-builder.jar
/usr/share/apache-maven/lib/maven-model.jar
/usr/share/apache-maven/lib/maven-plugin-api-3.3.9.jar
/usr/share/apache-maven/lib/maven-plugin-api.jar
/usr/share/apache-maven/lib/maven-repository-metadata-3.3.9.jar
/usr/share/apache-maven/lib/maven-repository-metadata.jar
/usr/share/apache-maven/lib/maven-settings-3.3.9.jar
/usr/share/apache-maven/lib/maven-settings-builder-3.3.9.jar
/usr/share/apache-maven/lib/maven-settings-builder.jar
/usr/share/apache-maven/lib/maven-settings.jar
/usr/share/apache-maven/lib/org.eclipse.sisu.inject-0.3.1.jar
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
/usr/share/java/maven/maven-aether-provider.jar
/usr/share/java/maven/maven-artifact.jar
/usr/share/java/maven/maven-builder-support.jar
/usr/share/java/maven/maven-compat.jar
/usr/share/java/maven/maven-core.jar
/usr/share/java/maven/maven-embedder.jar
/usr/share/java/maven/maven-model-builder.jar
/usr/share/java/maven/maven-model.jar
/usr/share/java/maven/maven-plugin-api.jar
/usr/share/java/maven/maven-repository-metadata.jar
/usr/share/java/maven/maven-settings-builder.jar
/usr/share/java/maven/maven-settings.jar
/usr/share/javadoc/*
/usr/share/maven-metadata/maven.xml
/usr/share/maven-poms/maven/maven-aether-provider.pom
/usr/share/maven-poms/maven/maven-artifact.pom
/usr/share/maven-poms/maven/maven-builder-support.pom
/usr/share/maven-poms/maven/maven-compat.pom
/usr/share/maven-poms/maven/maven-core.pom
/usr/share/maven-poms/maven/maven-embedder.pom
/usr/share/maven-poms/maven/maven-model-builder.pom
/usr/share/maven-poms/maven/maven-model.pom
/usr/share/maven-poms/maven/maven-plugin-api.pom
/usr/share/maven-poms/maven/maven-repository-metadata.pom
/usr/share/maven-poms/maven/maven-settings-builder.pom
/usr/share/maven-poms/maven/maven-settings.pom
/usr/share/maven-poms/maven/maven.pom
