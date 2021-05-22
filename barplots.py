import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('cf_norm_sim.csv')

a = 0.2
b = 0.8

threshold_val = a
threshold_val_second = (3*a+b)/4

# confusion matrix corresponding to a
fp_confusion = df.loc[df["threshold"] == threshold_val, "fp"]
tp_confusion = df.loc[df["threshold"] == threshold_val, "tp"]
fn_confusion = df.loc[df["threshold"] == threshold_val, "fn"]

fp_confusion_second = df.loc[df["threshold"] == threshold_val_second, "fp"]
tp_confusion_second = df.loc[df["threshold"] == threshold_val_second, "tp"]
fn_confusion_second = df.loc[df["threshold"] == threshold_val_second, "fn"]

x = ["a", "(3a+b)/4"]

fig = go.Figure()

fig.add_trace(go.Bar(x=x, y=[tp_confusion.iat[0], tp_confusion_second.iat[0]], marker_color='deepskyblue', name='True Positive'))
fig.add_trace(go.Bar(x=x, y=[fp_confusion.iat[0], fp_confusion_second.iat[0]], marker_color='lightgrey', name='False Positive'))
fig.add_trace(go.Bar(x=x, y=[(fn_confusion.iat[0]*-1), (fn_confusion_second.iat[0]*-1)], marker_color='crimson', name='False Negative'))

fig.update_layout(barmode='relative', title_text='Confusion Matrix Graph')
fig.show()