#!/usr/bin/env python
import sys
import warnings

from recipe_generator.crew import RecipeGenerationCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the recipe generation crew.
    Prompts user for cuisine and ingredients.
    """
    # Interactive input for cuisine and ingredients
    # cuisine = input("Enter the cuisine type (e.g., Italian, Mexican, Asian): ").strip()
    # ingredients = input("Enter available ingredients (comma-separated): ").strip()

    inputs = {
        'cuisine': "Italian",
        'ingredients': "tomato, onion"
    }
    RecipeGenerationCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    # Interactive input for cuisine and ingredients
    #cuisine = input("Enter the cuisine type (e.g., Italian, Mexican, Asian): ").strip()
    # ingredients = input("Enter available ingredients (comma-separated): ").strip()

    inputs = {
        'cuisine': "Italian",
        'ingredients': "tomato, onion"
    }
    try:
        RecipeGenerationCrew().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        RecipeGenerationCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    cuisine = input("Enter the cuisine type (e.g., Italian, Mexican, Asian): ").strip()
    ingredients = input("Enter available ingredients (comma-separated): ").strip()

    inputs = {
        "cuisine": cuisine,
        "ingredients": ingredients
    }
    try:
        RecipeGenerationCrew().crew().test(
            n_iterations=int(sys.argv[1]), 
            openai_model_name=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()