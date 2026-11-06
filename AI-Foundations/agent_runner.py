
import json

from openai.types.responses.response_input_param import FunctionCallOutput

from azure_inspector import (
    list_resource_groups,
    list_resources,
    list_virtual_machines
)

# Map model tool names to actual Python functions
FUNCTION_MAP = {
    "list_resource_groups": list_resource_groups,
    "list_resources": list_resources,
    "list_virtual_machines": list_virtual_machines
}


def execute_tool(function_name, arguments):

    if function_name not in FUNCTION_MAP:
        raise ValueError("Unsupported tool requested")

    function = FUNCTION_MAP[function_name]

    return function(**arguments)



def run_agent(openai_client, user_question, conversation_id):

    response = openai_client.responses.create(
        conversation=conversation_id,
        input=user_question
    )

    while True:

        function_calls = [
            item for item in response.output
            if item.type == "function_call"
        ]

        if not function_calls:
            break

        outputs = []

        for call in function_calls:

            print(f"Executing tool: {call.name}")

            arguments = json.loads(call.arguments)

            try:
                result = execute_tool(
                    call.name,
                    arguments
                )

                output = {
                    "success": True,
                    "data": result
                }

            except Exception as error:
                output = {
                    "success": False,
                    "error": str(error)
                }

            outputs.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": json.dumps(output)
            })

        # Submit outputs to the SAME conversation
        response = openai_client.responses.create(
            conversation=conversation_id,
            input=outputs
        )

    return response.output_text


    response = openai_client.responses.create(
    conversation=conversation_id,
    input=user_question
    )

    # Process tool calls until the model returns a final answer
    while True:

        function_calls = [
            item for item in response.output
            if item.type == "function_call"
        ]

        if not function_calls:
            break

        outputs = []

        for call in function_calls:

            arguments = json.loads(call.arguments)

            try:
                result = execute_tool(
                    call.name,
                    arguments
                )

                output = {
                    "success": True,
                    "data": result
                }

            except Exception as error:
                output = {
                    "success": False,
                    "error": str(error)
                }

            outputs.append(
                FunctionCallOutput(
                    type="function_call_output",
                    call_id=call.call_id,
                    output=json.dumps(output)
                )
            )

        response = openai_client.responses.create(
        conversation=conversation_id,
        input=user_question
    )

    return response.output_text
