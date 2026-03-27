import pandas as pd
import plotly.express as px

# Create dataset
data = {
    "Epoch": list(range(1, 11)),
    "Training Loss": [0.95, 0.82, 0.68, 0.55, 0.47, 0.42, 0.40, 0.39, 0.39, 0.38]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create line chart
fig = px.line(
    df,
    x="Epoch",
    y="Training Loss",
    title="Training Loss Over Epochs",
    labels={
        "Epoch": "Epoch",
        "Training Loss": "Loss"
    },
    markers=True
)

# Add annotation where loss stabilizes
fig.add_annotation(
    x=7,
    y=0.40,
    text="Loss starts stabilizing here",
    showarrow=True,
    arrowhead=2
)

# Display chart
fig.show()