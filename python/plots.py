import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_boxplot_by_year(data, outcome, outcome_label, title, width=12, height=8):
    year_box = sns.boxplot(x='year_group', y=np.log(data[outcome]),
                          hue='dispatch_quarter', data=data, palette='bright')

    year_box.set(title=title)
    year_box.legend(title=None)

    plt.xticks(fontsize=15)
    plt.xlabel('Year', fontsize=18)
    plt.yticks(fontsize=15)
    plt.ylabel('Log({})'.format(outcome_label), fontsize=18)
    plt.legend(bbox_to_anchor=(1.05, 0.6), loc=2, borderaxespad=0., title=None)
    fig = plt.gcf()
    fig.set_size_inches(width, height)

    return fig