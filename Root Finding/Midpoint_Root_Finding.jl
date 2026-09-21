ϵ = 0.0001
f(x) = tan(x) - exp(x)
a = 0; b = 9π/20
x_0 = (a+b)/2; #
err = abs(f(x_0))

while err > ϵ
    print("\n")
    global x_0
    global err
    global a
    global b
    x_0 = (a+b)/2;
    err = abs(f(x_0))
    if err < ϵ
        break
    elseif f(x_0)*f(b) < 0
        a = x_0
    elseif f(a)*f(x_0) < 0
        b = x_0
    end
end

print(x_0)