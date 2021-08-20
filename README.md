Jetson
======

[TOC]

## Install os & Jetpack 
0. Prepare Host pc (Ubuntu 16.04, 18.04 and 20.04 on x86_64 system ,CentOS 7.6, 8.0 and 8.2 on x86_64 system)
1. Install NVIDIA-SDK-Manager(https://developer.nvidia.com/nvidia-sdk-manager)
2. Connect jetson and Host pc 
3. Put Jetson into Force Recovery Mode
4. Follow SDK Manager's steps

## apt update and install pip3
```shell
sudo apt-get update
sudo apt-get install python3-pip
```

## Install Jetson-stats
This package has useful commands. [Instruction](https://github.com/rbonghi/jetson_stats)
```shell
sudo -H pip3 install -U jetson-stats
```

You can use ``jtop`` to change the power mode or monitor CPU, GPU, RAM.


## Install Libraries for pytorch
```shell
# install torch-1.9.0
wget https://nvidia.box.com/shared/static/h1z9sw4bb1ybi0rm3tu8qdj8hs05ljbm.whl -O torch-1.9.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get install python3-pip libopenblas-base libopenmpi-dev 
pip3 install Cython
pip3 install numpy torch-1.9.0-cp36-cp36m-linux_aarch64.whl

# install torchvision
pip3 install torchvision
```



## Mounting Swap
Unless you are on AGX Xavier, you should mount 4GB of swap space. as training uses up a lot of memory. Follow [this link](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-transfer-learning.md#mounting-swap).
