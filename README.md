# Lambda Proxy Function

This AWS Lambda function acts as a proxy for forwarding HTTP requests to a target URL. It can be used to integrate external APIs with AWS Lambda and handle requests in a serverless environment.

## Prerequisites

- AWS account
- AWS Lambda service configured
- API Gateway (optional, if using as an HTTP endpoint)

## Getting Started

1. Clone the repository:

[git clone https://github.com/your-username/your-repo.git](https://github.com/Unniks-here/lambda-proxy.git)

2. Install the required dependencies:


3. Open the `lambda_function.py` file and update the `target_url` variable with your desired URL.

4. Deploy the Lambda function to AWS Lambda.

5. (Optional) Configure API Gateway to serve as an HTTP endpoint for your Lambda function.

## Usage

The Lambda function expects an event object with the following structure:

`json
{
"httpMethod": "GET",
"rawPath": "/example",
"queryStringParameters": {},
"headers": {},
"body": ""
}`

httpMethod: The HTTP method of the request.
rawPath: The raw path of the request URL.
queryStringParameters: Any query parameters passed with the request.
headers: The request headers.
body: The request body.
The function will forward the request to the specified target_url and return the response.

## Importing requests

To import the requests library in the Lambda function, follow these steps:

In the root directory of your cloned repository, create a file named **requirements.txt** if it doesn't already exist.<br>
Add the following line to **requirements.txt**:<br>
<br>
`requests`
<br><br>
When deploying the Lambda function, make sure to include the requests library in the deployment package. This can be done using various deployment methods, such as AWS CLI, AWS Management Console, or using a build system like AWS CodeBuild.
For example, if using AWS CLI, navigate to the root directory of your repository and run the following command:

`aws lambda create-function --function-name my-function --runtime python3.8 --role role-arn --handler lambda_function.lambda_handler --zip-file fileb://./lambda_function.zip --region us-west-2`

This command packages the function code and dependencies into a zip file (lambda_function.zip), which is then uploaded to AWS Lambda.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
