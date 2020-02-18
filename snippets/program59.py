
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits

X,y=load_digits(return_X_y=True)

from sklearn.ensemble import RandomForestClassifier
random_forest_clf=RandomForestClassifier(n_estimators=5,max_depth=5,random_state=1)


from sklearn.model_selection import cross_val_predict
predictions=cross_val_predict(random_forest_clf,X,y)

import scikitplot as skplt
skplt.metrics.plot_confusion_matrix(y,predictions,normalize=True)

plt.show()
