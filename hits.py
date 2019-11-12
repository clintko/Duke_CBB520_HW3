import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from mt_genome_regions import regions, is_in_range, get_region
from matplotlib.lines import Line2D
import matplotlib.patches as patches


# def main():
with open('loc_type.txt') as f_in:
    lines = [line.strip().split(',') for line in f_in]

locs = [int(loc) for (seq_name, loc, loc_type, loc_name, comp)
        in lines if seq_name[0:3] == 'SRR']

locs.sort()
counts = Counter(locs)

mt_locs = list(range(16727))
mt_frq = [counts[i] for i in mt_locs]

color_type = {'gene_CDS': 'green', 'tRNA': 'red',
              'D-loop': 'blue', 'rRNA': 'purple', 'rep_origin': 'brown'}

fig, ax = plt.subplots()
for r in regions:
    plt.plot(
        mt_locs[r['range'][0]:r['range'][1]],
        mt_frq[r['range'][0]:r['range'][1]],
        c=color_type[r['type']],
        label=r['name'],
    )
    rect = patches.Rectangle(
        xy=(r['range'][0], 0),
        width=r['range'][1]-r['range'][0],
        height=900,
        linewidth=1,
        edgecolor='orange' if r['comp'] and r['type'] is 'tRNA' else 'none',
        facecolor='orange' if r['comp'] and r['type'] is 'tRNA' else 'none',
        alpha=0.3
    )
    ax.add_patch(rect)

legend_objs = []
legend_txt = []
for t, c in color_type.items():
    legend_txt.append(t)
    legend_objs.append(
        Line2D([0], [0], color=c, lw=4)
    )

legend_txt.append('Complementary strand tRNA')
legend_objs.append(
    Line2D([0], [0], color='orange', alpha=0.3, lw=4)
)
ax.legend(legend_objs, legend_txt)
plt.title('Hits from Ancient RNA files')
plt.show()


# if __name__ == "__main__":
#    main()

# Create a Rectangle patch
rect = patches.Rectangle((50, 100), 40, 30, linewidth=1,
                         edgecolor='r', facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)
