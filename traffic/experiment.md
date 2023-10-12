# Experimentation Process Record- Reasoning for neural network setup

1. Initial Model:

I started with an initial model that had a high loss of 3.3275 and a low accuracy of 0.0966. This suggested that the model was not performing well.

2. Removed Dropout:

In an attempt to address the initial poor performance, I removed the dropout. This led to a significant improvement, reducing the loss to 0.6388 and increasing accuracy to 0.9264. However, it raised concerns about potential overfitting.

3. Adding Back Dropout (5%):

To mitigate the risk of overfitting, I added dropout with a rate of 5%. This adjustment further improved the model, reducing the loss to 0.3739 and increasing accuracy to 0.9435.

4. Doubling the Number of Nodes to 256:

I experimented with increasing the number of nodes in the model to 256. While this improved accuracy to 0.9632 for my final piece of training data, there were still indications of overfitting, as the test result gave 0.9322.

5. Trying 50% Dropout:

In an attempt to reduce overfitting, I increased the dropout rate to 50%. However, this led to a decline in accuracy to 0.7386, indicating excessive dropout.

6. Trying 10% Dropout:

I then reduced the dropout rate to 10%, resulting in an accuracy of 0.9164. This change improved accuracy while maintaining a reasonable dropout rate, but still not as good as experiment number 3.

7. Adding an Extra Layer:

I added an additional layer to the model, which further improved performance, reducing the loss to 0.4033 and increasing accuracy to 0.9393.

8. Reducing Dropout to 5%:

After observing potential overfitting, I decreased the dropout rate to 5%. This change increased accuracy to 0.9013.

9. Adding More Filters (64 Filters):

I experimented with adding more filters to the convolutional layers, using 64 filters. This change had a minimal impact on accuracy, resulting in 0.9140.

10. Making Max Pool Size 3x3:

I adjusted the max pool size to 3x3, which reduced accuracy to 0.9121. I concluded that this was not granular enough, and moved back to a max pool size of 2x2.

## Conclusion
I chose to go with the setting of experiment number 3, with 32 filters of a 3x3 kernal with one convolutional layer (relu activation), a max pool layer of size 2x2 and then finally one layer with 128 neurons with a relu activation. The output layer for traffic signs had a softmax activation.