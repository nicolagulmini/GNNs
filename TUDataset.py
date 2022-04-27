import kernel_baselines as kb
import auxiliarymethods.datasets as dp

use_labels, use_edge_labels = True, False
dataset = "ENZYMES"

# Download dataset.
classes = dp.get_dataset(dataset)

iterations = 3
gram_matrix = kb.compute_wl_1_dense(dataset, iterations, use_labels, use_edge_labels)