from urllib import request, parse

def build_url(host_name, port, path, params, fragment):
    """Builds the complete URL from given components."""
    query_string = parse.urlencode(params)
    return f"http://{host_name}:{port}{path}?{query_string}#{fragment}"

def main():
    # Define the components of the URL
    host_name = "jsonplaceholder.typicode.com"
    port = 80  # Change this to 443 if you're using HTTPS
    path = "/posts"
    fragment = "section1"

    # Create a dictionary for query parameters
    params = {
        "userId": 1
    }

    # Build the complete URL
    url = build_url(host_name, port, path, params, fragment)

    # Display the complete URL
    print("Complete URL:", url)

    # Make the GET request
    resp = request.urlopen(url)

    # Check if the response is closed
    print("Is response closed?", resp.isclosed())

    # Get and display the response code
    print("Response Code:", resp.code)

    # Read the response body
    data = resp.read()

    # Get the length of the response data
    print("Response Length:", len(data))

    # Decode the response data to HTML
    htm = data.decode("UTF-8")

    # Display the type of the HTML content
    print("Type of HTML content:", type(htm))

    # Print the HTML content
    print("HTML Content:", htm)

    # Close the response
    resp.close()

if __name__ == "__main__":
    main()
