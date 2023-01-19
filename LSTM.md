# LSTM
From [[deep learning]]

The problem of simple [[RNN]] is that it performs poorly on learning long-term dependencies. Here is a particular architecture that can help with it. 

## Step-by-step derivation
### [[RNN]]
$$ h_{t} = \tanh(W_{u}x_{t}+U_{u}h_{t-1} +b_{u})$$
Here the state is completely recalculated each time based on the previous state and the new inputs. Because of this, when we apply activation function multiple times the information from the past quickly vanishes or explodes.

### Adding constant error carousel

$$ u_{t} = \tanh(W_{u}x_{t}+U_{u}h_{t-1} +b_{u})$$
$$ c_{t} = c_{t-1} + u_{t} $$
$$ h_{t}= c_{t} $$
So if we denote our previous activation function $f(x)$ then now we use $x + f(x)$ instead, like in invertible neural networks. As one can see, the gradient of our new activation function is $1 + f'(x)$ . It means that for majority of traditional functions (tanh, sigmoid) we solved the problem of vanishing gradient (Our gradient is more than 1), but it still can explode.


### Cutting off gradients

To prevent it, we will truncate our backpropagation. Now we don’t propagate gradients from $u_{t}$ to $h_{t-1}$.We just decompose $c_t$ into a sum of $u_{1..t}$ and differentiate all of them w.r.t. $x_{1..t}$.


### Adding gates
$$ u_{t} = \tanh(W_{u}x_{t}+U_{u}h_{t-1} +b_{u})$$
$$i_{t} = \sigma(W_{i}x_{t} + U_{i}h_{t-1} + b_{i})$$
$$o_{t} = \sigma(W_{o}x_{t} + U_{o}h_{t-1} + b_{o})$$
$$ c_{t} = c_{t-1}+i_{t}\odot u_{t}$$
$$ h_{t}= o_{t}\odot c_{t} $$
here: 
$i_t$ — input gate activation
$o_t$ — output gate activation
$h_t$ — hidden state, which is also output
$u_t$ — cell update
$c_t$ — cell state vector
$\odot$ — Hadamard product (elementwise multiplication)

Now we add multiplicative gates between update and cell state vectors (input) and between cell state and hidden state (output). This allows the network to be more selective about which parts of cell memory can be overwritten and from which parts should we calculate the answer.

### Merging into blocks
We have three layers. Input, hidden and output. Hidden layer consists of memory blocks. Each block has one input and output gate and some number of memory cells, as described above. This slightly reduces the number of parameters and computation cost, and with small enough blocks, it doesn’t affect the quality of results too much because often information comes naturally in a larger-than-bit sizes.