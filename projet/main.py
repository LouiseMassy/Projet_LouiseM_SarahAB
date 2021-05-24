#!/usr/bin/env python3

from simulator import Simulator, World, Body
from simulator.utils.vector import Vector2
from simulator.solvers import DummySolver, KuttaSolver
from simulator.physics.engine import DummyEngine
from simulator.graphics import Screen
import random



if __name__ == "__main__":
    b1 = Body(Vector2(0, 0),
              velocity=Vector2(0, 0),
              mass=10,
              color=(255,255,255),
              draw_radius=10)
    b2 = Body(Vector2(1, 1),
              velocity=Vector2(0, 0.2),
              mass=5,
              color=(240,128,128),
              draw_radius=5)

    world = World()
    world.add(b1)
    world.add(b2)

    listbodies = [b1, b2]

    ChoixSolver = KuttaSolver    #choix du solveur : Dummy ou Kutta  

    simulator = Simulator(world, DummyEngine, ChoixSolver)

    screen_size = Vector2(800, 600)
    screen = Screen(screen_size,
                    bg_color=(0, 0, 0),
                    caption="Simulator")
    screen.camera.scale = 10    #pas trop grand sinon on ne voit pas les deux particules
                                #autour de 10
    # this coefficient controls the speed
    # of the simulation
    time_scale = 10

    print("Start program")
    while not screen.should_quit:
        dt = screen.tick(60)
        
        
    
        # simulate physics
        delta_time = time_scale * dt / 1000
        simulator.step(delta_time)

        # read events
        screen.get_events()

        # handle events
        #   scroll wheel
        if screen.get_wheel_up():
            screen.camera.scale *= 1.1
        elif screen.get_wheel_down():
            screen.camera.scale *= 0.9
        
        
        # ajout d'un corps dans le world
        if screen.get_right_mouse():
            b = Body(Vector2(random.randint(0,5), random.randint(0,5)),
              velocity=Vector2(0, random.uniform(0.0,0.2)),
              mass=random.randint(1,10),
              color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)),
              )
            b.draw_radius=b.mass
            
            listbodies.append(b)

            world = World()
            for bdy in listbodies :
              world.add(bdy)
            simulator=Simulator(world,DummyEngine,ChoixSolver)
#            

        # draw current state
        screen.draw(world)

        # draw additional stuff
        screen.draw_corner_text("Time: %f" % simulator.t)
        
        # show new state
        screen.update()

    screen.close()
    print("Done")
