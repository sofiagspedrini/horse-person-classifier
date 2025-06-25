## Step-by-step of project development

The experiments notebook was created to test diferent preprocessing methods and distinct model architectures.

First, I checked if the number of samples in both classes of the dataset are similar. This indicates if the dataset is balanced or if it needs an over/under sampling preprocessing. Fortunatly, the dataset was alerady balanced.

Then, I plotted some images to check the samples. It was possible to get some basic insights, as the images size and the fact it was colored.

Considering these aspectes, a preprocessing function was created to convert the image to gray scale and to reduce the image size. This reduce the size of the information that the models will have to handle during training, making the code run smoothly.

The data was then reshaped to be used as input in classic machine learning (ML) models: Logist Regressor and Random Forest. I started testing classic ML models to check their performance compared to Deep Learning (DL) models that were developed later. 

First I created a Logistic Regressor with a some parameters tunning in GridSearch and a small cross validation of 5 folds, which returned 80% accuracy.

Then I used the same parameters with a StratifiedKFold to improve the performance. The StratifiedKFold garantees that the data in all folds are balanced before for the training. This returned the same 80% accuracy, so It didn't impacted much this model. 

The Random Forest was the next one tested. I also used some parameters tunning in GridSearch and a small cross validation of 5 folds t start, and this provided 82% accuracy, a slightly improvement compared to the Logistic Regressor models.

Then, I included the StratifiedKFold in the random forest, which ruterned 97% accuracy in the training set, but 57% accuracy in the testing set. This indicates that the model overfitted, meaning it memorized the aspectes of the training dataset and couldn't generalize what it learnt in the testing dataset.

As a third Random Forest test, I decided to keep the StratifiedKFold but reduced the parameters in the gridsearch based in the best parameters of the first Random Forest. I also reduced the number of splits of the Kfold from 5 to 3. This resulted in an 87% accuracy.

Even though 87% is already a great accuracy, I decided to test some DL models to check if they could perform better.

I reshaped the data to input in Neural Network models. CNN was the chosen architecture due to its good performance with image recognition compared to other NN models.

I included the first Conv2D (convolutional) layer, which learns the patterns, followed by Maxpooling layer, which reduces dimensionality and computation, while keeping important features. Then I included one more Conv2D layer followed by Maxpooling to learn more patterns. The fifth layer is a Flatten, to change the data dimention. Then, a dense layer with relu was included to learn high-level representations.Finally a dense layer with sigmoid outputs a probability between 0 and 1, which is ideal for binary classification.

I included the Adam optimizer, binary_crossentropy in the loss, and the accuracy_metric since they perform well for binary classification problems like this one.

The first DL had 91% accuracy. I decided to test the same model with addition of droputs in the architecture, since it can reduce overtting, and it gave 92% accuracy.

I also tested this second DL with an early_stop function, to improve the overfitting as well, which resultes in 84% accuracy (maybe the early_stop stopped too early!)

I also tested the second DL model using data aumentation with image generator, and it resulted in 85% accuracy.

The last part of the experiment compared the metrics of the best classic ML model with the best DL model. Both of them performed well. If memory and computational costs should be a priority, usin the Random forest would be a good option. If the model performance has to be priority, the DL model was a bit better. In this project, the DL model was chosen to be saved and used in the API.

Next steps could include fine tunning.