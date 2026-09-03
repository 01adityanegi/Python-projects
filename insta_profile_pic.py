import instaloader
import requests

ig = instaloader.Instaloader()
targets = ["adityanegi01" , "sujal_uk01_", "filmmakerpriyanshu","kunalrana___"] //instragram username 

for username in targets:
    print(f"\n{'='*40}")
    print(f"Scanning :{username}")

    profile = instaloader.Profile.from_username(ig.context, username)

     print(f"Name : {profile.full_name}")
    print(f"Followers : {profile.followers}")
    print(f"Following : {profile.followees}")
    print(f"Bio : {profile.biography}")

    dp_url= profile.profile_pic_url
    response = requests.get(dp_url)

    with open(f"{username}_dp.jpg","wb") as file:
        file.write(response.content)

    print(f"Saved As : {username}_dp.jpg")
    print(f"{'=*40'}")
