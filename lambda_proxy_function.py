import json
import requests

def lambda_handler(event, context):
    raw_path = event.get('rawPath', '')
    http_method = event.get('httpMethod', None)
        
    if http_method is None:
        http_method = event['requestContext']['http']['method'].upper() if 'requestContext' in event and 'http' in event['requestContext'] else None
    
    query_params = event.get('queryStringParameters', {})
    headers = event.get('headers', {})
    body = event.get('body', '')

    target_url = f'https://yourdomain.com{raw_path}' #specify your domain

    try:
        
        return {
            "url":target_url,
        }
        response = requests.request(
            method=http_method,
            url=target_url,
            params=query_params,
            headers=headers,
            data=body
        )
        
        # Create a dictionary for the response data
        response_data = {
            'statusCode': response.status_code,
            'body': response.json(),
            'headers': dict(response.headers)
        }
        # Add CORS headers to the response
        response_data['headers']['Access-Control-Allow-Origin'] = '*'  # Allow requests from any origin
        response_data['headers']['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'  # Allow specific HTTP methods
        response_data['headers']['Access-Control-Allow-Headers'] = 'Content-Type, Accept, Authorization, X-Requested-With, Application'  # Allow specific headers
        
        return response_data

    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
