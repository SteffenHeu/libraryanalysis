import plotly.graph_objects as go
import pandas as pn
import numpy as np
import kaleido
import seaborn as sns
import matplotlib.pyplot as plt
from plotly.graph_objs.histogram import XBins


# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def plotSnsHist(columnName, dfs: list, numBins=None):
    numBins = 'auto' if numBins is None else numBins
    for df in dfs:
        sns.histplot(data=df, x=columnName, bins=numBins, element="step", fill=False,
                     label=df.name + ' (' + str(len(df)) + ')')
    plt.legend()
    plt.savefig(columnName + '.png')
    # plt.show()
    plt.close()


def plot(columnName, dfs: list, numbins=None):
    fig = go.Figure()
    autobin = numbins is None if True else False
    nbins = numbins is None if None else numbins

    for df in dfs:
        fig.add_trace(go.Histogram(x=df.get(columnName), name=df.name + ' (' + str(len(df)) + ')',
                                   nbinsx=nbins, autobinx=autobin))

    fig.update_traces(opacity=0.4)
    fig.update_layout(title_text=columnName, yaxis_title_text="Count", xaxis_title_text=columnName,
                      barmode='overlay'
                      )
    fig.show()
    fig.write_image(file=columnName + '.pdf', format='pdf')
    fig.write_image(file=columnName + '.png', format='png')


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

    min2.name = "min2"
    min3.name = "min3"
    min4.name = "min4"
    standard.name = "standard"

    dfs = [standard, min2, min3, min4]

    # plot('explained_intensity', dfs, 20)
    # plot('explained_peaks', dfs, 20)
    # plot('num_peaks', dfs)

    min2 = min2[min2['num_peaks'] >= 2]
    min3 = min3[min3['num_peaks'] >= 2]
    min4 = min4[min4['num_peaks'] >= 2]
    standard = standard[standard['num_peaks'] >= 2]

    min2.name = "min2"
    min3.name = "min3"
    min4.name = "min4"
    standard.name = "standard"

    dfs = [standard, min2, min3, min4]

    # plot('explained_intensity', dfs, 20)
    # plot('explained_peaks', dfs, 20)
    # plot('num_peaks', dfs)
    # plot('spectral_entropy', dfs)
    # plot('normalized_entropy', dfs)
    polarity = "Positive"
    plt.title(polarity)
    plotSnsHist('explained_intensity', dfs, [0.0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0])
    plt.title(polarity)
    plotSnsHist('explained_peaks', dfs, [0.0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0])
    plt.title(polarity)
    plotSnsHist('num_peaks', dfs)
    plt.title(polarity)
    plotSnsHist('spectral_entropy', dfs, 10)
    plt.title(polarity)
    plotSnsHist('normalized_entropy', dfs, [0.0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0])

    plt.title(polarity)
    sns.scatterplot(data=standard, x="num_peaks", y="explained_peaks",
                    label=standard.name + "(" + str(len(standard)) + ")")
    sns.scatterplot(data=min2, x="num_peaks", y="explained_peaks", label=min2.name + "(" + str(len(min2)) + ")")
    sns.scatterplot(data=min3, x="num_peaks", y="explained_peaks", label=min3.name + "(" + str(len(min3)) + ")")
    sns.scatterplot(data=min4, x="num_peaks", y="explained_peaks", label=min4.name + "(" + str(len(min4)) + ")")
    plt.legend()
    plt.savefig("scatter_peaks_num_vs_explained.png")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
