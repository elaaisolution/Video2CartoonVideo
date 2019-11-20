# Video2CartoonVideo
*To Transform the video file to cartoon video*
## Sample Script to convert Video to Cartoon 
### Just follow bellow steps:
* Create a input directory
* Create a output directory
* Paste input from input directory
* Run Python Script

# Example

    video_in, video_out = sys.argv[1], sys.argv[2]
    start_sec = int(sys.argv[3])
    end_sec = int(sys.argv[4])
    cartoonize(video_in, video_out, start_sec, end_sec)

# Comment line argument 

 **python3 CartoonVideo.py /input/sample.mp4 /output/cartoon.mp4  0 10**

# Input
![](/input/sample.mp4)

# Output
![](/output/cartoon.mp4)
