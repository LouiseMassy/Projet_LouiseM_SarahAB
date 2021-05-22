from ..utils.vector import Vector, Vector2
import math as m

class SolverError(Exception):
    pass


class ISolver:

    # NOTE: our systems do not depend on time,
    # so the input t0 will never be used by the
    # the derivatives function f
    # However, removing it will not simplify
    # our functions so we might as well keep it
    # and build a more general library that
    # we will be able to reuse some day

    def __init__(self, f, t0, y0, max_step_size=0.01):
        self.f = f
        self.t0 = t0
        self.y0 = y0
        self.max_step_size = max_step_size

    def integrate(self, t):
        """ Compute the solution of the system at t
            The input `t` given to this method should be increasing
            throughout the execution of the program.
            Return the new state at time t.
        """
        raise NotImplementedError

###MÉTHODE D'EULER EXPLICITE
# class DummySolver(ISolver):
#     def __init__(self, f, t0, y0, max_step_size=0.01):
#         self.f = f  
#         self.t0 = t0
#         self.y0 = y0
#         self.max_step_size = max_step_size

#     def integrate(self, t):
#         n=m.floor((t-self.t0)/self.max_step_size)
#         s = self.y0 + self.max_step_size * self.f(self.t0, self.y0)
#         for i in range(1, n+1):    
#             s = s + self.max_step_size * self.f(self.t0+i*self.max_step_size, s)
#         s = s + (t-n*self.max_step_size-self.t0) * self.f(t, s)
        
#         self.t0 = t
#         self.y0 = s
#         return s
    
##MÉTHODE DE RUNGE-KUTTA D'ORDRE 4
class DummySolver(ISolver):
    def __init__(self, f, t0, y0, max_step_size=0.01):
        self.f = f  
        self.t0 = t0
        self.y0 = y0
        self.max_step_size = max_step_size

    def integrate(self, t):
        n=m.floor((t-self.t0)/self.max_step_size)
        #s = self.y0 + self.max_step_size * self.f(self.t0, self.y0)
        k1=self.f(self.t0, self.y0)
        k2=self.f(self.t0 + self.max_step_size / 2, self.y0+ self.max_step_size * k1 / 2)
        k3=self.f(self.t0 + self.max_step_size / 2, self.y0+ self.max_step_size * k2 / 2)
        k4=self.f(self.t0 + self.max_step_size, self.y0+ self.max_step_size * k3)
        s=self.y0 + self.max_step_size * (k1+2*k2+2*k3+k4) / 6
        
        for i in range(1, n+1): 
            k1=self.f(self.t0+i*self.max_step_size, s)
            k2=self.f(self.t0+i*self.max_step_size + self.max_step_size / 2, s + self.max_step_size * k1 / 2)
            k3=self.f(self.t0+i*self.max_step_size + self.max_step_size / 2, s + self.max_step_size * k2 / 2)
            k4=self.f(self.t0+i*self.max_step_size + self.max_step_size, s + self.max_step_size * k3)
            #s = s + self.max_step_size * self.f(self.t0+i*self.max_step_size, s)
        #s = s + (t-n*self.max_step_size-self.t0) * self.f(t, s)
        H = (t-n*self.max_step_size-self.t0)    #dernier pas jusqu'à t
        k1=self.f(t, s)
        k2=self.f(t + H / 2, s + H * k1 / 2)
        k3=self.f(t + H / 2, s + H * k2 / 2)
        k4=self.f(t + H, s + H * k3)
           
        self.t0 = t
        self.y0 = s
        return s