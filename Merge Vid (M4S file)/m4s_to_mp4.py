import os
import subprocess

# define a function for merge vid and aud files
def merge_files(video_path, audio_path, output_path):
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        output_path
    ]
    subprocess.run(cmd)

# main function
def main():
    lab_folder = r"C:\Users\Lenovo\Documents\Python_Project\Merge Vid (M4S file)"
    video_folder = "video"
    
    # see and find find all m4s files
    m4s_files = [filename for filename in os.listdir(lab_folder) if filename.endswith(".m4s")]
    
    if not m4s_files:
        print("bro dont play play ah i didnt found anything")
        return
    
    # loop vid and aud files (1对)
    for i in range(0, len(m4s_files), 2):
        video_path = os.path.join(lab_folder, m4s_files[i])
        audio_path = os.path.join(lab_folder, m4s_files[i + 1])
        
        # define output file name for merge
        output_filename = f"merged_output_{i // 2}.mp4"
        output_file = os.path.join(lab_folder, output_filename)
        
        try:
            # merge the vid and aud to one
            merge_files(video_path, audio_path, output_file)
            
            # create a folder to put merge vid
            if not os.path.exists(os.path.join(lab_folder, video_folder)):
                os.makedirs(os.path.join(lab_folder, video_folder))
            
            video_folder_path = os.path.join(lab_folder, video_folder)
            output_video_path = os.path.join(video_folder_path, output_filename)
            
            # same name Error dame 
            count = 1
            while os.path.exists(output_video_path):
                output_filename = f"merged_output_{i // 2}_{count}.mp4"
                output_video_path = os.path.join(video_folder_path, output_filename)
                count += 1
            
            # rename output file
            os.rename(output_file, output_video_path)
            
            # delete original vid and aud file
            os.remove(video_path)
            os.remove(audio_path)

            print(f"merge done: haha bro, im done already, pro pro leh~")
        
        except Exception as e:
            print(f"merge unsucess: sry bro, i no have strength dah QAQ\nError: {str(e)}")

if __name__ == "__main__":
    main()
