from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.configs import GroqConfig
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.toolkits import TerminalToolkit
from dotenv import load_dotenv


load_dotenv("api.env")


groq_model = ModelFactory.create(
    model_platform=ModelPlatformType.GROQ,
    model_type="llama3-70b-8192", 
    model_config_dict=GroqConfig(
        temperature=0.9, 
    ).as_dict()
)


terminal_toolkit = TerminalToolkit(
    working_dir=r"C:\Users\Tushar Singh\OneDrive\Desktop\test_terminal",
    safe_mode=False
)
tools = terminal_toolkit.get_tools()


def recommend_careers(mapped_interests):
    system_msg = BaseMessage.make_assistant_message(
        role_name="Career Advisor",
       content = (
            "You are a career advisor. Suggest the top 5 careers. Use terminal tools if needed "
            "to analyze user files or environment. Ensure that all terminal commands are fully "
            "compatible with Windows CMD — use double backslashes `\\` in paths instead of forward slashes `/`, "
            "and avoid using Unix-only commands."
        )
    )
    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content=mapped_interests
    )
    agent = ChatAgent(
        system_message=system_msg,
        model=groq_model,
        tools=tools
    )
    response = agent.step(user_msg)
    return response.msg.content
