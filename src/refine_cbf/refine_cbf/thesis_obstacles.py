# Contains Obstacles class.
# Its attributes are the different sets of obstacles used in the experiment.
# Any number of sets of obstacles can be defined.
# The sets of obstacles are defined as dictionaries.
# Currently only circles, rectangles and bounding boxes are supported.
# Addtionally, functionality can be developed by adding to the refine_cbf/utils.py file.

import numpy as np

class Obstacles:
    """Class representing different sets of obstacles used in the experiment."""

    # 1st (Initial) set of obstacles
    OBSTACLES_1 = {
        "bounding_box": {
            "bounding_box_1": {"center": np.array([0.5, 1.0]), "length": np.array([1.0, 2.0])},
        },
        "iteration": 0,
    }

    # 2nd set of obstacles
    OBSTACLES_2 = {
        "circle": {
            "circle_1": {"center": np.array([1.1, 1.0]), "radius": 0.1},
            "circle_2": {"center": np.array([1.75, 0.25]), "radius": 0.75},
            "circle_3": {"center": np.array([1.75, 1.75]), "radius": 0.75},
        },
        "bounding_box": {
            "bounding_box_1": {"center": np.array([1.0, 1.0]), "length": np.array([2.0, 2.0])},
        },
        "iteration": 10,
    }

    # 3rd set of obstacles
    OBSTACLES_3 = {
        "circle": {
            "circle_1": {"center": np.array([1.1, 1.0]), "radius": 0.1},
            "circle_2": {"center": np.array([2.0, 2.0]), "radius": 1.0},
            "circle_3": {"center": np.array([2.0, 0.0]), "radius": 1.0},
        },
        "bounding_box": {
            "bounding_box_1": {"center": np.array([1.0, 1.0]), "length": np.array([2.0, 2.0])},
        },
        "iteration": 20,
    }

    # 4th set of obstacles
    OBSTACLES_4 = {
        "circle": {
            "circle_1": {"center": np.array([1.1, 1.0]), "radius": 0.1},
            "circle_2": {"center": np.array([2.0, 2.25]), "radius": 1.0},
            "circle_3": {"center": np.array([2.0, 0.25]), "radius": 1.0},
        },
        "bounding_box": {
            "bounding_box_1": {"center": np.array([1.0, 1.0]), "length": np.array([2.0, 2.0])},
        },
        "iteration": 30,
    }

    # 5th set of obstacles
    OBSTACLES_4 = {
        "circle": {
            "circle_1": {"center": np.array([1.1, 1.0]), "radius": 0.1},
            "circle_2": {"center": np.array([2.0, 2.75]), "radius": 1.0},
            "circle_3": {"center": np.array([2.0, -0.75]), "radius": 1.0},
        },
        "bounding_box": {
            "bounding_box_1": {"center": np.array([1.0, 1.0]), "length": np.array([2.0, 2.0])},
        },
        "iteration": 40,
    }

    # Add more obstacles here if necessary.

    def get_obstacle_list(self):
        """Get all attributes defined in the class starting with 'OBSTACLES_'."""
        all_attributes = vars(type(self))
        obstacle_attributes = [value for key, value in all_attributes.items() if key.startswith('OBSTACLES_')]
        return obstacle_attributes

    def get_iteration_list(self):
        """Get the 'iteration' values from the obstacle dictionaries."""
        obstacle_attributes = self.get_obstacle_list()
        iteration_list = [obstacle["iteration"] for obstacle in obstacle_attributes]
        return iteration_list
