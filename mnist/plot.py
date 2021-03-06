import numpy as np
import matplotlib.pyplot as plt

for i in range(0,4):
    plt.plot(10**np.arange(0,5),1/(np.load(f'./V100_data/worker_{2**i}.npy')/10000),'.-',label=f'num_workers={2**i}')
plt.title('TESLA V100')
plt.xscale('log')
#plt.yscale('log')
plt.xlabel('batch_size')
plt.ylabel('FPS')
plt.xticks(10**np.arange(0,5))
plt.grid()
plt.legend()
plt.savefig('../plots/TESLA_V100.pdf')
