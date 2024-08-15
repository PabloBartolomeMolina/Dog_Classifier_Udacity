# Description
Project in Python to use a Classifier so a set of images of pets are classified between dogs and not dogs. Also, dogs are classified by breed.
Done in the context of a Udacity's Nanodegree "AI Programming with Python"
Three different CNN model architectures are available: Alexnet, Resnet and VGG.

# Run the project
You can run the project with a console command `python check_images.py`. It will run the program with default parameters, but you can also specify the directory with images, the file with dognames to use, and the CNN model to use.

You can run all 3 CNN models by using the terminal command `sh run_models_batch.sh` or `sh run_models_batch_uploaded.sh` to use the directory uploaded_images in which you can place your images. The difference between both commands is the directory of image to be used as input.

# Dependencies
* Pillow==10.4.0
* torch==2.4.0
* torchvision==0.19.0


# Possible improvements
- [ ] Cleaner code.
- [ ] Improve efficiency.
- [ ] Update classifier to latests available versions.
