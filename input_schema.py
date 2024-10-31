INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["A cat holding a sign that says hello world"]
    },
     "workflow": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://github.com/ash368/ComfyUI-Inferless-template/raw/main/workflows/workflow.json"]
    },
    "negative_prompt": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["blurry, illustration, toy, clay, low quality, flag, nasa, mission patch"]
    }
}
