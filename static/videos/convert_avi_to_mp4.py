import moviepy.editor as mp
import os
import glob

def convert_avi_to_mp4(input_file):
    # Check if input is an AVI file
    if not input_file.endswith(".avi"):
        print("Input file must be an AVI file.")
        return
    
    # Create the output MP4 filename
    output_file = input_file.replace(".avi", ".mp4")
    
    # Load the AVI file using moviepy
    video_clip = mp.VideoFileClip(input_file)
    
    # Write the video clip to an MP4 file
    video_clip.write_videofile(output_file, codec='libx264')
    
    # Close the video clip
    video_clip.close()
    
    # Delete the original AVI file
    if os.path.exists(output_file):
        os.remove(input_file)
        print(f"{input_file} has been deleted after conversion.")
    else:
        print("Conversion failed, AVI file not deleted.")



# Convert all AVI files in the current directory to MP4
avi_files = glob.glob("./*/*.avi")

for avi_file in avi_files:
    convert_avi_to_mp4(avi_file)