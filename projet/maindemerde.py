#!/usr/bin/env python3

from simulator import Simulator, World, Body
from simulator.utils.vector import Vector2
from simulator.solvers import DummySolver
from simulator.physics.engine import DummyEngine
from simulator.graphics import Screen

import pygame as pg

if __name__ == "__main__":
    b1 = Body(Vector2(0, 0),
              velocity=Vector2(0, 0),
              mass=10,
              draw_radius=10)
    b2 = Body(Vector2(1, 1),
              velocity=Vector2(0, 0.2),
              mass=1,
              draw_radius=5)

    world = World()
    world.add(b1)
    world.add(b2)

    simulator = Simulator(world, DummyEngine, DummySolver)

    screen_size = Vector2(800, 600)
    screen = Screen(screen_size,
                    bg_color=(0, 0, 0),
                    caption="Simulator")
    screen.camera.scale = 50

    # this coefficient controls the speed
    # of the simulation
    time_scale = 10

    DummyEngine.derivatives()
