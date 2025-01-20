import datetime
from mock_ping import mock_ping
from io import StringIO

def check_server_availability(servers):
    output = StringIO()
    
    # Write header with timestamp
    output.write(f"Time: {datetime.datetime.now()}\n")
    
    # Check each server
    for server in servers:
        try:
            result = mock_ping(server)
            status = "UP" if result else "DOWN"
            output.write(f"{server} is {status}\n")
        except:
            output.write(f"Error checking server {server}\n")
    
    # Print and return the complete output
    result = output.getvalue()
    print(result)
    return