from deepface import DeepFace
def get_distance(img1:str,img2:str):
    result = DeepFace.verify(img1_path = img1, img2_path = img2, distance_metric = 'cosine')
    print(result)
    return result