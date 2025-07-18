
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.toolkits import TerminalToolkit, FileWriteToolkit
from dotenv import load_dotenv

load_dotenv("api.env")

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type="gpt-4o",
    model_config_dict={"temperature": 0.4, "max_tokens": 4096}
)

terminal_toolkit = TerminalToolkit(
    working_dir=r"C:/Desktop/Snake",
    safe_mode=False
)

file_toolkit = FileWriteToolkit(
    output_dir=r"C:/Desktop/Snake"
)

tools = terminal_toolkit.get_tools() + file_toolkit.get_tools()

def write_game(game_name):
    system_msg = BaseMessage.make_assistant_message(
    role_name="Universal Playable Game Code Writer",
    content=(
            "You are a professional Python Game Developer Agent.\n"
            "Your task is to write a **fully functional and playable Python game** based on the game name or description given by the user.\n\n"
            " The game MUST include complete playable logic — the user must be able to control or interact with the game.\n"
            " The game MUST respond to keyboard and/or mouse inputs.\n"
            " You MUST write the entire playable code — not just static screens, boards, or UI.\n"
            " Use 'turtle' for simple arcade games (Snake, Pong, Breakout).\n"
            " Use 'tkinter' for board or grid-based games (Chess, Tic-Tac-Toe, Checkers).\n"
            " Use 'pygame' for advanced 2D games — but ONLY with built-in shapes and colors.\n\n"
            " You MUST NOT use external images, sounds, or assets.\n"
            " You MUST NOT use tk.PhotoImage(), pygame.image.load(), or any file loading.\n"
            " You MUST NOT use `while True` loops — only ontimer(), after(), event loops, or suitable game loops.\n"
            " You MUST NOT write commented-out code lines or explanations.\n\n"
            " The game MUST start automatically when the file is run.\n"
            " The game must be saved completely into `C:/Desktop/Snake/game.py` using only the FILE_WRITE tool.\n"
            " Your highest priority is that the user can run the file and immediately PLAY the game."
            " You MUST NOT create just a static board with pieces — you MUST implement full playable game logic with working user controls (moving, selecting, or interacting)."
        )
)


    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content=f"Write a complete, playable {game_name} Python game into `C:/Desktop/Snake/game.py` using FILE_WRITE tool only."
    )

    agent = ChatAgent(system_message=system_msg, model=model, tools=tools)
    response = agent.step(user_msg)
    return response.msg.content


if __name__ == "__main__":
    game_name = input("🕹️ Which game do you want to generate & play?: ")
    print(write_game(game_name))
