#RSS/WEBSITE TERMINAL FEED/MANAGER BOT(UPDATED)

import webbrowser

feeds = {
    "1": "https://www.nasa.gov/multimedia/imagegallery/iotd.html",
    "2": "https://www.pcmag.com/picks/the-best-laptops",
    "3": "https://www.foxbusiness.com/",
    "4": "https://www.msn.com/en-us/sports/nfl"
}

def edit_list():
    print("Edit List:")
    print("1. Add new feed")
    print("2. Remove existing feed")
    ans = input("What would you like to do? ")
    if ans == "1":
        feed_name = input("Enter the name of the feed: ")
        feed_url = input("Enter the URL of the feed: ")
        feeds[feed_name] = feed_url
    elif ans == "2":
        feed_name = input("Enter the name of the feed you want to remove: ")
        feeds.pop(feed_name, None)
    else:
        print("Invalid choice. Please try again.")

print('Select a number to open the corresponding RSS feed in your default browser:')
ans=True
while ans:
    print("""
    1. NASA image of the day
    2. PCMag best laptops
    3. Fox business
    4. MSN NFL
    5. Edit List
    6. Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans in feeds:
        webbrowser.open_new_tab(feeds[ans])
    elif ans == "5":
        edit_list()
    elif ans == "6":
        print("\nHave a good day/night!")
        ans = None
    else:
        print("Invalid choice. Please try again.")



#CREDIT/SIDENOTES:
#THIS UPDATED VERISON WAS MADE WITH ASSISTANCE OF AI OF FIXING SOME OF THE ISSUES WITH IT.
#AI FIXED ERRORS, AND ADDED THE EDIT FUCTION TO MAKE CHANGES EASIER. AI DID THOSE PARTS, THE REST WAS ALL ME.
