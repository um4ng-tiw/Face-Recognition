from PIL import Image
import face_recognition

# Load the document
document = face_recognition.load_image_file("me_id.jpeg")

#find the face location in document
face_locations = face_recognition.face_locations(document)


print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = document[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()


# Load the selfie
unknown_image = face_recognition.load_image_file("me.jpeg")


known_encoding = face_recognition.face_encodings(face_image)

try:

    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    print(unknown_encoding)
    results = face_recognition.compare_faces(known_encoding, unknown_encoding)
    

    if results and results[0] == True:
        print("Picture matched")
    else:
        print("No match")

except IndexError:
    print("Oops ! Face not found")


