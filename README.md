# AvalancheDesktop
Desktop GUI and serial communication with STM32

### 1.Project Description
A basic GUI for visualizing data passed through the serial interface of an STM32 nucleo. Simple commands as start/stop recording and save data to a file located on the PC.



### 2.Run issues
## Ubuntu
#1. Permission denied for the used port by STM32
sudo usermod -a -G dialout your_user_name
