import instaloader
import csv

with open("alfred.csv", "r") as list_file:
    with open("new_alfred.csv", "w") as new_file:
        csv_reader = csv.reader(list_file, delimiter = ",")
        csv_writer = csv.writer(new_file)
        username=""
        for row in csv_reader:
            if row[3] == "IG":
                csv_writer.writerow(row)
            else:
                del row[-1]
                username=row[3]
                L=instaloader.Instaloader(dirname_pattern="img",title_pattern=username,save_metadata=False,compress_json=False)
                profile=instaloader.Profile.from_username(L.context, username)
                biography=profile.biography
                csv_writer.writerow(row+[biography])
                print(L.download_profile(username,profile_pic_only=True))