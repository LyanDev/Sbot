from abc import ABC, abstractmethod, abstractstaticmethod
from email import message
from io import BytesIO
from PIL import Image   
import discord

class Command(ABC):
    @abstractmethod
    def __init__(self, calls=[], admin=False) -> None:
        self.calls = calls
        self.admin = admin 

    @abstractstaticmethod
    async def execute(args: list, msg: discord.Message):
        pass

class Help(Command):
    def __init__(self):
        super().__init__(["hello"], False)
    
    async def execute(args: list, msg: discord.Message):
        return "Hello"

class CustomEmoji(Command):
    def __init__(self):
        super().__init__(["color"], False)
    
    async def execute(args: list, msg: discord.Message):
        if len(args) != 3:
            return "Idk understand ur format"
        elif not all([(lambda a: a.isdigit())(x) for x in args]):
            return "Color value must be from 0 ~ 255"
        
        args.append(255)
        
        emoji = Image.new(mode="RGBA", size=(32, 32), color=tuple([int(x) for x in args]))
        img_byte_array = BytesIO()
        emoji.save(img_byte_array, format="PNG")

        await msg.guild.create_custom_emoji(name="_".join(args[:3]), image=img_byte_array.getvalue())
        return "Successfully created the emoji :{}:".format("_".join(args[:3]))