using Plots
 
x = collect(1:0.1:30)
y = sin.(x)
df = 2
 
anim = @animate for i = 1:df:length(x)
    plot(x[1:i], y[1:i], legend=false)
end
 
gif(anim, "anima.gif", fps = 30)