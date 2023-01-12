# RNN
From [[deep learning]]

Recurrent neural networks are a class of neural networks that are able to save some information about previous inputs using a hidden layer. There are different variations, e.g. [[LSTM]], but here we describe the simplest case.

On each step, hidden layer is changed by new input and then hidden layer is used for inference an output. More formally, $a$ - previous hidden layer, $x$ - input, then $$a = g_1(W_{aa}a + W_{ax}x + b_{a}), y = g_2(W_{ya} a + b_y)$$
where $W_{ax}, W_{aa}, W_{ya}, b_a, b_y$ are coefficients that are shared temporally and $g_1, g_2$ are some activation functions.

Advantages:
- Possibility of processing input of any length taking into account historical information
- Model size doesn't increase for larger inputs, because weights are shared
Drawbacks:
- Slow computation, because we need to process input sequentially
- Difficult access to information from a long time ago due to unstable gradients

## Loss function

Loss function is defined as the sum of loss functions for elements of sequence:
$$\L (\widehat{y}, y) = \sum_i \L (\widehat{y}_{i}, y_i)$$
## Backpropagation through time

Backpropagation is done after loss is counted for each element in sequence.

```python
a = torch.randn(hsize)
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

## Example
```python
class Model(nn.Module):
    def __init__(self, hidden_size, x_size, y_size):
        super().__init__()
        self.hidden_size = hidden_size
        self.x_size = x_size
        self.y_size = y_size
        
        self.Waa = nn.Linear(hidden_size, hidden_size)
        self.Wax = nn.Linear(x_size, hidden_size)
        self.g1 = nn.Tanh()
        self.g2 = nn.Softmax()
        
        self.Wya = nn.Linear(hidden_size, y_size)
    
    def forward(self, x, a):
        new_a = self.g1(self.Waa(a) + self.Wax(x))
        return self.g2(self.Wya(new_a)), new_a
```

## Hidden layer initialization

When doing inference, hidden layer should be initialized with zeros. But in case of training, hidden layer can be initialized using $\mathcal{N}(0, \sigma)$ - it will work as regularization.

## Useful observation

There is a class of tasks when only last element of output sequence is important and others should be 0. It can be useful to train model slightly increasing length of sequence.