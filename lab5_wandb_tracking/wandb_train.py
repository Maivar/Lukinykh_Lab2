import wandb
wandb.init(project="wandb_mnist", config={"epochs": 5})
for i in range(5):
    wandb.log({"accuracy": 0.8 + i*0.02})
