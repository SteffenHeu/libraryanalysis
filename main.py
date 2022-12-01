import plotly.graph_objects as go
import pandas as pn
import numpy as np
import kaleido
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from plotly.graph_objs.histogram import XBins


# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def plotSnsHist(columnName, dfs: list, numBins=None):
    numBins = 'auto' if numBins is None else numBins
    for df in dfs:
        sns.histplot(data=df, x=columnName, bins=numBins,
                     label=df.name + ' (' + str(len(df)) + ')', element="step", alpha=0.3)
    plt.legend()
    plt.savefig(columnName + '.png')
    plt.show()
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
    mzmineMsdialCompare()
    # compare500ms()
    # compareMzmine()

def compareMzmine():
    mzm100msNogap: DataFrame = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/MZmine Paper/20221128 - Nist sample/nist1950_100ms_hilic_wizard_nogap.csv',
        sep=';')
    areaNogap = mzm100msNogap.filter(like=":area")
    areaNogap["sdev"] = areaNogap.std(axis=1)
    areaNogap["avg"] = areaNogap.mean(axis=1)
    areaNogap["RSD of feature area"] = areaNogap["sdev"] / areaNogap["avg"]
    areaNogap.name = "MZmine no gap"

    mzm100ms: DataFrame = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/MZmine Paper/20221128 - Nist sample/nist1950_100ms_hilic_wizard.csv',
        sep=';')
    area100 = mzm100ms.filter(like=":area")
    area100["sdev"] = area100.std(axis=1)
    area100["avg"] = area100.mean(axis=1)
    mzm100ms["RSD of feature area"] = area100["sdev"] / area100["avg"]
    mzm100ms.name = "MZmine - HILIC Wizard"

    plotSnsHist("RSD of feature area", [mzm100ms, areaNogap], [0.0, 0.1, 0.2, .3, .4, .5, .6, .7, .8, .9, 1.0])


def compare500ms():
    mzm500ms: DataFrame = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/MZmine Paper/20221128 - Nist sample/nist1950_500ms_hilic_wizard.csv',
        sep=';')
    area500 = mzm500ms.filter(like=":area")
    area500["sdev"] = area500.std(axis=1)
    area500["avg"] = area500.mean(axis=1)
    area500["RSD 500 ms"] = area500["sdev"] / area500["avg"]
    area500.name = "MZmine 500 ms"
    msd500ms: DataFrame = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/MZmine Paper/20221128 - Nist sample/msdial 500 ms default.csv',
        sep=';')
    msd500ms = msd500ms[msd500ms["Average mobility"] != -1]
    msd500ms["RSD 500 ms"] = msd500ms["Stdev"] / msd500ms["Average"]
    msd500ms.name = "MSDIAL 500 ms"
    plotSnsHist("RSD 500 ms", [area500, msd500ms], [0.0, 0.1, 0.2, .3, .4, .5, .6, .7, .8, .9, 1.0])


def mzmineMsdialCompare():
    mzm100ms: DataFrame = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/MZmine Paper/20221128 - Nist sample/nist1950_100ms_hilic_wizard.csv',
        sep=';')
    area100 = mzm100ms.filter(like=":area")
    area100["sdev"] = area100.std(axis=1)
    area100["Average"] = area100.mean(axis=1)
    area100.name = "MZmine"
    mzm100ms["RSD of feature area"] = area100["sdev"] / area100["Average"]
    count = (mzm100ms["RSD of feature area"] < 0.3).sum()
    mzm100ms.name = "MZmine - HILIC Wizard [" + str(count) + "]"

    msd100msopt: DataFrame = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/MZmine Paper/20221128 - Nist sample/MSDIAL 100 ms area.csv',
        sep=';')
    msd100msopt = msd100msopt[msd100msopt["Average mobility"] != -1]
    msd100msopt["RSD of feature area"] = msd100msopt["Stdev"] / msd100msopt["Average"]
    count = (msd100msopt["RSD of feature area"] < 0.3).sum()
    msd100msopt.name = "MSDIAL - transferred parameters [" + str(count) + "]"

    msd100msdefault: DataFrame = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/MZmine Paper/20221128 - Nist sample/msdial_area_100ms_default.csv',
        sep=';')
    msd100msdefault = msd100msdefault[msd100msdefault["Average mobility"] != -1]
    msd100msdefault["RSD of feature area"] = msd100msdefault["Stdev"] / msd100msdefault["Average"]
    count = (msd100msdefault["RSD of feature area"] < 0.3).sum()
    msd100msdefault.name = "MSDIAL - default, 2 det [" + str(count) + "]"

    msd100msdefault500: DataFrame = pn.read_csv(
        'D:/sciebo/Promotion/Auswertungen/MZmine Paper/20221128 - Nist sample/msdial_area_100ms_default_500height.csv',
        sep=';')
    msd100msdefault500 = msd100msdefault500[msd100msdefault500["Average mobility"] != -1]
    msd100msdefault500["RSD of feature area"] = msd100msdefault500["Stdev"] / msd100msdefault500["Average"]
    count = (msd100msdefault500["RSD of feature area"] < 0.3).sum()
    msd100msdefault500.name = "MSDIAL - default, 500 height, 2 det [" + str(count) + "]"

    # plotSnsHist("RSD of feature area", [mzm100ms, msd100msdefault500, msd100msdefault, msd100msopt],
    #             [0.0, 0.1, 0.2, .3, .4, .5, .6, .7, .8, .9, 1.0])

    # area100["Average"] = area100["Average"] / area100["Average"].max()
    # msd100msdefault500["Average"] = msd100msdefault500["Average"] / msd100msdefault500["Average"].max()
    areadfs = [area100, msd100msdefault500]
    sns.histplot(area100, x="Average", element="step", log_scale=(True, False), label=area100.name)
    sns.histplot(msd100msdefault500, x="Average", element="step", log_scale=(True, False), label=msd100msdefault500.name)
    plt.legend()
    plt.show()

    mzm100ms["software"] = "MZmine 3"
    msd100msdefault500["software"] = "MSDIAL 4.92"
    mzm100ms["Average"] = area100["Average"]
    mergedDf = pn.concat([mzm100ms, msd100msdefault500])
    g = sns.jointplot(mergedDf, x="RSD of feature area", y="Average", hue="software", kind='hist')
    g.ax_joint.set_yscale("log")
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
