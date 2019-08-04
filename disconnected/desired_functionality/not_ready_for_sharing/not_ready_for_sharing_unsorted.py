# ML

def ocr(img):
    pass

def get_pytorch_datasets():
    pass

def fake_pytorch_model(dataset):
    pass

def fake_pytorch_trainer(model, dataset):
    pass

def check_pytorch_datasets():
    pytorch_datasets = get_pytorch_datasets()
    for ds in pytorch_datasets:
        dataset = Dataset.from_existing_object(ds)
        model = fake_pytorch_model(dataset)
        trainer = fake_pytorch_trainer(model, dataset)
        trainer.something()

def get_tensorflow_datasets():
    pass

def fake_tensorflow_model(dataset):
    pass

def fake_tensorflow_trainer(model, dataset):
    pass

def check_tensorflow_datasets():
    tensorflow_datasets = get_tensorflow_datasets()
    for ds in tensorflow_datasets:
        dataset = Dataset.from_existing_object(ds)
        dataset.download()
        model = fake_tensorflow_model(dataset)
        trainer = fake_tensorflow_trainer(model, dataset)
        trainer.something()

def get_gym_environments():
    pass

def check_gym_environments():
    gym_envs = get_gym_environments()
    for env in gym_envs:
        model = fake_model(env)
        trainer = fake_trainer(model, dataset)
        trainer.something()

# OTHER


def rotate_matrix(mat):
    pass

def backup_to_google_drive(file_path, **kwargs):
    pass

def pdf_to_list_of_images(pdf_path):
    pass

def send_image_via_flask(image_path):
    pass

def parse_research_paper_pdf(pdf_path):
    pass