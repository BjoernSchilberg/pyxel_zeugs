from pyxel import Pyxel

# a rudimentary neural network for the Pyxel coding pet
# https://www.educationalinsights.com/codewith-pyxel
pyxel = Pyxel()


class random_for_pyxel:
    def __init__(self, seed=1):
        self.a = 1664525  # Multiplier
        self.c = 1013904223  # Increment
        self.m = 2**32  # Modulus
        self.seed = seed

    def random(self):
        # Generate the next number in the sequence
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m

    def uniform(self, a, b):
        # Generate a random number within a specific range
        return a + (b - a) * self.random()


class SimpNeuralNetwork:
    def __init__(self, num_inputs, num_outputs):
        # Initialize weights
        self.weights = [
            [random_for_pyxel.uniform(-1, 1) for _ in range(num_inputs)]
            for _ in range(num_outputs)
        ]

    def activate(self, inputs):
        # Activation Function
        def threshold(sum):
            return 1 if sum > 0 else 0

        outputs = []
        for weight in self.weights:
            weighted_sum = sum(i * w for i, w in zip(inputs, weight))
            outputs.append(threshold(weighted_sum))

        return outputs

    def adjust_weights(self, inputs, desired_outputs):
        # Simple weight adjustment
        for i, (output, desired_output) in enumerate(
            zip(self.activate(inputs), desired_outputs)
        ):
            if output != desired_output:
                for j in range(len(inputs)):
                    self.weights[i][j] += (desired_output - output) * inputs[j]


# Map Output to Light Colors
def map_to_lights(outputs):
    light_colors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Assuming 10 different colors
    activated_lights = [
        color for output, color in zip(outputs, light_colors) if output == 1
    ]
    for color in activated_lights:
        pyxel.Lights(color, 3)


# Emotional States with Light Patterns
emotional_states = {
    "happy": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "curious": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "scared": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "calm": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "excited": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "sad": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    "playful": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "relaxed": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
}

# Training Data for Emotional Responses
training_data = [
    # Define training examples for each emotional state
    ([1, 0], emotional_states["happy"]),
    ([0, 1], emotional_states["curious"]),
    # Add more examples for each state
]

# Train the Neural Network
nn = NeuralNetwork(num_inputs=2, num_outputs=10)
for inputs, desired_outputs in training_data:
    while True:
        outputs = nn.activate(inputs)
        if outputs == desired_outputs:
            break
        nn.adjust_weights(inputs, desired_outputs)

# Real-time Interaction
while True:
    proximity_input = 1 if pyxel.Proximity(1) else 0
    touch_input = 1 if pyxel.Touch(1) else 0
    nn_outputs = nn.activate([proximity_input, touch_input])
    map_to_lights(nn_outputs)
