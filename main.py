import numpy as np
import matplotlib.pyplot as plt
from pid import PID
from DynamicModel import MassSpringDamper

dt = 0.001

reg = PID(15, 10, 0.0016, dt, -10 ,10)
model = MassSpringDamper(1, 1, 1, dt=dt)
T = 20
t = np.arange(0, T, dt)
F = 0

x_des = np.ones(len(t))

model_x = []

P_hist, D_hist, I_hist = [], [], []
for i in range(len(t)):
    model_x.append(model.update(F))
    F = -reg.update(model_x[-1], x_des[i])
    P_hist.append(reg.q_p)
    D_hist.append(reg.q_d)
    I_hist.append(reg.q_p)
    
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=[10, 7])
ax1.plot(t, model_x, label="real x")
ax1.plot(t, x_des, label="x desired")
ax2.plot(t, P_hist, label="P")
ax2.plot(t, D_hist, label="D")
ax2.plot(t, I_hist, label="I")
 

ax1.legend()
ax2.legend()
plt.show()

git add .
git commit -m "some changes"
git push