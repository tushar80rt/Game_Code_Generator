from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.toolkits import TerminalToolkit
from dotenv import load_dotenv

load_dotenv("api.env")

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type="gpt-4o",
    model_config_dict={"temperature": 0.4, "max_tokens": 1024}
)

terminal_toolkit = TerminalToolkit(
    working_dir=r"C:/Desktop/Snake",
    safe_mode=False
)
tools = terminal_toolkit.get_tools()

def run_game(file_name="game.py"):
    system_msg = BaseMessage.make_assistant_message(
        role_name="Game Runner Agent",
        content=f"You are a terminal executor. Use TERMINAL tool to run `python {file_name}`. Do not explain."
    )

    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content=f"Run `python {file_name}` using TERMINAL tool."
    )

    agent = ChatAgent(system_message=system_msg, model=model, tools=tools)
    response = agent.step(user_msg)
    return response.msg.content

