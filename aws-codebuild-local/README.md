## AWS CodeBuild Local Builds

Locally test and debug your AWS CodeBuild builds using the new CodeBuild local agent

## Authenticate to the public.ecr.aws repo

```
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
```

## Get the build image

Start by pulling the signed local agent image from [public ECR](https://gallery.ecr.aws/codebuild/local-builds):

For x86_64: `docker pull public.ecr.aws/codebuild/local-builds:latest`

For ARM: `docker pull public.ecr.aws/codebuild/local-builds:aarch64`

## Run the CodeBuild agent

To run the CodeBuild agent

1. Change to the directory that contains your build project source.
2. Download the codebuild_build.sh script:

```
$ curl -O  https://raw.githubusercontent.com/aws/aws-codebuild-docker-images/
master/local_builds/codebuild_build.sh
$ chmod +x codebuild_build.sh
```

3. Run the codebuild_build.sh script and specify your container image and the output
   directory.

   To run an x86_64 build, run the following command:

```
./codebuild_build.sh -i <container-image> -a <output directory>
```

    To run an ARM build, run the following command:

```
./codebuild_build.sh -i <container-image> -a <output directory> -l public.ecr.aws/codebuild/local-builds:aarch64
```

Replace `<container-image>` with the name of the container image, such as aws/
codebuild/standard:5.0 or public.ecr.aws/codebuild/amazonlinux2-x86_64-
standard:4.0.
The script launches the build image and runs the build on the project in the current directory.
To specify the location of the build project, add the -s `<build project directory>`
option to the script command.

**Required:**

* `-i`        Used to specify the customer build container image.
* `-a`        Used to specify an artifact output directory.

**Optional:**

* `-l`        Used to override the default local agent image. Default is "public.ecr.aws/codebuild/local-builds:latest"
* `-r`        Used to specify a report output directory.
* `-c`        Use the AWS configuration and credentials
  from your local host. This includes ~/.aws and any AWS_* environment
  variables.
* `-p`        Used to specify the AWS CLI Profile.
* `-b`        Used to specify a buildspec override file. Defaults to buildspec.yml in the source directory.
* `-e`        Used to specify a file containing environment variables.
* `-m`        Used to mount the source directory to the customer build container directly.
* `-d`        Used to run the build container in docker privileged mode.
* `-s`        Used to specify a source directory. Defaults to the current working directory.
  * First `-s` is for primary source
  * Use additional `-s` in `<sourceIdentifier>:<sourceLocation>` format for secondary source
  * For `sourceIdentifier`, use a value that is fewer than 128 characters and contains only alphanumeric characters and underscores

**Environment variable file format:**

* Expects each line to be in VAR=VAL format
* Lines beginning with # are processed as comments and ignored
* Blank lines are ignored
* File can be of type .env or .txt
* There is no special handling of quotation marks, meaning they will be part of the VAL

## Full Example

./codebuild_build.sh -i ./codebuild_build.sh -i public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0  -a . -l public.ecr.aws/codebuild/local-builds:aarch64 -a . -l public.ecr.aws/codebuild/local-builds:aarch64

Ouput:

```
r.cunningham@a3dlinks-MacBook-Pro aws-codebuild-local % ./codebuild_build.sh -i public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0  -a . -l public.ecr.aws/codebuild/local-builds:aarch64
Build Command:

docker run -it -v /var/run/docker.sock:/var/run/docker.sock -e "IMAGE_NAME=public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0" -e "ARTIFACTS=/Users/r.cunningham/repos/personal/aws-codebuild-local/." -e "SOURCE=/Users/r.cunningham/repos/personal/aws-codebuild-local" -e "LOCAL_AGENT_IMAGE_NAME=public.ecr.aws/codebuild/local-builds:aarch64" -e "INITIATOR=r.cunningham" public.ecr.aws/codebuild/local-builds:aarch64

Removing network agent-resources_default
Removing volume agent-resources_source_volume
Removing volume agent-resources_user_volume
Creating network "agent-resources_default" with the default driver
Creating volume "agent-resources_source_volume" with local driver
Creating volume "agent-resources_user_volume" with local driver
Creating agent-resources_agent_1 ... done
Creating agent-resources_build_1 ... done
Attaching to agent-resources_agent_1, agent-resources_build_1
agent_1  | [Container] 2024/02/19 11:48:34 Waiting for agent ping
agent_1  | [Container] 2024/02/19 11:48:35 Waiting for DOWNLOAD_SOURCE
agent_1  | [Container] 2024/02/19 11:48:36 Phase is DOWNLOAD_SOURCE
agent_1  | [Container] 2024/02/19 11:48:36 CODEBUILD_SRC_DIR=/codebuild/output/src348178247/src
agent_1  | [Container] 2024/02/19 11:48:36 YAML location is /codebuild/output/srcDownload/src/buildspec.yml
agent_1  | [Container] 2024/02/19 11:48:36 Processing environment variables
agent_1  | [Container] 2024/02/19 11:48:37 Moving to directory /codebuild/output/src348178247/src
agent_1  | [Container] 2024/02/19 11:48:37 Registering with agent
agent_1  | [Container] 2024/02/19 11:48:37 Phases found in YAML: 1
agent_1  | [Container] 2024/02/19 11:48:37  BUILD: 4 commands
agent_1  | [Container] 2024/02/19 11:48:37 Phase complete: DOWNLOAD_SOURCE State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:48:37 Phase context status code:  Message: 
agent_1  | [Container] 2024/02/19 11:48:37 Entering phase INSTALL
agent_1  | [Container] 2024/02/19 11:48:37 Phase complete: INSTALL State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:48:37 Phase context status code:  Message: 
agent_1  | [Container] 2024/02/19 11:48:37 Entering phase PRE_BUILD
agent_1  | [Container] 2024/02/19 11:48:37 Phase complete: PRE_BUILD State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:48:37 Phase context status code:  Message: 
agent_1  | [Container] 2024/02/19 11:48:37 Entering phase BUILD
agent_1  | [Container] 2024/02/19 11:48:37 Running command env
agent_1  | _=/usr/bin/env
agent_1  | JAVA_17_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | CODEBUILD_START_TIME=1708343314808
agent_1  | DOCKER_COMPOSE_VERSION=1.29.2
agent_1  | CODEBUILD_LAST_EXIT=0
agent_1  | ANT_VERSION=1.10.13
agent_1  | GOENV_DISABLE_GOPATH=1
agent_1  | RBENV_SRC_DIR=/usr/local/rbenv
agent_1  | DOCKER_VERSION=20.10.24
agent_1  | GRADLE_PATH=/gradle
agent_1  | GOPATH=/go:/codebuild/output/src348178247
agent_1  | CODEBUILD_SRC_DIR=/codebuild/output/src348178247/src
agent_1  | DOCKER_SHA256=AB91092320A87691A1EAF0225B48585DB9C69CFF0ED4B0F569F744FF765515E3
agent_1  | RUBY_BUILD_SRC_DIR=/usr/local/rbenv/plugins/ruby-build
agent_1  | MAVEN_DOWNLOAD_SHA512=4810523ba025104106567d8a15a8aa19db35068c8c8be19e30b219a1d7e83bcab96124bf86dc424b1cd3c5edba25d69ec0b31751c136f88975d15406cab3842b
agent_1  | CODEBUILD_LOCAL_BUILD=true
agent_1  | CODEBUILD_INITIATOR=r.cunningham
agent_1  | HOME=/root
agent_1  | JDK_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | SHLVL=2
agent_1  | CODEBUILD_BUILD_ID=local:00000000-0000-0000-0000-000000000000
agent_1  | CODEBUILD_AGENT_PORT=http://BMR:3000
agent_1  | RUBY_31_VERSION=3.1.4
agent_1  | JRE_17_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | CODEBUILD_AGENT_ENDPOINT=http://BMR:3000
agent_1  | PYTHON_PIP_VERSION=21.3.1
agent_1  | CODEBUILD_BUILD_ARN=arn:aws:codebuild:us-east-1:000000000000:build/local:00000000-0000-0000-0000-000000000000
agent_1  | AWS_REGION=us-east-1
agent_1  | PHP_81_VERSION=8.1.20
agent_1  | DOTNET_60_SDK_VERSION=6.0.418
agent_1  | GRADLE_DOWNLOADS_SHA256=5861dcc093556fef71cdde8cbae9887be70a8bf40e0f5856b61181ae92dccf33 7.6.2
agent_1  | JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | CODEBUILD_BUILD_IMAGE=public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0
agent_1  | PYYAML_VERSION=5.4.1
agent_1  | DOTNET_ROOT=/root/.dotnet
agent_1  | POWERSHELL_DOWNLOAD_SHA=9D6F798461D172391B508FCF27F9CBBB4BEF307EBFD6886ED50860C322C7D1B3
agent_1  | PWD=/codebuild/output/src348178247/src
agent_1  | AWS_DEFAULT_REGION=us-east-1
agent_1  | GOLANG_18_VERSION=1.18.10
agent_1  | MAVEN_HOME=/opt/maven
agent_1  | PATH=/usr/local/bin/sbt/bin:/root/.goenv/shims:/root/.goenv/bin:/go/bin:/root/.phpenv/shims:/root/.phpenv/bin:/root/.pyenv/shims:/root/.pyenv/bin:/root/.rbenv/shims:/usr/local/rbenv/bin:/usr/local/rbenv/shims:/root/.dotnet/:/root/.dotnet/tools/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/codebuild/user/bin
agent_1  | PYTHON_39_VERSION=3.9.17
agent_1  | CODEBUILD_GOPATH=/codebuild/output/src348178247
agent_1  | NODE_16_VERSION=16.20.1
agent_1  | NUGET_XMLDOC_MODE=skip
agent_1  | MAVEN_OPTS=-Dmaven.wagon.httpconnectionManager.maxPerRoute=2
agent_1  | DIND_COMMIT=3b5fac462d21ca164b3778647420016315289034
agent_1  | DOCKER_BUCKET=download.docker.com
agent_1  | LOG4J_UNSAFE_VERSIONS=2.11.1 1.2.8
agent_1  | SBT_DOWNLOAD_SHA256=21F4210786FD68FD15DCA3F4C8EE9CAE0DB249C54E1B0EF6E829E9FA4936423A
agent_1  | POWERSHELL_DOWNLOAD_URL=https://github.com/PowerShell/PowerShell/releases/download/v7.2.11/powershell-7.2.11-linux-x64.tar.gz
agent_1  | INSTALLED_GRADLE_VERSIONS=7.6.2
agent_1  | MAVEN_VERSION=3.9.5
agent_1  | CODEBUILD_AUTH_TOKEN=12345
agent_1  | GITVERSION_VERSION=5.11.1
agent_1  | JRE_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | GRADLE_VERSION=7.6.2
agent_1  | NO_PROXY=BMR:3000
agent_1  | JDK_17_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | OLDPWD=/codebuild_docker_build
agent_1  | CODEBUILD_BUILD_SUCCEEDING=1
agent_1  | N_SRC_DIR=/n
agent_1  | DOCKER_CHANNEL=stable
agent_1  | ANT_DOWNLOAD_SHA512=de4ac604629e39a86a306f0541adb3775596909ad92feb8b7de759b1b286417db24f557228737c8b902d6abf722d2ce5bb0c3baa3640cbeec3481e15ab1958c9
agent_1  | POWERSHELL_VERSION=7.2.11
agent_1  | SBT_VERSION=1.8.3
agent_1  | HOSTNAME=333171278a93
agent_1  | 
agent_1  | [Container] 2024/02/19 11:48:37 Running command whoami
agent_1  | root
agent_1  | 
agent_1  | [Container] 2024/02/19 11:48:37 Running command echo Build started on `date`
agent_1  | Build started on Mon Feb 19 11:48:37 UTC 2024
agent_1  | 
agent_1  | [Container] 2024/02/19 11:48:37 Running command PWD
agent_1  | /codebuild/output/tmp/script.sh: line 4: PWD: command not found
agent_1  | 
agent_1  | [Container] 2024/02/19 11:48:37 Command did not exit successfully PWD exit status 127
agent_1  | [Container] 2024/02/19 11:48:37 Phase complete: BUILD State: FAILED
agent_1  | [Container] 2024/02/19 11:48:37 Phase context status code: COMMAND_EXECUTION_ERROR Message: Error while executing command: PWD. Reason: exit status 127
agent_1  | [Container] 2024/02/19 11:48:37 Entering phase POST_BUILD
agent_1  | [Container] 2024/02/19 11:48:37 Phase complete: POST_BUILD State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:48:37 Phase context status code:  Message: 
agent-resources_agent_1 exited with code 0
Stopping agent-resources_build_1 ... done
Aborting on container exit...
r.cunningham@a3dlinks-MacBook-Pro aws-codebuild-local % ./codebuild_build.sh -i public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0  -a . -l public.ecr.aws/codebuild/local-builds:aarch64
Build Command:

docker run -it -v /var/run/docker.sock:/var/run/docker.sock -e "IMAGE_NAME=public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0" -e "ARTIFACTS=/Users/r.cunningham/repos/personal/aws-codebuild-local/." -e "SOURCE=/Users/r.cunningham/repos/personal/aws-codebuild-local" -e "LOCAL_AGENT_IMAGE_NAME=public.ecr.aws/codebuild/local-builds:aarch64" -e "INITIATOR=r.cunningham" public.ecr.aws/codebuild/local-builds:aarch64

Removing agent-resources_build_1 ... done
Removing agent-resources_agent_1 ... done
Removing network agent-resources_default
Removing volume agent-resources_source_volume
Removing volume agent-resources_user_volume
Creating network "agent-resources_default" with the default driver
Creating volume "agent-resources_source_volume" with local driver
Creating volume "agent-resources_user_volume" with local driver
Creating agent-resources_agent_1 ... done
Creating agent-resources_build_1 ... done
Attaching to agent-resources_agent_1, agent-resources_build_1
agent_1  | [Container] 2024/02/19 11:48:57 Waiting for agent ping
agent_1  | [Container] 2024/02/19 11:48:58 Waiting for DOWNLOAD_SOURCE
agent_1  | [Container] 2024/02/19 11:48:59 Phase is DOWNLOAD_SOURCE
agent_1  | [Container] 2024/02/19 11:48:59 CODEBUILD_SRC_DIR=/codebuild/output/src685673091/src
agent_1  | [Container] 2024/02/19 11:48:59 YAML location is /codebuild/output/srcDownload/src/buildspec.yml
agent_1  | [Container] 2024/02/19 11:48:59 Processing environment variables
agent_1  | [Container] 2024/02/19 11:48:59 Moving to directory /codebuild/output/src685673091/src
agent_1  | [Container] 2024/02/19 11:48:59 Registering with agent
agent_1  | [Container] 2024/02/19 11:48:59 Phases found in YAML: 1
agent_1  | [Container] 2024/02/19 11:48:59  BUILD: 4 commands
agent_1  | [Container] 2024/02/19 11:48:59 Phase complete: DOWNLOAD_SOURCE State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:48:59 Phase context status code:  Message: 
agent_1  | [Container] 2024/02/19 11:48:59 Entering phase INSTALL
agent_1  | [Container] 2024/02/19 11:48:59 Phase complete: INSTALL State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:48:59 Phase context status code:  Message: 
agent_1  | [Container] 2024/02/19 11:48:59 Entering phase PRE_BUILD
agent_1  | [Container] 2024/02/19 11:48:59 Phase complete: PRE_BUILD State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:48:59 Phase context status code:  Message: 
agent_1  | [Container] 2024/02/19 11:48:59 Entering phase BUILD
agent_1  | [Container] 2024/02/19 11:48:59 Running command env
agent_1  | _=/usr/bin/env
agent_1  | JAVA_17_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | CODEBUILD_START_TIME=1708343337441
agent_1  | DOCKER_COMPOSE_VERSION=1.29.2
agent_1  | CODEBUILD_LAST_EXIT=0
agent_1  | ANT_VERSION=1.10.13
agent_1  | GOENV_DISABLE_GOPATH=1
agent_1  | RBENV_SRC_DIR=/usr/local/rbenv
agent_1  | DOCKER_VERSION=20.10.24
agent_1  | GRADLE_PATH=/gradle
agent_1  | GOPATH=/go:/codebuild/output/src685673091
agent_1  | CODEBUILD_SRC_DIR=/codebuild/output/src685673091/src
agent_1  | DOCKER_SHA256=AB91092320A87691A1EAF0225B48585DB9C69CFF0ED4B0F569F744FF765515E3
agent_1  | RUBY_BUILD_SRC_DIR=/usr/local/rbenv/plugins/ruby-build
agent_1  | MAVEN_DOWNLOAD_SHA512=4810523ba025104106567d8a15a8aa19db35068c8c8be19e30b219a1d7e83bcab96124bf86dc424b1cd3c5edba25d69ec0b31751c136f88975d15406cab3842b
agent_1  | CODEBUILD_LOCAL_BUILD=true
agent_1  | CODEBUILD_INITIATOR=r.cunningham
agent_1  | HOME=/root
agent_1  | JDK_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | SHLVL=2
agent_1  | CODEBUILD_BUILD_ID=local:00000000-0000-0000-0000-000000000000
agent_1  | CODEBUILD_AGENT_PORT=http://BMR:3000
agent_1  | RUBY_31_VERSION=3.1.4
agent_1  | JRE_17_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | CODEBUILD_AGENT_ENDPOINT=http://BMR:3000
agent_1  | PYTHON_PIP_VERSION=21.3.1
agent_1  | CODEBUILD_BUILD_ARN=arn:aws:codebuild:us-east-1:000000000000:build/local:00000000-0000-0000-0000-000000000000
agent_1  | AWS_REGION=us-east-1
agent_1  | PHP_81_VERSION=8.1.20
agent_1  | DOTNET_60_SDK_VERSION=6.0.418
agent_1  | GRADLE_DOWNLOADS_SHA256=5861dcc093556fef71cdde8cbae9887be70a8bf40e0f5856b61181ae92dccf33 7.6.2
agent_1  | JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | CODEBUILD_BUILD_IMAGE=public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0
agent_1  | PYYAML_VERSION=5.4.1
agent_1  | DOTNET_ROOT=/root/.dotnet
agent_1  | POWERSHELL_DOWNLOAD_SHA=9D6F798461D172391B508FCF27F9CBBB4BEF307EBFD6886ED50860C322C7D1B3
agent_1  | PWD=/codebuild/output/src685673091/src
agent_1  | AWS_DEFAULT_REGION=us-east-1
agent_1  | GOLANG_18_VERSION=1.18.10
agent_1  | MAVEN_HOME=/opt/maven
agent_1  | PATH=/usr/local/bin/sbt/bin:/root/.goenv/shims:/root/.goenv/bin:/go/bin:/root/.phpenv/shims:/root/.phpenv/bin:/root/.pyenv/shims:/root/.pyenv/bin:/root/.rbenv/shims:/usr/local/rbenv/bin:/usr/local/rbenv/shims:/root/.dotnet/:/root/.dotnet/tools/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/codebuild/user/bin
agent_1  | PYTHON_39_VERSION=3.9.17
agent_1  | CODEBUILD_GOPATH=/codebuild/output/src685673091
agent_1  | NODE_16_VERSION=16.20.1
agent_1  | NUGET_XMLDOC_MODE=skip
agent_1  | MAVEN_OPTS=-Dmaven.wagon.httpconnectionManager.maxPerRoute=2
agent_1  | DIND_COMMIT=3b5fac462d21ca164b3778647420016315289034
agent_1  | DOCKER_BUCKET=download.docker.com
agent_1  | LOG4J_UNSAFE_VERSIONS=2.11.1 1.2.8
agent_1  | SBT_DOWNLOAD_SHA256=21F4210786FD68FD15DCA3F4C8EE9CAE0DB249C54E1B0EF6E829E9FA4936423A
agent_1  | POWERSHELL_DOWNLOAD_URL=https://github.com/PowerShell/PowerShell/releases/download/v7.2.11/powershell-7.2.11-linux-x64.tar.gz
agent_1  | INSTALLED_GRADLE_VERSIONS=7.6.2
agent_1  | MAVEN_VERSION=3.9.5
agent_1  | CODEBUILD_AUTH_TOKEN=12345
agent_1  | GITVERSION_VERSION=5.11.1
agent_1  | JRE_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | GRADLE_VERSION=7.6.2
agent_1  | NO_PROXY=BMR:3000
agent_1  | JDK_17_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64
agent_1  | OLDPWD=/codebuild_docker_build
agent_1  | CODEBUILD_BUILD_SUCCEEDING=1
agent_1  | N_SRC_DIR=/n
agent_1  | DOCKER_CHANNEL=stable
agent_1  | ANT_DOWNLOAD_SHA512=de4ac604629e39a86a306f0541adb3775596909ad92feb8b7de759b1b286417db24f557228737c8b902d6abf722d2ce5bb0c3baa3640cbeec3481e15ab1958c9
agent_1  | POWERSHELL_VERSION=7.2.11
agent_1  | SBT_VERSION=1.8.3
agent_1  | HOSTNAME=61b5be9cf1c2
agent_1  | 
agent_1  | [Container] 2024/02/19 11:48:59 Running command whoami
agent_1  | root
agent_1  | 
agent_1  | [Container] 2024/02/19 11:48:59 Running command echo Build started on `date`
agent_1  | Build started on Mon Feb 19 11:49:00 UTC 2024
agent_1  | 
agent_1  | [Container] 2024/02/19 11:49:00 Running command pwd
agent_1  | /codebuild/output/src685673091/src
agent_1  | 
agent_1  | [Container] 2024/02/19 11:49:00 Phase complete: BUILD State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:49:00 Phase context status code:  Message: 
agent_1  | [Container] 2024/02/19 11:49:00 Entering phase POST_BUILD
agent_1  | [Container] 2024/02/19 11:49:00 Phase complete: POST_BUILD State: SUCCEEDED
agent_1  | [Container] 2024/02/19 11:49:00 Phase context status code:  Message: 
agent-resources_agent_1 exited with code 0
Stopping agent-resources_build_1 ... done
Aborting on container exit...
r.cunningham@a3dlinks-MacBook-Pro aws-codebuild-local % ./codebuild_build.sh -i public.ecr.aws/codebuild/amazonlinux2-x86_64-standard:4.0  -a . -l public.ecr.aws/codebuild/local-builds:aarch64
```
