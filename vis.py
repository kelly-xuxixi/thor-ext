import matplotlib.pyplot as plt 
import numpy as npy 

f = open('log.txt').readlines()

fig, axs = plt.subplots(2, 2)
fig.set_figheight(8)
fig.set_figwidth(8)
connections = []
failure_rate = []
handshaking_mean = []
latency_mean = []
for line in f:
    data = line.split()
    connections.append(int(data[0]))
    failure_rate.append(float(data[2]))
    handshaking_mean.append(float(data[3]))
    latency_mean.append(float(data[4]))

axs[0, 0].plot(connections, failure_rate)
axs[0, 0].set_title('failure rate')
axs[1, 0].plot(connections, handshaking_mean)
axs[1, 0].set_title('handshaking mean time(ms)')
axs[1, 1].plot(connections, latency_mean)
axs[1, 1].set_title('latency mean time(ms)')

plt.savefig('metrics.png')
plt.close()