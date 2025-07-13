from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.configs import GroqConfig
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

def generate_roadmap(career_suggestions):
    system_msg = BaseMessage.make_assistant_message(
        role_name="Roadmap Generator",
        content = (
            "You are a career mentor. Use terminal if needed. Build a step-by-step roadmap "
            "for the given careers. If you use terminal commands, make sure they are fully compatible "
            "with Windows CMD (use backslashes `\\` in folder paths, avoid Unix-style syntax)."
        )

    )

    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content=career_suggestions
    )


    agent = ChatAgent(
        system_message=system_msg,
        model=groq_model,
        tools=tools
    )
    response = agent.step(user_msg)
    return response.msg.content

