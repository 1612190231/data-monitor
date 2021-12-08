# coding : utf-8
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    plt.scatter([118.80148, 117.14018, 117.14018, 117.14018, 117.14018], [35.158635, 38.604235, 38.604235, 38.604235, 38.604235],
                marker='o', color='blue', label='loc_2', s=1, alpha=0.3)

    # plt.scatter([66], [49], marker='^', color='darkred', label='LCSD_2', s=8)

    # plt.title('Scatter')
    plt.title("scatter points", fontsize=18)
    plt.xlabel("fac_cpx_loc_2", fontsize=9)
    plt.ylabel("abe_cpx_loc_2", fontsize=9)
    # plt.axis([73.33, 135.05, 3.51, 53.33])
    plt.legend(loc='upper right')
    plt.show()
    # plt.xticks(fac_cpx_loc_2)
    # plt.yticks(abe_cpx_loc_2)
    # plt.savefig('./0.15blue_dims_fac_abe.jpg', dpi=1000)
