FROM ubuntu:18.04

# Prerequisites
RUN apt update && apt install -y curl git unzip xz-utils zip libglu1-mesa openjdk-8-jdk wget

# Setup new user
#RUN useradd -ms /bin/bash developer
#USER developer
#WORKDIR /home/developer

WORKDIR /frontend/


# Prepare Android directories and system variables
RUN mkdir -p Android/Sdk
#ENV ANDROID_SDK_ROOT /home/developer/Android/Sdk
ENV ANDROID_SDK_ROOT /frontend/Android/Sdk
RUN mkdir -p .android && touch .android/repositories.cfg

# Setup Android SDK
RUN wget -O sdk-tools.zip https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip
RUN unzip sdk-tools.zip && rm sdk-tools.zip
RUN mv tools Android/Sdk/tools
RUN cd Android/Sdk/tools/bin && yes | ./sdkmanager --licenses
RUN cd Android/Sdk/tools/bin && ./sdkmanager "build-tools;29.0.2" "patcher;v4" "platform-tools" "platforms;android-29" "sources;android-29"

#TODO ADD ADROID SDK TO ENV'S PATH

# Download Flutter SDK
ENV FLUTTER_ROOT="/frontend/flutter"
RUN git clone https://github.com/flutter/flutter.git
#ENV PATH "$PATH:/home/developer/flutter/bin"
ENV PATH="${FLUTTER_ROOT}/bin:${PATH}"

# Run basic check to download Dark SDK
RUN flutter channel beta
RUN flutter upgrade
RUN flutter config --enable-web

#WORKDIR /home/developer
#ADD . /home/developer
WORKDIR /frontend/
ADD . /frontend/
#RUN flutter pub get
#RUN flutter packages pub global activate webdev
#RUN flutter packages pub global run webdev serve
#ENTRYPOINT ['/frontend/']
#CMD echo PATH
#CMD flutter run -d chrome
#RUN flutter run -d chrome
#RUN flutter doctor