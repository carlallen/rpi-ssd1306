# rpi-ssd1306

`docker run -d -e RESET=4 -e ROTATE=False --privileged -v /etc/localtime:/etc/localtime --device /dev/i2c-1:/dev/i2c-1 --device /dev/spidev0.0:/dev/spidev0.0 --restart always --name clock carlallen/rpi-ssd1306:latest
Be`
