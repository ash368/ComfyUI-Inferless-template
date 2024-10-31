# ComfyUI-Inferless-template
Welcome to an immersive tutorial that guides you through leveraging the power of ComfyUI's API capabilities and deploying your workflows on Inferless. This resource is designed to help you create and deploy custom workflows, extending ComfyUI's API functionality. You'll learn how to interact with ComfyUI and deploy on Inferless.

## Architecture
<img width="1336" alt="image" src="https://github.com/user-attachments/assets/d1d23b2d-940f-40ee-8418-2771e35591f3">

---
## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the app.py according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

  ---
## Quick Start
Here is a quick start to help you get up and running with this template on Inferless.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Create a Custom Runtime in Inferless
To access the custom runtime window in Inferless, simply navigate to the sidebar and click on the Create new Runtime button. A pop-up will appear.

Next, provide a suitable name for your custom runtime and proceed by uploading the inferless-runtime.yaml file given above. Finally, ensure you save your changes by clicking on the save button.

### Add Your Hugging Face Access Token and NFS Volume
Add the `NFS_VOLUME` Volume path and the `HF_TOKEN` Hugging Face access token as a environment variables.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the Add Model button.

Select the GitHub as a model provider and choose **Repo(custom code)** as your model source and select the branch.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/github-custom-code) for more information on model import.

---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu.

For more information refer to the [Inferless docs](https://docs.inferless.com/).
