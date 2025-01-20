from typing import Union, Optional
from dataclasses import dataclass
from enum import Enum
import time

class ServerStatus(Enum):
    UP = "UP"
    DOWN = "DOWN"
    TIMEOUT = "TIMEOUT"
    DNS_ERROR = "DNS_ERROR"
    UNAUTHORIZED = "UNAUTHORIZED"

@dataclass
class PingResult:
    status: ServerStatus
    response_time: float
    error_message: Optional[str] = None

    def __bool__(self):
        return self.status == ServerStatus.UP

class MockPingError(Exception):
    """Base exception for mock ping errors"""
    pass

class MockDNSError(MockPingError):
    """Raised when DNS resolution fails"""
    pass

class MockTimeoutError(MockPingError):
    """Raised when ping times out"""
    pass

class MockAuthenticationError(MockPingError):
    """Raised when authentication is required but not provided"""
    pass

def mock_ping(server: str, timeout: float = 1.0, require_auth: bool = False) -> PingResult:
    """
    Simulates pinging a server with various realistic scenarios
    
    Args:
        server: Server address to ping
        timeout: Maximum time to wait for response
        require_auth: Whether authentication is required
        
    Returns:
        PingResult object containing status and response information
        
    Raises:
        MockDNSError: If DNS resolution fails
        MockTimeoutError: If ping times out
        MockAuthenticationError: If authentication is required but not provided
        ValueError: If server parameter is invalid
    """
    if not isinstance(server, str):
        raise ValueError(f"Server must be a string, got {type(server).__name__}")
        
    if not server:
        raise ValueError("Server address cannot be empty")

    if server.startswith("timeout"):
        time.sleep(timeout + 0.1)
        raise MockTimeoutError(f"Connection to {server} timed out after {timeout} seconds")
        
    if server.startswith("auth") and not require_auth:
        raise MockAuthenticationError(f"Authentication required for {server}")
        
    if ".invalid" in server:
        raise MockDNSError(f"Could not resolve hostname: {server}")

    mock_responses = {
        "192.168.1.1": PingResult(ServerStatus.UP, 0.001),
        "example.com": PingResult(ServerStatus.DOWN, 0.0, "Connection refused"),
        "localhost": PingResult(ServerStatus.UP, 0.0001),
        "slow.server": PingResult(ServerStatus.UP, 0.8),
        "firewall.blocked": PingResult(ServerStatus.DOWN, 0.001, "Connection blocked by firewall")
    }

    response_time = timeout * 0.1

    return mock_responses.get(
        server,
        PingResult(ServerStatus.DOWN, response_time, f"Unknown host: {server}")
    )