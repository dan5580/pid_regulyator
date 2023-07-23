class PID:
    def __init__(self, k_p, k_d, k_i, d_t, lowerbound, upperbound):
        self.k_p = k_p
        self.k_d = k_d
        self.k_i = k_i
        self.d_t = d_t
        self.prev_err = None
        self.q_p = 0
        self.q_d = 0
        self.q_i = 0
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        
    def update(self, x_value, xdes):
        err = x_value - xdes
        self._P = self.k_p * err
        if self.prev_err is not None:
            self._D = self.k_d * (err - self.prev_err) / self.d_t
        self.q_i += self.k_i * err
        self.prev_err = err
        outp = self._P + self._D + self.q_i
        outp = self._constrain(outp, self.upperbound, self.lowerbound)
        return outp
    
    def _constrain(self, x_value, upperbound, lowerbound):
        if x_value > upperbound:
            x_value = upperbound
        if x_value < lowerbound:
            x_value = lowerbound
        return x_value 
        