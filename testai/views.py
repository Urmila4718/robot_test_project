from django.http import JsonResponse
import json
import subprocess
from django.views.decorators.csrf import csrf_exempt

# testai/views.py


@csrf_exempt
def execute_test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tests = data.get('tests', [])

        # Create a new Robot Framework test suite file
        with open('test_suite.robot', 'w') as f:
            f.write('*** Settings ***\nLibrary    SeleniumLibrary\n\n')
            f.write('*** Test Cases ***\n')
            for test in tests:
                title = test.get('title', '')
                steps = test.get('steps', [])

                # Write the test case to the file
                f.write(f'{title}\n')
                f.write(f'    [Documentation]    Test case to open {title}\n')
                for step in steps:
                    # Remove quotes from the step
                    step = step.replace('\'', '')
                    if step.startswith('Open Browser'):
                        step = step.replace('Open Browser', 'Open Browser\t\t\t\t', 1)
                    elif step.startswith('Go To'):
                        step = step.replace('Go To', 'Go To\t\t\t\t', 1)
                    f.write(f'    {step}\n')

        # Execute the Robot Framework test suite
        result = subprocess.run(['robot', 'test_suite.robot'], stdout=subprocess.PIPE)

        # Capture the output of the test execution
        output = result.stdout.decode('utf-8')

        # Return the output in the API response
        return JsonResponse({'output': output})
