from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
    try:
        # Get the video from the URL
        url = request.form["url"]
        yt = YouTube(url)

        # Get the highest quality video stream available
        video = (
            yt.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )

        # Download the video to the current directory
        video.download()

        message = "Video downloaded successfully"

    except Exception as e:
        message = "An error occurred while downloading the video"
        print(e)

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
