Gradient Descent For Multiple Variables

Gradient Descent for Multiple Variables

The gradient descent equation itself is generally the same form; we just have to repeat it for our 'n' features:

}repeat until convergence:{θ0:=θ0−α1m∑i=1m(hθ(x(i))−y(i))⋅x(i)0θ1:=θ1−α1m∑i=1m(hθ(x(i))−y(i))⋅x(i)1θ2:=θ2−α1m∑i=1m(hθ(x(i))−y(i))⋅x(i)2⋯
In other words:

}repeat until convergence:{θj:=θj−α1m∑i=1m(hθ(x(i))−y(i))⋅x(i)jfor j := 0...n
The following image compares gradient descent with one variable to gradient descent with multiple variables:
![](GradientDescentForMultipleVariables.png)
