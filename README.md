This is an extension of Thor: [https://github.com/observing/thor](https://github.com/observing/thor)

The project is to generate metrics(failure rate, handshaking time, latency) and figures of different number of connections(from start to end with interval).
e.g. In **metrics.png**, we show the figure of failure rate, handshaking time, latency from connections number 1000 to 4000, with 500 being the inteval.

To use it, simply run ```./run.sh $start $end $inteval``` (You may need to ```chmod +x run.sh``` before running)

The default websocket is ```ws://localhost:9000/ws```. You can change it in **run.sh**

After running, the figures are in **metrics.png** and the logs are in **logs** directory.