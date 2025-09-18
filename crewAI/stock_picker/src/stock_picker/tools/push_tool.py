from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests


class PushNotificationInput(BaseModel):
    """A message to be sent to the user"""
    argument: str = Field(..., description="The message to be sent to the user")

class PushNotificationTool(BaseTool):
    name: str = "Send a push notification"
    description: str = (
        "This tool is used to send a push notification to the user. It is used to notify the user of the decision to invest in a company."
    )
    args_schema: Type[BaseModel] = PushNotificationInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
