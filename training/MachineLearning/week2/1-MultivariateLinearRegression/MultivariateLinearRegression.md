# Multiple Features

Note: [7:25 - θT is a 1 by (n+1) matrix and not an (n+1) by 1 matrix]

Linear regression with multiple variables is also known as "multivariate linear regression".

We now introduce notation for equations where we can have any number of input variables.

x(i)jx(i)mn=value of feature j in the ith training example=the column vector of all the feature inputs of the ith training example=the number of training examples=∣∣x(i)∣∣;(the number of features)
The multivariable form of the hypothesis function accommodating these multiple features is as follows:

hθ(x)=θ0+θ1x1+θ2x2+θ3x3+⋯+θnxn
In order to develop intuition about this function, we can think about θ0 as the basic price of a house, θ1 as the price per square meter, θ2 as the price per floor, etc. x1 will be the number of square meters in the house, x2 the number of floors, etc.

Using the definition of matrix multiplication, our multivariable hypothesis function can be concisely represented as:

hθ(x)=[θ0θ1...θn]⎡⎣⎢⎢⎢⎢x0x1⋮xn⎤⎦⎥⎥⎥⎥=θTx
This is a vectorization of our hypothesis function for one training example; see the lessons on vectorization to learn more.

Remark: Note that for convenience reasons in this course we assume x(i)0=1 for (i∈1,…,m). This allows us to do matrix operations with theta and x. Hence making the two vectors 'θ' and x(i) match each other element-wise (that is, have the same number of elements: n+1).]

The following example shows us the reason behind setting x(i)0=1 :

X=[x(1)0x(1)1x(2)0x(2)1x(3)0x(3)1],θ=[θ0θ1]
As a result, you can calculate the hypothesis as a vector with:

hθ(X)=θTX