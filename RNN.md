# RNN
#RNN
Recurrent neural networks are a class of neural networks that are able to save some information about previous inputs using a hidden layer. 
On each step, hidden layer is changed by new input and then hidden layer is used for inference an output. More formally, *a* - hidden layer, *x* - input, then $$a = g_1(W_{aa}a + W_{ax}x + b_{a}), y = g_2(W_{ya} a + b_y)$$
where $W_{ax}, W_{aa}, W_{ya}, b_a, b_y$​ are coefficients that are shared temporally and $g_1, g_2$ activation functions.

| **Advantages**                                        | **Drawbacks**                                            |
| ----------------------------------------------------- | -------------------------------------------------------- |
|  Possibility of processing input of any length       | Computation being slow                                   |
| Model size not increasing with size of input          | Difficulty of accessing information from a long time ago |
| Computation takes into account historical information | Cannot consider any future input for the current state   |
| Weights are shared across time                        |                                                          |

## Loss function

Loss function is defined as the sum of loss functions for elements of sequence:
$$\L (\widehat{y}, y) = \sum_i \L (\widehat{y}_{i}, y_i)$$
## Backpropagation through time

Backpropagation is done after loss is counted for each element in sequence.

```python
a = torch.nrand(hsize)
loss = 0
    
x, y, n = get_sequence()

for it in range(n):
    y_pred, a = net(x[it], a)
    loss += F.mse_loss(y_pred, y[it])
    
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

## Commonly used activation functions

The most common activation functions used in RNN modules are:

- **Sigmoid**
- **Tanh**
- **RELU**

## Hidden layer initialization

When inference, hidden layer should be initialized with zeros. But it case of training hidden layer can be initialized using $\mathcal{N}(0, \sigma)$ - it will work as regularization.

## Useful observation

There is a class of tasks when only last element of output sequence is important and others should be 0. It can be useful to train model slightly increasing length of sequence.