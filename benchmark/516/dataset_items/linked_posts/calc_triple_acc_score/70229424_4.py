# split dataset into train-test
X_train, X_test, y_train, y_test = train_test_split(
    df[["x"]], df.y.values, test_size=0.5, random_state=1)
# init and fit Logistic Regression on train set
clf = linear_model.LogisticRegression()
clf.fit(X_train, y_train)
# predict probabilities on x test set
y_proba = clf.predict_proba(X_test)
# compute FPR and TPR from y test set and predicted probabilities
fpr, tpr, thresholds = roc_curve(
    y_test, y_proba[:,1], drop_intermediate=False)
# compute ROC AUC
roc_auc = auc(fpr, tpr)
# init a dataframe for results
df_test = pd.DataFrame({
    "x": X_test.x.values.flatten(),
    "y": y_test,
    "proba": y_proba[:,1]
})
# sort it by predicted probabilities
# because thresholds[1:] = y_proba[::-1]
df_test.sort_values(by="proba", inplace=True)
# add reversed TPR and FPR
df_test["tpr"] = tpr[1:][::-1]
df_test["fpr"] = fpr[1:][::-1]
# optional: add thresholds to check
#df_test["thresholds"] = thresholds[1:][::-1]
# add Youden's j index
df_test["youden_j"] = df_test.tpr - df_test.fpr
# define the cut_off and diplay it
cut_off = df_test.sort_values(
    by="youden_j", ascending=False, ignore_index=True).iloc[0]
print("CUT-OFF:")
print(cut_off)

# plot everything
with plt.style.context("bmh"):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    
    RocCurveDisplay(
        fpr=df_test.fpr, tpr=df_test.tpr,
        roc_auc=roc_auc).plot(ax=ax[0])
    ax[0].set_title("ROC curve")
    ax[0].axline(xy1=(0,0), slope=1, color="r", ls=":")
    ax[0].plot(cut_off.fpr, cut_off.tpr, 'ko', ms=10)
    
    df_test.plot(
        x="youden_j", y="proba", ax=ax[1], 
        ylabel="Predicted Probabilities", xlabel="Youden j",
        title="Youden's index", legend=False
    )
    ax[1].axvline(cut_off.youden_j, color="k", ls="--")
    ax[1].axhline(cut_off.proba, color="k", ls="--")
    
    df_test.plot(
        x="x", y="proba", ax=ax[2], 
        ylabel="Predicted Probabilities", xlabel="X Feature",
        title="Cut-Off", legend=False
    )
    ax[2].axvline(cut_off.x, color="k", ls="--")
    ax[2].axhline(cut_off.proba, color="k", ls="--")

    plt.show()
