# importing Flask and other modules
from flask import Flask, request, render_template, send_file
import youtube_dl

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def yt2mp3():
    if request.method == "POST":
        link = request.form.get("YoutubeLink")
        video_url = link
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=video_url, download=False
        )

        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename
        }

        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                print("Attempting download... \n")
                ydl.download([video_info['webpage_url']])

        except Exception as e:
            print("Fatal Error Occurred! Code: " + str(e))
        # return "Your link is " + link

        return send_file(filename, as_attachment=True)
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
