import pandas as pd
import plotly.express as pe

reader = pd.read_csv("Studentlevel.csv")
student_attempt = reader.loc[reader['student_id'] == 'TRL_253']
groups = student_attempt.groupby('level')['attempt'].mean()
figure = pe.Figure(pe.Scatter(
    x=groups,y=['Level 1','Level 2','Level 3','Level 4'],
    orientation = 'h'))

figure.show()