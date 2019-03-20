from coeplottk import *

#thick(right=0.85)
#figure(figsize=(9.5,6))
#thick(right=0.87, left=0.1)

lam, Fcont, Fline = loaddata('grismsensitivity.txt').T
thick(top=0.9)

plot(lam, Fcont)

xlim(2.4, 5.0)
ylim(0, 26)

xlabel('Wavelength (microns)')
ylabel('Continuum Sensitivity ($\mu$Jy)  S/N=10 in 10 ks')
title('NIRCam grism continuum sensitivity (approx.)')

savepng('grism_cont_sensitivity')

###

# W / m^2
# W   = 1e7 erg / s
# m^2 = 1e4 cm^2

figure(2)

plot(lam, 1e21 * Fline)
xlim(2.4, 5.0)
ylim(0, 11)
retickymult((1))
xlim(2.4, 5.0)

def tentothe(n):
    return '10$\\mathdefault{^{%d}}\!$' % n

xlabel('Wavelength (microns)')
ylabel('Line Sensitivity (' + tentothe(-18) + ' erg/s/cm' + squared + ') S/N=10 in 10 ks', fontsize=17)
title('NIRCam grism line sensitivity (approx.)')

savepng('grism_line_sensitivity')

semilogy()
retickylogmult((1,1.5,2,3,4,5,7))

ytxf = yticks()[0]
ytxm = map(nJytoAB, ytxf)
ytxm = ytxm[1:]
dy = 0.5
ytxm = multiples(min(ytxm), max(ytxm)+dy, dy)
#ytxm = 26.8, 27, 27.2, 27.5, 27.7, 28, 28.2, 28.5, 29, 30
#ytxm = 26.8, 26.9, 27, 27.2, 27.3, 27.5, 27.7, 28, 28.2, 28.5, 29, 30
#ytxm = 27.8, 28, 28.2, 28.5, 28.7, 29, 29.5, 30
ytxf = map(ABtonJy, ytxm)

ax1 = gca()
ax2 = ax1.twinx()
ax1.yaxis.set_label_position('left')
ax2.yaxis.set_label_position('right')
ax1.yaxis.tick_left()
ax2.yaxis.tick_right()

semilogy()

#print ytxf
ylabel('AB magnitude')
yts = map(mapfmt1, ytxm)
#print yts
yticks(ytxf, yts)
ylim(ylo, yhi)
ax2.minorticks_off()
xlim(xlo, xhi)

show()
