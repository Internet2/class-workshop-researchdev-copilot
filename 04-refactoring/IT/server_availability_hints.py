import datetime
from mock_ping import mock_ping
from io import StringIO

def check_server_availability(servers):
    output = StringIO()
    
    # Write header with timestamp
    output.write(f"Time: {datetime.datetime.now()}\n")
    
    # Check each server
    for server in servers: # Poor variable naming
        try:
            # Ignores all the rich information from mock_ping
            # and reduces it to just True/False
            result = mock_ping(server)
            status = "UP" if result else "DOWN"
            output.write(f"{server} is {status}\n")
        except: # Bare except clause
            output.write(f"Error checking server {server}\n")   # Generic error message without context
    
    # Print and return the complete output
    result = output.getvalue()
    print(result)
    return