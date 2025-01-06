@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem
@rem SPDX-License-Identifier: Apache-2.0
@rem

@if "%DEBUG%"=="" @echo off
@rem ##########################################################################
@rem
@rem  PaperWish startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%"=="" set DIRNAME=.
@rem This is normally unused
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%..

@rem Resolve any "." and ".." in APP_HOME to make it shorter.
for %%i in ("%APP_HOME%") do set APP_HOME=%%~fi

@rem Add default JVM options here. You can also use JAVA_OPTS and PAPER_WISH_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if %ERRORLEVEL% equ 0 goto execute

echo. 1>&2
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH. 1>&2
echo. 1>&2
echo Please set the JAVA_HOME variable in your environment to match the 1>&2
echo location of your Java installation. 1>&2

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto execute

echo. 1>&2
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME% 1>&2
echo. 1>&2
echo Please set the JAVA_HOME variable in your environment to match the 1>&2
echo location of your Java installation. 1>&2

goto fail

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\lib\PaperWish.jar;%APP_HOME%\lib\camel-core-3.11.0.jar;%APP_HOME%\lib\camel-http-3.11.0.jar;%APP_HOME%\lib\camel-file-3.11.0.jar;%APP_HOME%\lib\camel-jackson-3.11.0.jar;%APP_HOME%\lib\slf4j-simple-1.7.36.jar;%APP_HOME%\lib\camel-core-languages-3.11.0.jar;%APP_HOME%\lib\camel-cluster-3.11.0.jar;%APP_HOME%\lib\camel-health-3.11.0.jar;%APP_HOME%\lib\camel-xml-jaxb-3.11.0.jar;%APP_HOME%\lib\camel-core-engine-3.11.0.jar;%APP_HOME%\lib\camel-bean-3.11.0.jar;%APP_HOME%\lib\camel-browse-3.11.0.jar;%APP_HOME%\lib\camel-controlbus-3.11.0.jar;%APP_HOME%\lib\camel-dataformat-3.11.0.jar;%APP_HOME%\lib\camel-direct-3.11.0.jar;%APP_HOME%\lib\camel-directvm-3.11.0.jar;%APP_HOME%\lib\camel-language-3.11.0.jar;%APP_HOME%\lib\camel-log-3.11.0.jar;%APP_HOME%\lib\camel-dataset-3.11.0.jar;%APP_HOME%\lib\camel-mock-3.11.0.jar;%APP_HOME%\lib\camel-ref-3.11.0.jar;%APP_HOME%\lib\camel-rest-3.11.0.jar;%APP_HOME%\lib\camel-saga-3.11.0.jar;%APP_HOME%\lib\camel-scheduler-3.11.0.jar;%APP_HOME%\lib\camel-stub-3.11.0.jar;%APP_HOME%\lib\camel-vm-3.11.0.jar;%APP_HOME%\lib\camel-seda-3.11.0.jar;%APP_HOME%\lib\camel-timer-3.11.0.jar;%APP_HOME%\lib\camel-validator-3.11.0.jar;%APP_HOME%\lib\camel-xpath-3.11.0.jar;%APP_HOME%\lib\camel-xslt-3.11.0.jar;%APP_HOME%\lib\camel-xml-jaxp-3.11.0.jar;%APP_HOME%\lib\camel-http-common-3.11.0.jar;%APP_HOME%\lib\camel-core-reifier-3.11.0.jar;%APP_HOME%\lib\camel-cloud-3.11.0.jar;%APP_HOME%\lib\camel-core-model-3.11.0.jar;%APP_HOME%\lib\camel-http-base-3.11.0.jar;%APP_HOME%\lib\camel-attachments-3.11.0.jar;%APP_HOME%\lib\camel-base-engine-3.11.0.jar;%APP_HOME%\lib\camel-base-3.11.0.jar;%APP_HOME%\lib\camel-core-processor-3.11.0.jar;%APP_HOME%\lib\camel-support-3.11.0.jar;%APP_HOME%\lib\camel-api-3.11.0.jar;%APP_HOME%\lib\camel-management-api-3.11.0.jar;%APP_HOME%\lib\camel-util-3.11.0.jar;%APP_HOME%\lib\camel-xml-io-util-3.11.0.jar;%APP_HOME%\lib\slf4j-api-1.7.36.jar;%APP_HOME%\lib\javax.servlet-api-3.1.0.jar;%APP_HOME%\lib\httpclient-4.5.13.jar;%APP_HOME%\lib\jackson-annotations-2.12.3.jar;%APP_HOME%\lib\jackson-core-2.12.3.jar;%APP_HOME%\lib\jackson-databind-2.12.3.jar;%APP_HOME%\lib\camel-tooling-model-3.11.0.jar;%APP_HOME%\lib\jaxb-impl-2.3.3.jar;%APP_HOME%\lib\jakarta.xml.bind-api-2.3.3.jar;%APP_HOME%\lib\jaxb-core-2.3.0.jar;%APP_HOME%\lib\httpcore-4.4.13.jar;%APP_HOME%\lib\commons-logging-1.2.jar;%APP_HOME%\lib\commons-codec-1.11.jar;%APP_HOME%\lib\camel-util-json-3.11.0.jar;%APP_HOME%\lib\jakarta.activation-api-1.2.2.jar;%APP_HOME%\lib\jakarta.activation-1.2.2.jar;%APP_HOME%\lib\javax.activation-1.2.0.jar


@rem Execute PaperWish
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %PAPER_WISH_OPTS%  -classpath "%CLASSPATH%" com.example.XmasWishesRoute %*

:end
@rem End local scope for the variables with windows NT shell
if %ERRORLEVEL% equ 0 goto mainEnd

:fail
rem Set variable PAPER_WISH_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
set EXIT_CODE=%ERRORLEVEL%
if %EXIT_CODE% equ 0 set EXIT_CODE=1
if not ""=="%PAPER_WISH_EXIT_CONSOLE%" exit %EXIT_CODE%
exit /b %EXIT_CODE%

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
