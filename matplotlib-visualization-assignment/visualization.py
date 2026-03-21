import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame({
    "epoch":range(1,11),
    "loss":[0.9,0.8,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.33]
})

#line plot 
plt.figure(figsize=(10, 5))
plt.plot(df["epoch"], df["loss"])
plt.xlabel("epoch")
plt.ylabel("loss")
plt.title("Epoch vs Loss")

# As I am using linux so saving the file instead of just showing. :) 
plt.savefig("matplotlib-visualization-assignment/line_plot.png")
plt.show()


# scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(df["loss"], df["epoch"])
plt.xlabel("loss")
plt.ylabel("epoch")
plt.title("Loss vs Epoch")
plt.savefig("matplotlib-visualization-assignment/scatter_plot.png")
plt.show()

# bar plot\
accuracy = pd.DataFrame({

    "model": ["model1", "model2", "model3"],
    "accuracy":[0.85,0.9,0.88]
})

plt.figure(figsize=(10, 5))
plt.bar(accuracy["model"], accuracy["accuracy"])
plt.xlabel("model")
plt.ylabel("accuracy")
plt.title("Model vs Accuracy")
plt.savefig("matplotlib-visualization-assignment/bar_plot.png")
plt.show()
