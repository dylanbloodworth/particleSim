import pygame

# Initializes the pygame and screen for the animation sequence.
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('testing solving methods')
clock = pygame.time.Clock()


class verlet_obj:

    instances = []

    def __init__(self, init_pos, init_vel, init_acc, dt, radius):

        # Finds the x_1 position based on the Verlet algorithm.
        # This allows me to include an initial velocity into the solver
        # which doesn't seem to be included in any video/forum post I've seen
        # Source -> https://en.wikipedia.org/wiki/Verlet_integration
        self.pos_cur = pygame.Vector2(
            init_pos[0] + init_vel[0]*dt + 0.5*init_acc[0]*dt*dt,
            init_pos[1] + init_vel[1]*dt + 0.5*init_acc[1]*dt*dt
        )

        # This is the initial position x_0
        self.pos_prev = pygame.Vector2(init_pos[0], init_pos[1])
        self.radius = radius
        self.acceleration = pygame.Vector2(0, 0)

        # This adds the initialized object to the list. This allows us to
        # iterate through all the created objects in the Solver class.
        verlet_obj.instances.append(self)

    def update(self, dt):
        """
        Updates the position of the verlet_object a single step. After it
        calculates the position, it redraws the circle and then sets the
        acceleration vector to 0.
        """

        # Vertical updates
        velY = self.pos_cur.y - self.pos_prev.y
        self.pos_prev.y = self.pos_cur.y
        self.pos_cur.y += velY + self.acceleration.y*dt*dt

        # Horizontal updates
        velX = self.pos_cur.x - self.pos_prev.x
        self.pos_prev.x = self.pos_cur.x
        self.pos_cur.x += velX + self.acceleration.x*dt*dt

        # Reset the acceleration vector to 0
        self.acceleration = pygame.Vector2(0, 0)

        pygame.draw.circle(screen, "white", self.pos_cur, self.radius)

    def boundary_constraint(self):
        """
        Checks if the verlet_object is within the boundaries of the screen.
        If not, then it moves the particle back to the edge and gives it the
        correct corresponding velocity based on an elastic collision.
        """

        if self.pos_cur.y > screen.get_height() - self.radius:
            velY = self.pos_cur.y - self.pos_prev.y
            self.pos_cur.y = screen.get_height() - self.radius
            self.pos_prev.y = velY + self.pos_cur.y

        if self.pos_cur.y < self.radius:
            velY = self.pos_cur.y - self.pos_prev.y
            self.pos_cur.y = self.radius
            self.pos_prev.y = velY + self.pos_cur.y

        if self.pos_cur.x < self.radius:
            velX = self.pos_cur.x - self.pos_prev.x
            self.pos_cur.x = self.radius
            self.pos_prev.x = velX + self.pos_cur.x

        if self.pos_cur.x > screen.get_height() - self.radius:
            velX = self.pos_cur.x - self.pos_prev.x
            self.pos_cur.x = screen.get_height() - self.radius
            self.pos_prev.x = velX + self.pos_cur.x

    def accelerate(self, acceleration):
        """
        Sets the acceleration of the object at the beginning of each frame.
        """
        self.acceleration = pygame.Vector2(acceleration[0], acceleration[1])


class Solver:

    def __init__(self, dt):
        self.dt = dt
        self.acceleration = [0, 9.8]

    def update(self):
        self.apply_acceleration()
        self.apply_contraints()
        self.update_position()

    def update_position(self):
        for obj in verlet_obj.instances:
            obj.update(self.dt)

    def apply_acceleration(self):
        for obj in verlet_obj.instances:
            obj.accelerate(self.acceleration)

    def apply_contraints(self):
        for obj in verlet_obj.instances:
            obj.boundary_constraint()


def main():

    running = True

    dt = clock.tick(60)/500
    solve = Solver(dt)

    verlet_obj([255, 255], [10, 20], [0, 9.8], dt, 10)
    verlet_obj([100, 300], [-30, 40], [0, 9.8], dt, 20)

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        screen.fill("black")

        solve.update()


main()
