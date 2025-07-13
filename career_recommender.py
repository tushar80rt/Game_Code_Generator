# from camel.models import ModelFactory
# from camel.types import ModelPlatformType, ModelType
# from camel.configs import MistralConfig
# from camel.agents import ChatAgent
# from camel.messages import BaseMessage

# from dotenv import load_dotenv

# load_dotenv("api.env")

# mistral_model = ModelFactory.create(
#     model_platform=ModelPlatformType.MISTRAL,
#     model_type=ModelType.MISTRAL_SMALL_3_2,
#     model_config_dict=MistralConfig(temperature=0.9).as_dict()
# )

# def recommend_careers(mapped_interests):
#     system_msg = BaseMessage.make_assistant_message(
#         role_name="Career Advisor",
#         content="You are a career advisor. Suggest top 5 careers for the user."
#     )

#     user_msg = BaseMessage.make_user_message(
#         role_name="User",
#         content=mapped_interests
#     )

#     agent = ChatAgent(system_message=system_msg, model=mistral_model)
#     response = agent.step(user_msg)
#     return response.msg.content























# from camel.models import ModelFactory
# from camel.types import ModelPlatformType, ModelType
# from camel.configs import MistralConfig
# from camel.agents import ChatAgent
# from camel.messages import BaseMessage
# from camel.toolkits import TerminalToolkit
# from dotenv import load_dotenv

# load_dotenv("api.env")

# # Load Mistral model
# mistral_model = ModelFactory.create(
#     model_platform=ModelPlatformType.MISTRAL,
#     model_type=ModelType.MISTRAL_SMALL_3_2,
#     model_config_dict=MistralConfig(temperature=0.9).as_dict()
# )

# # Setup Terminal Toolkit
# terminal_toolkit = TerminalToolkit(working_dir=".", safe_mode=True)
# tools = terminal_toolkit.get_tools()

# def recommend_careers(mapped_interests):
#     system_msg = BaseMessage.make_assistant_message(
#         role_name="Career Advisor",
#         content="You are a career advisor. Suggest top 5 careers. Use terminal tools if needed to analyze user files or environment."
#     )

#     user_msg = BaseMessage.make_user_message(
#         role_name="User",
#         content=mapped_interests
#     )

#     agent = ChatAgent(
#         system_message=system_msg,
#         model=mistral_model,
#         tools=tools  # ✅ Yeh sahi argument hai
#     )

#     response = agent.step(user_msg)
#     return response.msg.content





















# MISTRAL_API_KEY=MMHzOdABkUc9piJC89Jn0WAtS1RWk1s8


















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
