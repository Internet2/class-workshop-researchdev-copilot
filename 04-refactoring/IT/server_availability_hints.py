import datetime
from mock_ping import mock_ping
from io import StringIO

def check_server_availability(servers):
    # No input validation or type hints

    try:
        output = StringIO()
        
        # Write header with timestamp
        output.write(f"Time: {datetime.datetime.now()}\n")
        
        for s in servers:  # Poor variable naming
            try:
                # Ignores all the rich information from mock_ping
                # and reduces it to just True/False
                result = mock_ping(s)
                if result == True:  # Non-pythonic comparison
                    f.write(s + " is up\n")
                else:
                    # Ambiguous error messaging
                    f.write(s + " is down\n")
            except:  # Bare except clause
                # Generic error message without context
                f.write("Error checking server\n")
        
        f.close()  # Manual file closing
    except:  # Another bare except
        # Unhelpful error message
        print("Error writing to log file")  # Inconsistent error reporting (print vs write)
        return  # Silent return on error