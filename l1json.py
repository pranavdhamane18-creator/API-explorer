import requests
def fetch_post(post_id):
    url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response=requests.get(url,timeout=5)
        response.raise_for_status()
        data=response.json()
        if not isinstance(data,dict):
            print("Invalid response format")
            return None
        required={"userId","id","title","body"}
        if not required.issubset(data.keys()):
            print("Required fields missing")
            return None
        return(data)
    except requests.exceptions.JSONDecodeError as e:
        print("JSON decode failed: ",e)
        return None
    except requests.exceptions.HTTPError as e:
        print("Request failed: ",e)
        return None
    except requests.exceptions.RequestException as e:
        print("Connection error: ",e)
        return None
def fetch_todos(user_id):
    url=f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    try:
        response=requests.get(url,timeout=5)
        response.raise_for_status()
        data=response.json()
        if not isinstance(data,list):
            print("Invalid response format")
            return None
        if data:
            required={"userId","id","title","completed"}
            for entry in data:
                if not isinstance(entry,dict):
                    print("Invalid entry in list")
                    return None
                if not required.issubset(entry.keys()):
                    print("Required fields are missing")
                    return None
        return data
    except requests.exceptions.JSONDecodeError as e:
        print("Failed to decode JSON",e)
        return None
    except requests.exceptions.HTTPError as e:
        print("Request failed",e)
        return None
    except requests.exceptions.RequestException as  e:
        print("Connection failed",e)
        return None
def main():
    choice=0
    while True:
        print("-----Menu-----")
        print("1.Fetch a post by ID.")
        print("2.Fetch todos by user ID.")
        print("3.Exit.")
        try:
            choice=int(input("Enter a valid choice number"))
        except ValueError as e:
            print("Invalid choice",e)
        else:
            if not 0<choice<4:
                print("Invalid choice")
            else:
                match choice:
                    case 1:
                        try:
                            x=int(input("Enter a valid ID"))
                            if x<=0:
                                print("ID should be positive")
                            else:
                                post=fetch_post(x)
                                if post is None:
                                    print("Failed!")
                                else:
                                    print("ID=",post["id"])
                                    print("Title:",post["title"])
                                    print("Body:",post["body"])
                        except ValueError as e:
                            print("Invalid ID")
                    case 2:
                        try:
                            x=int(input("Enter a valid user ID"))
                            if x<=0:
                                print("ID should be positive")
                            else:
                                todos=fetch_todos(x)
                                if todos is None:
                                    print("Failed!")
                                else:
                                    if todos:
                                        for entry in todos:
                                            print("ID=",entry["id"])
                                            print("Title:",entry["title"])
                                            print("Completed status:",entry["completed"])
                                    else:
                                        print("No todos found for the user")
                        except ValueError as e:
                            print("Invalid ID")
                    case 3:
                        print("Program exitted succesfully")
                        break
            print(" ")
if __name__ == "__main__":
    main()