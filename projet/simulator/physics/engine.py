from ..utils.vector import Vector, Vector2
from .constants import G


def gravitational_force(pos1, mass1, pos2, mass2):
    """ Return the force applied to a bodyVector in pos1 with mass1
        by a body in pos2 with mass2
    """
    norme_carre = Vector.sqrnorm(Vector.__sub__(pos1,pos2))
    normeF=G*mass1*mass2/norme_carre
    norme = Vector.norm(Vector.__sub__(pos1,pos2))
    vecteur_directeur=Vector2((pos2[0]-pos1[0])/norme,(pos2[1]-pos1[1])/norme)
    return Vector2(normeF*vecteur_directeur[0],normeF*vecteur_directeur[1])
    #raise NotImplementedError


class IEngine:                  #SQUELETTE
    def __init__(self, world):
        self.world = world

    def derivatives(self, t0, y0):
        """ This is the method that will be fed to the solver
            it does not use it's first argument t0,
            its second argument y0 is a vector containing the positions 
            and velocities of the bodies, it is laid out as follow
                [x1, y1, x2, y2, ..., xn, yn, vx1, vy1, vx2, vy2, ..., vxn, vyn]
            where xi, yi are the positions and vxi, vyi are the velocities.

            Return the derivative of the state, it is laid out as follow
                [vx1, vy1, vx2, vy2, ..., vxn, vyn, ax1, ay1, ax2, ay2, ..., axn, ayn]
            where vxi, vyi are the velocities and axi, ayi are the accelerations.
        """
        raise NotImplementedError

    def make_solver_state(self):
        """ Returns the state given to the solver, it is the vector y in
                y' = f(t, y)
            In our case, it is the vector containing the 
            positions and speeds of all our bodies:
                [x1, y1, x2, y2, ..., xn, yn, vx1, vy1, vx2, vy2, ..., vxn, vyn]
            where xi, yi are the positions and vxi, vyi are the velocities.
        """
        raise NotImplementedError


class DummyEngine(IEngine):
    def __init__(self, world):
        self.world = world
        
    def derivatives(self, t0, y0): 
        #récupération des masses
        masses=[]
        n=len(y0)//4
        for i in range (n) :
#            for body in self.world.bodies() : 
#                if (y0[2*i]==body.position[0]) and (y0[2*i+1]==body.position[1]):
#                    masses.append(body.mass)
            masses.append(self.world.get(i).mass)
                    
#        res=[]
#        for i in range (2*n):
#            res.append(y0[2*n+i])
#        for i in range (n):   #on calcule les accélérations ai
#            sommeX=0
#            sommeY=0
#            for j in range(n):    #somme des forces extérieures
#                if i != j :
#                    force = gravitational_force([y0[2*i], y0[2*i+1]], masses[i], [y0[2*j], y0[2*j+1]], masses[j])
#                    forceX = force[0]
#                    sommeX = sommeX + forceX
#                    forceY = force[1]
#                    sommeY = sommeY + forceY
#            res.append(sommeX / masses[i])
#            res.append(sommeY / masses[i])
            
        res = Vector(4*n)
        for i in range (2*n):
            res[i]=y0[2*n+i]
        for i in range (n):
            sommeX=0
            sommeY=0
            for j in range(n):    #somme des forces extérieures
                if i != j :
                    force = gravitational_force(Vector2(y0[2*i], y0[2*i+1]), masses[i], Vector2(y0[2*j], y0[2*j+1]), masses[j])                
                    forceX = force[0]
                    sommeX = sommeX + forceX
                    forceY = force[1]
                    sommeY = sommeY + forceY
            res[2*n+2*i] = sommeX / masses[i]
            res[2*n+2*i+1] = sommeX / masses[i]
        
        return(res)
        
    def make_solver_state(self):
#       y0=[]
#       for body in self.world.bodies() :
#           y0.append(body.position[0])
#           y0.append(body.position[1])
#       for body in self.world.bodies() :
#           y0.append(body.velocity[0])
#           y0.append(body.velocity[1])
#       return y0
        n=self.world.__len__()
        y0=Vector(4*n)
        for i in range (n) :
            value0=self.world.get(i).position[0]
            y0[2*i]=value0
            value1=self.world.get(i).position[1]
            y0[2*i+1]=value1
        for i in range (n) :
            value0=self.world.get(i).velocity[0]
            y0[2*i+2*n]=value0
            value1=self.world.get(i).velocity[1]
            y0[2*i+1+2*n] = value1
        
        return(y0)