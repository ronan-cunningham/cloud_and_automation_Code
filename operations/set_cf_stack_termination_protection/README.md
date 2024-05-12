# Turning on  termination protection for existing CloudFormation stacks using Python Boto3

My approach here is to use an inline Lambda as the code is relatively simple and does not require installing non-default modules.

A CloudWatch events rule triggers the function daily. It:

- loops through the configured regions in the AWS account the lambda runs in
- gets a list of all CloudFormation stacks in each region in a state where the stack can be updated.
- creates a sub-list of stacks that are not part of a nested CloudFormation stack 
- turns on termination protection for the stack.

The code does not check if it is already turned on for the stack. The update function passes if it is already on and this is fairly computationally inexpensive.