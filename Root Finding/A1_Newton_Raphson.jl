# Constant values for the problem
const a = 1;
const V_0 = 1;
const m = 0.5;
const ħ = 1;
z0 = sqrt(2*m*V_0/ħ^2);
# FOR THE EIGENVALUE of the Bound State Energy, z^2 = z0^2 - 2*m*f/ħ^2, f = (z0^2 - z^2)*ħ^2/(2m)
# IMPORTANT CONDITION: (z0/z)^2 >= 1, z0/z >= 1, |z0| >= |z|

f(x) = tan(a*x) - 2*sqrt(((z0/x)^2)-1)/(2 - ((z0/x)^2))
# General Numerical Derivative of function f at point x
function f_derivative(f::Function, x)
    h = 10^(-8); # precision for derivative
    return (f(x+h) - f(x-h))/(2*h);

end;

# Newton Raphson Method: x_n = x_(n-1) - f(x)/f'(x)
trial_val = 0.95; # -z0 <= z <= z0, trial value for the root finding
function newtonRaphson(f::Function, dfdx::Function, n)
    ϵ = abs(f(n));
    x = n;
    while (ϵ > 10^(-15)) && (x<=z0)
        if (dfdx(x) == 0)
            println("Derivative is zero, cannot continue.");
            break;
        end;
        x = x-f(x)/dfdx(x);
        ϵ = abs(f(x));
    end;
    return x;
end;

root = newtonRaphson(f, f_derivative, trial_val);
println("Value of root (z): ", root);
# using the root to find the energy of the bound state
E = (root^2 - z0^2)*ħ^2/(2*m);
println("The eigenvalue of the bound state energy is: ", round(E, digits=7));