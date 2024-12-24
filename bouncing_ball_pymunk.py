import pyxel
import pymunk

# https://qiita.com/malo21st/items/32b7865e7c78d4ac2741#%E4%BB%98%E9%8C%B2%EF%BC%92%E5%B0%8F%E3%83%8D%E3%82%BF%E9%9B%86

WIDTH, HEIGHT = 160, 120
INIT_POS = WIDTH // 2, 0
FPS = 60
BALL_PROPERTY = 1, float("inf")  # mass, moment of inertia
STOP_THRESHOLD = 0.1  # Threshold speed to consider the ball stopped


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, fps=FPS)
        self.space = pymunk.Space()  # Create physical space
        self.space.gravity = (0, 900)  # Set gravity
        self.create_ball(*INIT_POS)
        self.create_ground()
        pyxel.run(self.update, self.draw)

    def create_ball(self, x, y):
        self.ball_body = pymunk.Body(*BALL_PROPERTY)  # Create dynamic body for the ball
        self.ball_body.position = (x, y)  # Set initial position of the ball
        self.ball_shape = pymunk.Circle(
            self.ball_body, 5
        )  # Define the ball as a circle
        self.ball_shape.elasticity = 0.9  # Set elasticity
        self.space.add(self.ball_body, self.ball_shape)

    def create_ground(self):
        # Define the ground as a static box
        self.ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)  # Static body
        self.ground_body.position = (
            WIDTH / 2,
            HEIGHT - 5,
        )  # Set the center position of the box
        self.ground_shape = pymunk.Poly.create_box(
            self.ground_body, (WIDTH, 10)
        )  # Create the box
        self.ground_shape.elasticity = 0.8  # Set elasticity
        self.space.add(self.ground_body, self.ground_shape)

    def reset_ball_position(self):
        self.ball_body.position = INIT_POS  # Reset the position of the ball
        self.ball_body.velocity = (0, 0)  # Reset the velocity of the ball

    def update(self):
        self.space.step(1 / FPS)  # Update the time step
        # Check if the ball has stopped
        if abs(self.ball_body.velocity.y) < STOP_THRESHOLD:
            self.reset_ball_position()

    def draw(self):
        pyxel.cls(0)  # Clear the screen
        x, y = self.ball_body.position  # Get the position of the ball
        pyxel.circ(x, y, 5, 8)  # Draw the ball
        left, bottom, right, top = (
            self.ground_shape.bb
        )  # Get the position of the ground
        pyxel.rect(left, bottom, right - left, top - bottom, 11)  # Draw the ground


App()
