from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class RecipeGenerationCrew():
    """Recipe Generation Multi-Agent Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def culinary_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['culinary_researcher'],
            verbose=True
        )

    @agent
    def recipe_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['recipe_creator'],
            verbose=True
        )

    @agent
    def recipe_refiner(self) -> Agent:
        return Agent(
            config=self.agents_config['recipe_refiner'],
            verbose=True
        )

    @task
    def research_recipe_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_recipe_task'],
        )

    @task
    def create_recipe_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_recipe_task'],
            output_file='recipes.md'
        )

    @task
    def refine_recipe_task(self) -> Task:
        return Task(
            config=self.tasks_config['refine_recipe_task'],
            output_file='final_recipes.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Recipe Generation crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True
        )