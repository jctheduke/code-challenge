class ImageUpload(object):
    def __init__(self,key,event_time,customer_id,camera_make,camera_model):
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.camera_make = camera_make
        self.camera_model = camera_model

    def __str__(self):
        return "{}, {}, {}, {}".format(self.key, self.event_time, self.customer_id, self.camera_make, self.camera_model)
