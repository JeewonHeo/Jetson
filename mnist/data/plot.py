import matplotlib.pyplot as plt
import numpy as np

num_workers = 1
nano = np.load(f'NANO_data/worker_{num_workers}.npy')
tx2  = np.append(np.load( f'TX2_data/worker_{num_workers}.npy'),np.nan)
agx  = np.load( f'AGX_data/worker_{num_workers}.npy')
v100 = np.load(f'V100_data/worker_{num_workers}.npy')

plt.plot(10**np.arange(0,5),1/nano*10000,'.-',label='NANO')
plt.plot(10**np.arange(0,5), 1/tx2*10000,'.-',label='TX2' )
plt.plot(10**np.arange(0,5), 1/agx*10000,'.-',label='AGX' )
plt.plot(10**np.arange(0,5),1/v100*10000,'.-',label='V100')
plt.title(f'num_workers={num_workers}')
plt.xlabel('batch_size')
plt.ylabel('FPS')
plt.xscale('log')
#plt.yscale('log')
plt.grid()

plt.legend()
plt.savefig(f'../../plots/num_workers_{num_workers}.pdf')
