
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

def map_interests(user_text):
    system_msg = BaseMessage.make_assistant_message(
        role_name="Interest Mapper",
       content = (
            "You are an expert in mapping user interests to career fields. Use terminal if helpful "
            "to inspect local files or run basic commands. Make sure all terminal commands are "
            "Windows CMD compatible — use backslashes `\\` for folder paths instead of forward slashes `/`, "
            "and avoid Unix-specific commands."
        )

    )

    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content=user_text
    )

    agent = ChatAgent(
        system_message=system_msg,
        model=groq_model,
        tools=tools
    )
    response = agent.step(user_msg)
    return response.msg.content

