"""
Lambda function to send and analyze images using OpenAI API with Vision model
"""
import os
import json
import logging
import traceback

root = logging.getLogger()
root.setLevel(logging.INFO)

def lambda_handler(event, _):
    """
    Lambda Handler

    Args:
        event (object): Function body
        _ (string): Function context (not used)
    """
    try:
        logging.info(f'Event: {event}')

        print(os.environ['OPENAI_API_KEY'])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Hello World!"
            })
        }
    except Exception as exc:
        logging.error(str(traceback.format_exc()))
        raise exc
