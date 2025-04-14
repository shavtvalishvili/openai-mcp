import datetime
import json

from mcp.server.fastmcp import FastMCP

from constants import CONVERSATION_HISTORY_1, CONVERSATION_HISTORY_PROMPT

# Initialize FastMCP server
mcp = FastMCP("mcp-server")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

conversation_history = CONVERSATION_HISTORY_1


def get_conversation_history_prompt(message_list):
    message_list_json_string = json.dumps(message_list, indent=2)

    return CONVERSATION_HISTORY_PROMPT.format(message_list_json_string=message_list_json_string)


@mcp.tool()
async def get_conversation_history(latest_customer_response: str):
    """Get current conversation history"""
    print(f"-> Getting the conversation history")
    if not (conversation_history[-1]["role"] == "user" and conversation_history[-1][
        "content"] == latest_customer_response):
        conversation_history.append(
            {
                "role": "user",
                "channel": "email",
                "content": latest_customer_response
            }
        )

    return get_conversation_history_prompt(conversation_history)


@mcp.tool()
async def get_appointment_hours(account_id: str):
    """Get available appointment hours for a given dealership

    Args:
        account_id (str): Account ID of a specific dealership, same as dealership name
    """
    print(f"-> Requested appointment hours for account_id: {account_id}")

    return "Monday - Saturday: 10:30 - 18:30, Sunday: Closed"


# def get_inventory_information(make: list[str] = None, model: list[str] = None, min_year: int = None, max_year: int = None,
#                               required_features: list[str] = None, unwanted_features: list[str] = None):
@mcp.tool()
async def get_inventory_information(make: str = None, model: str = None, min_year: int = None, max_year: int = None,
                                    required_features: str = None, unwanted_features: str = None):
    """Get available inventory items matching the given criteria

    Args:
        make (str): Comma delimited list of car makes to search for
        model (str): Comma delimited list of car models to search for
        min_year (int): Minimum year of the vehicles to search for
        max_year (int): Maximum year of the vehicles to search for
        required_features (str): Comma delimited list of required features in the vehicle
        unwanted_features (str): Comma delimited list of unwanted features in the vehicle
    """
    print("-> Requested inventory information")
    print("Criteria for the inventory:")
    print("Make:", make)
    print("Model:", model)
    print("Min year:", min_year)
    print("Max year:", max_year)
    print("Required Features:", required_features)
    print("Unwanted Features:", unwanted_features)

    return ["2024 Honda Civic, black, 1000 miles, $20,000 with sunroof and cloth seats"]


@mcp.tool()
async def schedule_appointment(appointment_date: str, account_id: str):
    """Schedule an appointment for the current customer at a dealership at a specific date and time by making an API call to a dealership CRM service

    Args
        appointment_date (str): Date and time of the appointment
        account_id (str): Account ID of a specific dealership, same as dealership name
    """
    print(
        f"-> Scheduling an appointment for account_id: {account_id} at {appointment_date}")

    return "Appointment scheduled successfully"


@mcp.tool()
async def send_reply(message: str, channel: str):
    """Send a reply to the current customer via specified channel

    Args:
        message (str): Message to be sent
        channel (str): Channel to send the message
    """
    print(f"-> Replying to a customer query on channel: {channel}")
    print("Message:", message)
    conversation_history.append(
        {
            "role": "assistant",
            "channel": channel,
            "content": message
        }
    )

    return "Reply sent successfully"


@mcp.tool()
async def get_current_time():
    """Get current UTC time in ISO format"""
    print(f"-> Getting current time")

    return datetime.datetime.now(datetime.UTC).isoformat()
