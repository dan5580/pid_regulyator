class MassSpringDamper:
    def __init__(self, k_gg, c_gg, m_gg, x_zero=0, v_zero=0, dt=0.01):
        self.k = k_gg
        self.c = c_gg
        self.m = m_gg
        self.dt = d_t
        self.x = x_zero
        self.v = v_zero

    def update(self, F):
        xnew = self.v * self.dt + self.x
        vnew = self.dt / self.m * (F - self.c * self.v - self.k * self.x) + self.v
        self.x = xnew
        self.v = vnew
        return self.x