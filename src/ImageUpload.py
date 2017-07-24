class ImageUpload(object):
    def __init__(self,key,event_time,customer_id,camera_make,camera_model):
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.camera_make = camera_make
        self.camera_model = camera_model

    def __str__(self):
        return "{}, {}, {}, {}".format(self.key, self.event_time, self.customer_id, self.camera_make, self.camera_model)

if __name__ == "__main__":

    # chekcing the object
    if isinstance(ImageUpload(*['1', '2017-01-06T12:46:46.384Z', '101', 'Cannon', 'D303']), ImageUpload):
        print("ImageUpload object is created with out a problem")
    else:
        print("There is problem with ImageUpload class please check !")

    # check the customer details.
    image_upload = ImageUpload(*['1', '2017-01-06T12:46:46.384Z', '101', 'Cannon', 'D303'])
    if (image_upload.key == '1') and image_upload.event_time == '2017-01-06T12:46:46.384Z' and image_upload.customer_id == \
            '101' and image_upload.camera_make == "Cannon" and image_upload.camera_model == 'D303':
        print("All ImageUpload attributes can be retrived properly")
    else:
        print("There is problem with extracting ImageUpload attributes.")