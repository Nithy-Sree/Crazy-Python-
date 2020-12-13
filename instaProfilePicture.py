import instaloader

# load instagram
mod = instaloader.Instaloader()

# enter username of the account(to get profile picture)
a = input("Name of the user --> ")

# download the picture with the folder
mod.download_profile(a, profile_pic_only = True)
