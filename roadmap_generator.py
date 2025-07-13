# from camel.models import ModelFactory
# from camel.types import ModelPlatformType, ModelType
# from camel.configs import MistralConfig
# from camel.agents import ChatAgent
# from camel.messages import BaseMessage
# from dotenv import load_dotenv

# load_dotenv("api.env")

# # ... (imports same as above)

# mistral_model = ModelFactory.create(
#     model_platform=ModelPlatformType.MISTRAL,
#     model_type=ModelType.MISTRAL_LARGE,
#     model_config_dict=MistralConfig(temperature=0.9).as_dict()
# )

# def generate_roadmap(career_suggestions):
#     system_msg = BaseMessage.make_assistant_message(
#         role_name="Roadmap Generator",
#         content="You are a career mentor. Create a step-by-step roadmap for the careers."
#     )

#     user_msg = BaseMessage.make_user_message(
#         role_name="User",
#         content=career_suggestions
#     )

#     agent = ChatAgent(system_message=system_msg, model=mistral_model)
#     response = agent.step(user_msg)
#     return response.msg.content
































# from camel.models import ModelFactory
# from camel.types import ModelPlatformType
# from camel.types import ModelType
# from camel.configs import MistralConfig
# from camel.agents import ChatAgent
# from camel.messages import BaseMessage
# from camel.toolkits import TerminalToolkit
# from dotenv import load_dotenv

# load_dotenv("api.env")

# mistral_model = ModelFactory.create(
#     model_platform=ModelPlatformType.MISTRAL,
#     model_type=ModelType.MISTRAL_LARGE,
#     model_config_dict=MistralConfig(temperature=0.9).as_dict()
# )

# terminal_toolkit = TerminalToolkit(working_dir=".", safe_mode=True)
# tools = terminal_toolkit.get_tools()

# def generate_roadmap(career_suggestions):
#     system_msg = BaseMessage.make_assistant_message(
#         role_name="Roadmap Generator",
#         content="You are a career mentor. Use terminal if needed. Build a step-by-step roadmap for the given careers."
#     )

#     user_msg = BaseMessage.make_user_message(
#         role_name="User",
#         content=career_suggestions
#     )

#     # ✅ Corrected this line below
#     agent = ChatAgent(system_message=system_msg, model=mistral_model, tools=tools)
#     response = agent.step(user_msg)
#     return response.msg.content

























































from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.configs import GroqConfig
from camel.toolkits import TerminalToolkit
from dotenv import load_dotenv

load_dotenv("api.env")

# ✅ Load Groq LLaMA 3/4 Model
groq_model = ModelFactory.create(
    model_platform=ModelPlatformType.GROQ,
    model_type="llama3-70b-8192",  # model name as string
    model_config_dict=GroqConfig(
        temperature=0.9, # Will load from env
    ).as_dict()
)

# ✅ Setup Terminal Toolkit
# terminal_toolkit = TerminalToolkit(working_dir=".", safe_mode=False)


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

    # agent = ChatAgent(system_message=system_msg, model=groq_model, tools=tools)

    agent = ChatAgent(
        system_message=system_msg,
        model=groq_model,
        tools=tools
    )
    response = agent.step(user_msg)
    return response.msg.content
