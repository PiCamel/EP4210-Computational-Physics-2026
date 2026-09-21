using Random
using Plots

const N = 1000000 # number of points to generate
# Random number generation using Xoshiro256+ algorithm - NOT USED
# ! Learn how random works, the different algorithms
# rng = Xoshiro(100)
# println(rand(rng, 1:10, 6));

# Finding area of circle x^2 + y^2 <= 1 -> Monte Carlo integration
x_arr = rand(Float32, N)
x_arr = 2*x_arr.-1
y_arr = rand(Float32, N)
y_arr = 2*y_arr.-1

# Copilot Generate Part Begins

# Plot a small sample of the points for visualisation
sample_size = 20000
sample_idx = 1:ceil(Int, N/sample_size):N
point_colors = [(x^2 + y^2 <= 1) ? :green : :red for (x, y) in zip(x_arr[sample_idx], y_arr[sample_idx])]

scatter(x_arr[sample_idx], y_arr[sample_idx],
    color=point_colors,
    markerstrokewidth=0,
    markersize=1.5,
    alpha=0.8,
    xlabel="x",
    ylabel="y",
    title="Random points in [-1, 1]^2",
    aspect_ratio=:equal,
    legend=false,
    xlims=(-1, 1),
    ylims=(-1, 1)
)

plot!(x -> sqrt(1 - x^2), -1, 1, color=:black, lw=2, label="x^2 + y^2 = 1")
plot!(x -> -sqrt(1 - x^2), -1, 1, color=:black, lw=2, label="")
gui()
# Copilot Generated Part Ends

function counter(x_arr, y_arr, n)
    count = 0
    for i in 1:n
        if (x_arr[i])^2 + (y_arr[i])^2 <= 1
            count = count +1
        end
    end
    return count
end

area = 4.0*counter(x_arr, y_arr, N)/N
println(area)