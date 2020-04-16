import seaborn as sns
from cycler import cycler

# Default hues for colours
ORANGE = "#F58426"
BLUE = "#2464B0"
PURPLE = "#823BA0"
GREEN = "#559613"
COLOR_SET = [ORANGE, BLUE, GREEN, PURPLE]

DEFAULT = {
    'axes.facecolor': 'white',
    'axes.edgecolor': '0.65',
    'axes.grid': False,
    'axes.axisbelow': True,
    'axes.titlelocation': 'left',
    'axes.titlesize': 18,
    'axes.titleweight': 'bold',
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.prop_cycle': cycler('color', COLOR_SET),
    'lines.solid_capstyle': 'round',
    'patch.edgecolor': 'w',
    'image.cmap': 'rocket',
    'font.family': ['sans-serif'],
    'font.sans-serif': [
        'Raleway',
        'Liberation Sans',
        'sans-serif'],
    'font.weight': 'normal',
    'figure.autolayout': True,
    'figure.dpi': 100,
    'figure.figsize': (10, 10)
}

TWITTER = {
    'figure.dpi': 100,
    'figure.figsize': (10.24, 5.12),
    'axes.titlelocation': 'left',
}

PAPER = {
    'figure.dpi': 100,
    'figure.figsize': (8.5, 11),
    'axes.titlelocation': 'center',
    'axes.titlesize': 14,
    'axes.titleweight': 'bold'
}

PAPER_SQUARE = {
    'figure.dpi': 100,
    'figure.figsize': (10, 10),
    'axes.titlelocation': 'center',
    'axes.titlesize': 14,
    'axes.titleweight': 'bold'
}

PAPER_COMPACT = {
    'figure.dpi': 100,
    'figure.figsize': (4, 4),
    'axes.titlelocation': 'center',
    'axes.titlesize': 12,
    'axes.titleweight': 'bold'
}


def setup(style='default'):
    params = DEFAULT

    if style == 'twitter':
        for key, val in TWITTER.items():
            params[key] = val

    elif style == 'paper':
        for key, val in PAPER.items():
            params[key] = val
    
    elif style == 'paper_square':
        for key, val in PAPER_SQUARE.items():
            params[key] = val

    elif style == 'paper_compact':
        for key, val in PAPER_COMPACT.items():
            params[key] = val

    sns.set(rc=params)

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



