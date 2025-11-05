# check results
TP = df_test[(df_test.x>=cut_off.x)&(df_test.y==1)].index.size
FP = df_test[(df_test.x>=cut_off.x)&(df_test.y==0)].index.size
TN = df_test[(df_test.x< cut_off.x)&(df_test.y==0)].index.size
FN = df_test[(df_test.x< cut_off.x)&(df_test.y==1)].index.size

print("True Positive Rate: ", TP / (TP + FN))
print("False Positive Rate:", 1 - TN / (TN + FP))
