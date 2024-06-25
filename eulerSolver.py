import pygame
from math import *

# Initializes the pygame and screen for the animation sequence

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('testing solving methods')
clock = pygame.time.Clock()


class euler_object:

    instances = []

    def __init__(self, pos, vel, dt, radius):

        self.pos = pygame.Vector2(pos[0], pos[1])
        self.vel = pygame.Vector2(vel[0], vel[1])
        self.radius = radius
        self.acceleration = pygame.Vector2(0, 0)

        euler_object.instances.append(self)

    def update(self, dt):
        """
        Updates the position of the euler_object a single step. After it
        calculates the position and redraws the circle
        """
        self.vel += self.acceleration*dt
        self.pos += self.vel*dt

        self.acceleration = pygame.Vector2(0.0, 0.0)

        pygame.draw.circle(screen, "white", self.pos, self.radius)

    def boundary_constraint(self):

        if (self.pos.x < self.radius):
            self.pos.x = self.radius
            self.vel.x *= -1

        if (self.pos.x > screen.get_width() - self.radius):
            self.pos.x = screen.get_width() - self.radius
            self.vel.x *= -1

        if (self.pos.y > screen.get_height() - self.radius):
            self.pos.y = screen.get_height() - self.radius
            self.vel.y *= -1

        if (self.pos.y < self.radius):
            self.pos.y = self.radius
            self.vel.y *= -1

    def accelerate(self, acceleration):
        self.acceleration = acceleration


class Solver:

    def __init__(self, dt):
        self.dt = dt
        self.acceleration = pygame.Vector2(0, 9.8)

    def update(self):
        self.apply_acceleration()
        self.apply_constraint()
        self.apply_collision()
        self.update_position()

    def update_position(self):

        for obj in euler_object.instances:
            obj.update(self.dt)

    def apply_acceleration(self):

        for obj in euler_object.instances:
            obj.accelerate(self.acceleration)

    def apply_constraint(self):

        for obj in euler_object.instances:
            obj.boundary_constraint()

    def apply_collision(self):
        # This still doesn't work correctly. I don't really know if
        # it's because of the implementation of the elastic collision
        # or the method is really inaccurate at resolving the collision.

        # I'm incline to say that the elastic collision itself is
        # probably off somehow.
    :

        for obj_1 in euler_object.instances:
            for obj_2 in euler_object.instances:

                if obj_1 != obj_2:

                    collision_axis = obj_1.pos - obj_2.pos
                    dist = collision_axis.length()
                    constraint = obj_1.radius + obj_2.radius

                    if dist < constraint:
                        print(f"Collision Detected where distance is {dist}")

                        n = collision_axis.normalize()

                        delta = constraint - dist

                        obj_1.pos += delta * n
                        obj_2.pos -= delta * n

                        diff_v = obj_1.vel - obj_2.vel
                        diff_x = obj_1.pos - obj_2.pos
                        norm2 = diff_x.length_squared()

                        print(obj_1.vel.dot(obj_2.vel))

                        obj_1.vel, obj_2.vel = obj_1.vel - 2 * \
                            diff_v.dot(diff_x)*(diff_x/norm2), obj_2.vel + \
                            2*diff_v.dot(diff_x)*(diff_x/norm2)

                        print(obj_1.vel.dot(obj_2.vel))


def main():
    running = True

    dt = clock.tick(60)/1000
    solve = Solver(dt)

    while running:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                euler_object(pygame.Vector2(
                    mouse[0], mouse[1]), pygame.Vector2(0, 0), dt, 20)

        pygame.display.flip()
        screen.fill("black")

        solve.update()


main()
