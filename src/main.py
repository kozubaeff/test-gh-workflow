import os
import json

def db_watcher_function(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "contour": os.environ.get("CONTOUR"),
                "secret": os.environ.get("SECRET") 
            }, 
            default=vars,
        ),
    }