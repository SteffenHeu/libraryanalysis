import plotly.graph_objects as go
import pandas as pn
import numpy as np
from plotly.graph_objs.histogram import XBins


# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def plot(columnName, dfs: list, numbins=None):
    fig = go.Figure()
    autobin = numbins is None if True else False
    nbins = numbins is None if None else numbins

    for df in dfs:
        fig.add_trace(go.Histogram(x=df.get(columnName), name=df.name,
                                   nbinsx=nbins, autobinx=autobin))

    fig.update_traces(opacity=0.4)
    fig.update_layout(title_text=columnName, yaxis_title_text="Count",
                      barmode='overlay')
    fig.show()

def print_hi():
    min2 = pn.read_csv('D:/sciebo/Promotion/Auswertungen/20221027 - Mastermodul/20221014 - Pigmente/positiv/min2.csv',
                       sep=';')
    min3 = pn.read_csv('D:/sciebo/Promotion/Auswertungen/20221027 - Mastermodul/20221014 - Pigmente/positiv/min3.csv',
                       sep=';')
    min4 = pn.read_csv('D:/sciebo/Promotion/Auswertungen/20221027 - Mastermodul/20221014 - Pigmente/positiv/min4.csv',
                       sep=';')
    standard = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/20221027 - Mastermodul/20221014 - Pigmente/positiv/standard.csv',
        sep=';')

    min2 = min2[min2['num_peaks'] != 1]
    min3 = min3[min3['num_peaks'] != 1]
    min4 = min4[min4['num_peaks'] != 1]
    standard = standard[standard['num_peaks'] != 1]

    min2.name = "min2"
    min3.name = "min3"
    min4.name = "min4"
    standard.name = "standard"

    dfs = [standard, min2, min3, min4]

    plot('explained_intensity', dfs, 20)
    plot('explained_peaks', dfs, 20)
    plot('num_peaks', dfs)
    plot('spectral_entropy', dfs)
    plot('normalized_entropy', dfs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
