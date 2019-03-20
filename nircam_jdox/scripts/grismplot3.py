from coeplott import *

thick(top=0.87)
figure(figsize=(8,6.5))

plot([2.42, 3.12], [4,4], 'k')
plot([2.42, 4.03], [3,3], 'k')
plot([4.828, 5.5], [3,3], 'k', alpha=0.3)
plot([3.12, 4.01], [2,2], 'k')
plot([3.90, 4.31], [1,1], 'k')
plot([3.89, 5.00], [0,0], 'k')

text(1.5, 4, 'F277W', va='center')
text(1.5, 3, 'F322W2', va='center')
text(1.5, 2, 'F356W', va='center')
text(1.5, 1, 'F410M', va='center')
text(1.5, 0, 'F444W', va='center')

ms = 10
plot(4, 4, 'kx', ms=ms)
plot(4, 3, 'kx', ms=ms)
plot(4, 2, 'kx', ms=ms)
plot(4, 1, 'kx', ms=ms)
plot(4, 0, 'kx', ms=ms)

xlim(1, 5.5)
ylim(-0.8, 5.5)

ax = gca()
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top') 
xlabel('First-Order Wavelength (microns)')
ax.xaxis.set_ticks_position('both')

savepdf('grismorders')
show()

