import json
from datetime import datetime

from src.models.info import Info
from src.prompts import destination, finance
from universa.agents.generator_agent import GeneratorAgent
from universa.agents.generic_solver import GenericSolver
from universa.agents.matcher_agent import MatcherAgent
from universa.agents.solver import Solver
from src.utils.data import WriteToJson, ReadFromJson
from universa.agents.travel_solver import TravelSolver


def gather_information() -> str:
    # Ask user
    print("What can I do for you?")

    # Catch answer
    answer = input("> ")

    return answer

def web(answer : str):
        matcher_agent = MatcherAgent()
        api = matcher_agent.invoke(answer)

        generator_agent = GeneratorAgent()
        key = generator_agent.invoke(api.result)

        return {
             # I would like the api.result to be parsed to json through json.loads function
             # but for some reason api.result always returns invalid json strings
             # tried solution to use GenericSolver to correct the invalid json strings but it is hard to get it right.
            "Recommended API" : api.result,
            "Required input" : key.required.split(",")
        }


def main():

    task = gather_information()

    matcher_agent = MatcherAgent()
    api = matcher_agent.invoke(task)
    print("Recommended API:", api.result)

    generator_agent = GeneratorAgent()
    key = generator_agent.invoke(api.result)
    print("Required input:", key.required)


if __name__ == "__main__":
    main()
