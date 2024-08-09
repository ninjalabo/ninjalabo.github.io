# Arduino sketch

This is a arduino sktech for image recognition with the help of machine learning. It has been designed to be used on the Arduino Nano 33 BLE with the OV7675 camera module.

At the moment, it can be used for binary detection, for example weather there is a person in the picture.

## Dependencies

This sketch depends on [Tensorflow lite for microcontrollers](https://www.tensorflow.org/lite/microcontrollers).

## Installing sktech to microcontoller

### Arduino-cli

First, install the required [Arduino tflite library](https://github.com/tensorflow/tflite-micro-arduino-examples). On linux, this is typically in `~/Arduino/libraries`, on MacOS in `~/Documents/Arduino/libraries` and on Windows in `My Documents\Arduino\Libraries`.

Once in this directory, download the library with

```bash
git clone https://github.com/tensorflow/tflite-micro-arduino-examples Arduino_TensorFlowLite
```

Now you can continue to installation. First, install the core library for the used arduino board.

```bash
arduino-cli core install arduino:mbed_nano
```

Next, compile the sketch.

```bash
arduino-cli compile --fqbn arduino:mbed_nano:nano33ble template/
```

Finally, install it to the device. For this, the port to which the device is connected to is required. This can be found with

```bash
arduino-cli board list
```

Check the name of the port, for example */dev/ttyACM0*. Now, install the sketch with

```bash
arduino-cli upload -p <device_port> --fqbn arduino:mbed_nano:nano33ble template/
```

### Docker

There is a provided Dockerfile which can make the installation a lot easier.

First, build the image with docker. You can give it any other tag, but this example will name it *arduino*.

```bash
docker build -t arduino .
```

The image will contain the compiled sketch and will have `arduino-cli` as its entry point. Now, just install it with

```bash
docker run arduino upload -p <device_port> --fqbn arduino_mbed_nano:nano33ble template
```

Again, if you dont no what port the device is connected to, you can use the image to find that.

```bash
docker run arduino board list
```

## Changing the model

In order to use your own tensorflow model, replace the [target_model.cpp](./template/target_model.cpp) with your own model. This is a C array generated from the wanted model. To generate the C array from a *tflite* model, `xxd` can be used:

```bash
xxd -i <your_tflite_model> > target_model.cc
```

Then, replace the the old file with this new generated file.

### Renaming the model

If you want to rename the model, you need to also change the name of the models header file [target_model.h](./template/target_model.h) to the same name and change the headerfile name in [template.ino](./template/template.ino).

:warning: NOTE! Be careful when renaming the model. For some models the model can not be named something that starts with the word *model*. For this reason, it is adviced to always name the C-array file so that it does not start with *model*. ⚠️
