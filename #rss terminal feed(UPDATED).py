#RSS TERMINAL FEED BOT(UPDATED)
import webbrowser

print('Select a number to open the corresponding RSS feed in your default browser:')

ans=True
while ans:
    print("""
    1. NASA image of the day
    2. PCMag best laptops
    3. Fox business
    4. MSN NFL
    5. Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans == "1":
        webbrowser.open_new_tab('https://www.nasa.gov/multimedia/imagegallery/iotd.html')
    elif ans == "2":
        webbrowser.open_new_tab("https://www.pcmag.com/picks/the-best-laptops")
    elif ans == "3":
        webbrowser.open_new_tab("https://www.foxbusiness.com/")
    elif ans == "4":
        webbrowser.open_new_tab("https://www.msn.com/en-us/sports/nfl")
    elif ans == "5":
        print("\nHave a good day/night!")
        ans = None
    else:
        print("\nInvalid choice. Please try again.")


#credit/sidenotes:
#THIS UPDATED VERISON WAS MADE WITH ASSISTANCE OF AI OF FIXING SOME OF THE ISSUES WITH IT.
#AI FIXED ERRORS, I WROTE A BIG PORTION OF THE CODE AI ONLY MADE SMALL CHANGES.