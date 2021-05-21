import plotly.graph_objects as go
x = [1, 2, 3, 4]

fig = go.Figure()
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], marker_color='deepskyblue', name='True Positive'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], marker_color='lightslategrey', name='False Positive'))
fig.add_trace(go.Bar(x=x, y=[-15, -3, -4.5, -8], marker_color='crimson', name='False Negative'))

fig.update_layout(barmode='relative', title_text='Confusion Matrix Graph')
fig.show()