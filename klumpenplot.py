import seaborn as sns
from cycler import cycler

# Default hues for colours
ORANGE = "#F58426"
BLUE = "#2464B0"
PURPLE = "#823BA0"
GREEN = "#559613"
COLOR_SET = [ORANGE, BLUE, GREEN, PURPLE]

DEFAULT_PARAMS = {
    'axes.facecolor': 'white',
    'axes.edgecolor': '0.65',
    'axes.grid': False,
    'axes.axisbelow': True,
    # 'axes.labelcolor': '.15',
    # 'figure.facecolor': 'white',
    # 'text.color': '.15',
    # 'xtick.color': '.15',
    # 'ytick.color': '.15',
    # 'xtick.direction': 'out',
    # 'ytick.direction': 'out',
    'lines.solid_capstyle': 'round',
    'patch.edgecolor': 'w',
    'image.cmap': 'rocket',
    'font.family': ['sans-serif'],
    'font.sans-serif': [
        'Raleway',
        'Liberation Sans',
        'sans-serif'],
    'font.weight': 'normal',
    # 'patch.force_edgecolor': True,
    # 'xtick.bottom': False,
    # 'xtick.top': False,
    # 'ytick.left': False,
    # 'ytick.right': False,
    'axes.titlelocation': 'left',
    'axes.titlesize': 18,
    'axes.titleweight': 'bold',
    # 'axes.spines.left': True,
    # 'axes.spines.bottom': True,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.prop_cycle': cycler('color', COLOR_SET),
    'figure.dpi': 100,
    'figure.figsize': (10.24, 5.12),
    'figure.autolayout': True
}

def setup():
    sns.set(rc=DEFAULT_PARAMS)

def tweet(ax, title=None, subtitle=None, xlabel=None, ylabel=None, notes=None, credit=None):
    # Make it look good for tweets.
    if subtitle:
        ax.set_title(title, pad=22)
        ax.text(
            ax.get_xlim()[0] + ax.margins()[0], 
            ax.get_ylim()[1]*1.03, 
            subtitle, 
            fontstyle='italic')
    else:
        ax.set_title(title, pad=10)
    if credit:
        ax.text(
            ax.get_xlim()[1] + ax.margins()[0], 
            ax.get_ylim()[0]-0.20*(ax.get_ylim()[1] - ax.get_ylim()[0]), 
            credit, 
            fontsize=10, 
            horizontalalignment='right')
    if notes:
        ax.text(
            ax.get_xlim()[0] + ax.margins()[0], 
            ax.get_ylim()[0]-0.20*(ax.get_ylim()[1] - ax.get_ylim()[0]), 
            notes, 
            fontsize=10, 
            horizontalalignment='left')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return ax



