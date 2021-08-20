Jetson
======

[[_TOC_]]

## Install os & Jetpack 
0. Prepare Host pc (Ubuntu 16.04, 18.04 and 20.04 on x86_64 system ,CentOS 7.6, 8.0 and 8.2 on x86_64 system)
1. Install NVIDIA-SDK-Manager(https://developer.nvidia.com/nvidia-sdk-manager)
2. Connect jetson and Host pc 
3. Put Jetson into Force Recovery Mode
4. Follow SDK Manager's steps

## apt update and install pip3
```bash
sudo apt-get update
sudo apt-get install python3-pip
```

## Install Jetson-stats
This package has useful commands. [Instruction](https://github.com/rbonghi/jetson_stats)
```bash
sudo -H pip3 install -U jetson-stats
```

You can use ``jtop`` to change the power mode or monitor CPU, GPU, RAM.


## Installing pytorch on jetson
```bash
# install torch-1.9.0
wget https://nvidia.box.com/shared/static/h1z9sw4bb1ybi0rm3tu8qdj8hs05ljbm.whl -O torch-1.9.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get install python3-pip libopenblas-base libopenmpi-dev 
pip3 install Cython
pip3 install numpy torch-1.9.0-cp36-cp36m-linux_aarch64.whl
rm torch-1.9.0-cp36-cp36m-linux_aarch64.whl


# install torchvision
pip3 install torchvision
```



## Mounting Swap
Unless you are on Jetson AGX Xavier, you should mount 4GB of swap space. as training uses up a lot of memory. Run these commands on your Jetson (outside of container) to disable ZRAM and creat a swap file:

```bash 
sudo systemctl disable nvzramconfig
sudo fallocate -l 4G /mnt/4GB.swap
sudo mkswap /mnt/4GB.swap
sudo swapon /mnt/4GB.swap
```

Then add the following line to the end of ``/etc/fstab`` to make the change persistent:

``` bash
/mnt/4GB.swap  none  swap  sw 0  0
```

Now your swap file will automatically be mounted after reboots.  To check the usage, run `swapon -s` or `tegrastats`.  Disabling ZRAM (in-memory compressed swap) also free's up physical memory and requires a reboot to take effect.
[sources](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-transfer-learning.md#mounting-swap)


