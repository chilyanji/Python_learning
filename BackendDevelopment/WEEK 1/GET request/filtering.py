import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()

    # for user in users:
    #     if "South" in user["address"]["city"]:
    #         print(
    #             f"{user['name']} lives in {user['address']['city']} ")
    count = {}
    for user in users:
        city = user["address"]["city"]

        # if city in count:
        #     count[city] += 1
        # else:
        #     count[city] = 1

        count[city] = count.get(city, 0) + 1    # we can write this line to avoide if/else #
    print(count)
else:
    print(f"Error: {response.status_code}")


# Expected output:
# Patricia Lebsack lives in South Elvis
# Mrs. Dennis Schulist lives in South Christy
# Challenge: Count Users Per City