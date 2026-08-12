from fastmcp import FastMCP

mcp = FastMCP(name = 'Travel Agent')

@mcp.tool
def get_weather():
    """ Weather of given location """
    return {'location' : ' Hyderabad', 'weather' : 'Sunny', 'temperature':30}

@mcp.tool
def get_flights():
    """ The Flights from Hyderabad to Mumbai on August 15th 2026 """
    return {'Departure' : 'Hyderabad', 'Arrival' : 'Mumbai', 'price':5000, 'available_seats':50}

@mcp.tool
def get_hotels():
    """ The Hotels in Hyderabad """
    return {'hotel' : 'Taj Hotel', 'price':10000, 'available_rooms':50}

@mcp.tool
def get_date():
    """Date of flight"""
    return {'date' : '2022-12-31'}

@mcp.tool
def get_budget():
    """Budget of the user"""
    return {'budget' : 20000}

if __name__ == '__main__':
    mcp.run()