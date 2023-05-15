## Introduction

The aim of this project is to help us explore different locations like neighborhoods by gathering information on the surrounding areas and the most popular venues. To achieve this task, we will be utilizing a tool called Foursquare.

Foursquare is a location-based social networking platform that allows users to discover and share information about nearby places. Users can use the Foursquare mobile app to check in at a location, share tips and reviews, and discover new places based on their location and interests. Foursquare also offers personalized recommendations based on a user's check-in history and preferences.

The Foursquare API is a set of tools and resources provided by Foursquare that allows developers to integrate location-based data into their applications. The API provides access to a wide range of location-based data, including venue details, user check-ins, and ratings. Developers can use this data to build a variety of applications, such as location-based recommendations, social networking apps, and more. The Foursquare API is available in both free and paid tiers, with different levels of access and features depending on the plan.

After creating a Foursquare developer account and obtaining your credentials (which we will explain how to do later), it becomes simple to explore a specific location. By setting the URL in the following example and sending a GET request, you can retrieve data on the venues in that location, which will be returned in JSON format.

> https://api.foursquare.com/v2/venues/explore?client_id=**CLIENT_ID**&client_secret=**CLIENT_SECRET**&ll=**LATITUDE**,**LONGITUDE**&v=**VERSION**&limit=**LIMIT**

Theh URL request contain:

- The client credentials.
- The API version (set it to 20180605)
- The location geo-coordination
- Radius of the search in meters
- Limit: the minimium number of venues to retrieve.

Here's an example of what the results:

```python
import requests

results = requests.get(url).json()
items = results['response']['groups'][0]['items']
items[0]
```
![JSON output](json_output.png)

## Task

The primary objective is to develop a Python-based command-line interface (CLI) that can receive an address and the number of venues to collect. The CLI should then use the Foursquare API to obtain the data and store the results in a SQL-like database.

- Regarding the information to be saved, you have the option to store either all the data returned or select specific details, such as the venue's name, category, address, city, or any other relevant information you deem necessary.
- Create a database via SQLModel
- try to keep code modular and functions short.

## Additional reading

- The [argparse](https://docs.python.org/3/library/argparse.html) module makes it easy to write user-friendly command-line interfaces.
- To obtain Foursquare credentials follow these steps:
    1- Go to your "App Settings" page on the developer console of Foursquare.com
    2- Set the "Redirect URL" under "Web Addresses" to https://www.google.com
    3- Paste and enter the following url in your web browser (replace YOUR_CLIENT_ID with your actual client id): https://foursquare.com/oauth2/authenticate?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=https://www.google.com
    This should redirect you to a google page requesting permission to make the connection.
    4- Accept and then look at the url of your web browser (take note at the CODE part of the url to use in step 5) It should look like https://www.google.com/?code=CODE
    5- Copy the code value from the previous step. Paste and enter the following into your web browser (replace placeholders with actual values): https://foursquare.com/oauth2/access_token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&redirect_uri=https://www.google.com&code=CODE.
    6- When you paste the link , This should lead you to a page that gives you your access token.