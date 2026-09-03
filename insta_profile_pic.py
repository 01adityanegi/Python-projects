import instaloader
import requests

ig = instaloader.Instaloader()

targets = [
    "adityanegi01",
    "sujal_uk01_",
    "filmmakerpriyanshu",
    "kunalrana___"
]

for username in targets:
    print("\n" + "=" * 40)
    print(f"Scanning: {username}")

    try:
        profile = instaloader.Profile.from_username(
            ig.context,
            username
        )

        print(f"Name       : {profile.full_name}")
        print(f"Followers  : {profile.followers}")
        print(f"Following  : {profile.followees}")
        print(f"Bio        : {profile.biography}")

        # Profile picture URL
        dp_url = profile.profile_pic_url

        response = requests.get(
            dp_url,
            timeout=10
        )
        response.raise_for_status()

        filename = f"{username}_dp.jpg"

        with open(filename, "wb") as file:
            file.write(response.content)

        print(f"Saved As   : {filename}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' does not exist.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading profile picture: {e}")

    except Exception as e:
        print(f"Error scanning {username}: {e}")

    print("=" * 40)
