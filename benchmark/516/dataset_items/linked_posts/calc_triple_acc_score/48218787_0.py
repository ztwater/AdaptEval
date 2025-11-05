optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]
