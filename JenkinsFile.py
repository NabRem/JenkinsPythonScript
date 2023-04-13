import random

def generateDummyData(stage, successRate):
    print(f"Generating data for {stage} stage...")
    if random.random() < successRate:
        data = {
            "status": "success",
            "message": f"{stage} stage succeeded"
        }
        return data
    else:
        data = {
            "status": "failure",
            "message": f"{stage} stage failed"
        }
        return None