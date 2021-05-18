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


class DummySolver(ISolver):
    def __init__(self, f, t0, y0, max_step_size=0.01):
        self.f = f  
        self.t0 = t0
        self.y0 = y0
        self.max_step_size = max_step_size

    def integrate(self, t):
        n=m.floor((t-self.t0)/self.max_step_size)
        # s=0
        # for i in range(n+1):
        #     s= s + self.max_step_size * self.f(self.t0+i*self.max_step_size, self.y0)
        # s=s + (t-n*self.max_step_size-self.t0) * self.f(t, self.y0)
        # 
        #s=Vector(len(self.y0))
        s = self.y0 + self.max_step_size * self.f(self.t0, self.y0)
        for i in range(1, n+1):    
            s = s + self.max_step_size * self.f(self.t0+i*self.max_step_size, s)
        s = s + (t-n*self.max_step_size-self.t0) * self.f(t, s)
        
        self.t0 = t
        self.y0 = s
        return s