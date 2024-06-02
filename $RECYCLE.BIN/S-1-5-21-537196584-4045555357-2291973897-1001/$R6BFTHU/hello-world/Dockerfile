FROM osrf/ros:humble

RUN apt-get update && apt-get install -y nano && rm -rf /var/lib/apt/lists/*

ARG USERNAME=ros
ARG USER_UID=1000
ARG USER_GID=$USER_UID


#NON ROOT USER
RUN groupadd --gid $USER_GID --gid $USERNAME \
 && useradd -s /bin/bash --uid $USER_ID --gid $USER_GID -m $USERNAME \
 && MKDIR /HOME/$USERNAME/.config && chown &USER_UID:$USER_GID