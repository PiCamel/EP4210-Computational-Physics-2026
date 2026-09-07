const dx = 10^(-5) #Value of width of rectangle

#taking tiny rectangular strips to calculate area
function integral_rect(f::Function, a, b)
    sum = 0
    x = a
    while x < b
        sum += f(x)*dx
        x += dx
    end
    return sum
end

#taking trapezoidal areas to calculate area
function integral_trpz(f::Function, a, b)
    sum = 0
    x = a
    while x<=(b-dx)
        sum += (f(x) + f(x+dx))*dx/2
        x += dx
    end
    return sum
end
#limits for integration
n0 = 0
n1 = π
#area of sin from 0 to π/2 = 1
a0 = integral_rect(sin::Function, n0, n1)
println("Area from Rectangles: ", a0)
a1 = integral_trpz(sin::Function, n0, n1)
println("Area from Trapezoids: ", a1)