#RSS feed manager in terminal

import webbrowser

print('this may not work properly please select a number')

ans=True
while ans:
    print("""
    1.NASA image of the day
    2.pcmag best laptops
    3.Fox business
    4.msn nfl  
    5.Exit/Quit



    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      webbrowser.open_new_tab('https://www.nasa.gov/multimedia/imagegallery/iotd.html')
      webbrowser.open_new_tab("\n https://www.pcmag.com/picks/the-best-laptops")
    elif ans=="3":
      webbrowser.open_new_tab("\n https://www.foxbusiness.com/")
    elif ans=="4":
      webbrowser.open_new_tab("\n https://www.msn.com/en-us/sports/nfl ")
 
    elif ans=="5":
      print("\n have a good day/night!") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
       