import matplotlib.pyplot as plt
from sklearn import datasets,svm,metrics
from sklearn.model_selection import train_test_split

digits=datasets.load_digits()
_,axes=plt.subplots(2,4)
image_and_labels=list(zip(digits.images,digits.target))
for ax,(image,label) in zip(axes[0,:],images_and_label[:4]):
 ax.set_axis_off()
 ax.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
 ax.set_title('training: %i' % label)
 n_samples=len(digits.images)
 data=digits.images.reshape((n_samples,-1))
 classifier= svm.SVC(gamma=0.001)
 X_train,X_test,Y_train,Y_test=train_test_split(data,digits.target,test_size=0.5,shuffle=False)
 classifier.fit(X_train,y_train)
 predicted=classifier.predict(X_test)
 figr,newaxes=plt.subplots(2,6)
 images_and_predications=list(zip(digits.images[n_sample//2:],predicted))
 for ax,(image,prediction) in zip(newaxes[1,:],images_and_predictions[:6]):
      ax.set_axis_off()
      ax.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
      ax.set_title('prdiction: %i'% prediction)

print("classification report for classifier %s:\n%s\n"
         %(classifier,metrics.classification_report(y_test,predicted)))
disp= metrics.plot_confusion_matrix(classifier,X_test,y_test)
disp.figure_.suptitle("confusion Matrix")
print("Confusion matrix:\n%s"% disp.confusion_matrix)

plt.show()

