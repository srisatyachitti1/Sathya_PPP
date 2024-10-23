from urllib import request
from urllib.error import HTTPError, URLError


def main():
    # Define the components of the URL
    host_name = "10.10.10.61"
    port = 8081
    path = "/qm/cam/api/accounts/getAccountById/26862"

    # Construct the complete URL
    url = f"http://{host_name}:{port}{path}"

    # Display the complete URL
    print("Complete URL:", url)

    # Make the GET request
    try:
        resp = request.urlopen(url)

        # Check if the response is closed
        print("Is response closed?", resp.isclosed())

        # Get and display the response code
        print("Response Code:", resp.code)

        # Read the response body
        data = resp.read()

        # Get the length of the response data
        print("Response Length:", len(data))

        # Decode the response data to JSON or text
        response_content = data.decode("UTF-8")

        # Display the type of the response content
        print("Type of Response Content:", type(response_content))

        # Print the response content
        print("Response Content:", response_content)

    except HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
    except URLError as e:
        print(f"URL error occurred: {e.reason}")

if __name__ == "__main__":
    main()
