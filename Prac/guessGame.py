# import random;



# i=1;
# score1_Hum=0;
# score2_Com=0;
# for i in range(5):
#     print("Guess The Number From 1 to 10")
#     num1=random.randrange(1,11);
#     num2=int(input());

#     print("Your Guess Is: ",num2)
#     print("Computer Guess Is: ",num1)
    
#     if num1>num2:
#         score2_Com+=1
#     elif num1<num2:
#         score1_Hum+=1
        
            

# if score1_Hum>score2_Com:
#     print("Human Wim the game🥳")
#     print("Human Score: ",score1_Hum,"Computer Score: ",score2_Com);
    
# elif score1_Hum<score2_Com:
#     print("Computer Wim the game🥳")
#     print("Human Score: ",score1_Hum,"Computer Score: ",score2_Com);   
# else :
#     print("Match is Draw")
#     print("Human Score: ",score1_Hum,"Computer Score: ",score2_Com);    


# from pytube import YouTube
# YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.streams.filter(progressive=True, file_extension='mp4') .order_by('resolution') .desc() .first() .download() 


from pytube import YouTube

# def download_video():
#     try:
#         url = input("Enter the YouTube video URL: ")
#         yt = YouTube(url)
#         print(f"\nTitle: {yt.title}")
#         print("Downloading...")

#         # Get the highest resolution progressive stream (includes video + audio)
#         stream = yt.streams.filter(progressive=True, file_extension='mp4') \
#                            .order_by('resolution') \
#                            .desc() \
#                            .first()

#         stream.download()
#         print("✅ Download completed!")

#     except Exception as e:
#         print("❌ An error occurred:", e)

# if __name__ == "__main__":
#     download_video()



from pytube import YouTube

def download_video():
    try:
        raw_url = input("Enter the YouTube video URL: ")
        # url = raw_url.split("&")[0].split("?")[0]  # Clean the URL
        yt = YouTube(raw_url)

        print(f"\nTitle: {yt.title}")
        print("Downloading...")

        stream = yt.streams.filter(progressive=True, file_extension='mp4') \
                           .order_by('resolution') \
                           .desc() \
                           .first()

        stream.download()
        print("✅ Download completed!")

    except Exception as e:
        print("❌ An error occurred:", e)

if __name__ == "__main__":
    download_video()