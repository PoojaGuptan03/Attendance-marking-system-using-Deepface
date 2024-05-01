from deepface import DeepFace
import os
entries = os.listdir("C:/Users/coolp/Desktop/face recog/db")
def ver(im_list):
    verified_files = set()
    not_verified = set()
    for i in im_list:
        for entry in entries:
            entry_name, _ = os.path.splitext(entry) 
            if entry_name not in verified_files: 
                r = DeepFace.verify(img1_path=i, img2_path=os.path.join("C:/Users/coolp/Desktop/face recog/db", entry), model_name='DeepID')
                if r['verified']:
                    verified_files.add(entry_name)
                    not_verified.add(entry_name)
                else:
                    not_verified.add(entry_name)
            else:
                continue
    return verified_files,not_verified-verified_files