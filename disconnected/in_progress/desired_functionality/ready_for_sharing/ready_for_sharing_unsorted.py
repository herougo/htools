######################################################
# PROPER API #########################################
######################################################

class AutomatedEmailSender:
    def __init__(self, from_address):
        self._from = from_address
        self._emails = []

    def add_emails(self, to_emails, subjects, bodies):
        self._emails += list(zip(to_emails, subjects, bodies))
    
    def send_emails(self, password):
        # (implement me) ???? for to_email, subject, body in self._emails:
        del password

    def create_drafts(self, password):
        # (implement me) ???? for to_email, subject, body in self._emails:
        del password

######################################################
# INCOMPLETE API #####################################
######################################################

# DOWNLOADING

def get_youtuber_video_urls(youtuber_id):
    pass

def download_youtube_video(url, file_path):
    pass
    
def get_reddit_posts(subreddit_name):
    pass

def download_imgur_image(url):
    pass

# VIRTUAL ENVIRONMENT

def get_virtual_env():
    pass

def interact_with_environment():
    env = get_virtual_env()
    objects = env.get_all_objects()
    camera_position = env.get_camera_position()
    for obj in objects:
        skeleton = obj.skeleton
    env.place_object(obj, location)
    observations = env.step('turn_left')
    (
        (RGBD, normal_vectors, segmentation, bounding_boxes, 
         bounding_box_labels), # left
        (r_RGBD, r_normal_vectors, r_segmentation, r_bounding_boxes,
         r_bounding_box_labels) # right
    ) = observations

# OTHER

def execute_script(script_path):
    # execute .sh script
    pass

def print_n_decimal_places(decimal, n_decimal_places):
    pass

def mouse_left_click(x, y):
    pass



