from coeplott import *

#thick(right=0.85)
thick(top=0.92)
figure(figsize=(9.5,6))
#thick(right=0.87, left=0.1)

txt = loadfile('saturation64.txt')

allowedfilters = 'F070W F140M F150W F182M F187N F200W F210M F212N'.split()  # Time Series Imaging
# Grism Time Series: F182M F187N F210M F212N

ss = []
cc = []
for line in txt:
    if line[0] == '#':
        continue
    filter, saturation, center, lambda1, lambda2 = line.split('\t')

    if filter not in allowedfilters:
        continue

    if 'W' in filter:
        sym = 'D'
        lw = 1
        color = 'w'
        ms = 12
        fontweight = 'normal'
        fontsize = 10
        color = 'k'
        style = 'normal'
    elif 'M' in filter:
        sym = 'o'
        lw = 3
        color = 'k'
        ms = 8
        fontweight = 'bold'
        fontsize = 8
        color = 'k'
        style = 'normal'
        #continue
    elif 'N' in filter:
        sym = '+'
        lw = 5
        color = 'k'
        ms = 8
        fontweight = 'normal'
        fontsize = 10
        color= 'k'
        style = 'italic'
        #continue

    dy = 0.9
    dy = 1.5
    saturation = float(saturation)
    saturation -= 4.06  # WLP8 160x160
    y = saturation
    #y -= 5  # WLP8 160x160
    #yfac = 1.1
    #if filter in 'F212N F466N'.split():
    #    yfac = 0.84
    dy = 0.23
    if filter in 'F115W F322W2 F470N F480M F200W F187N'.split():
        dy = -0.42
    text(center, y-dy, filter, ha='center', fontsize=fontsize, fontweight=fontweight, color=color, style=style)
    #s = roundint(float(saturation))
    #text(center, float(saturation)-1, '%d'%s, ha='center', va='top', fontsize=10)

    plot([lambda1, lambda2], [saturation, saturation], 'k', lw=lw, zorder=-10)
    #plot([center], [saturation], color+sym, ms=ms)
    ss.append(float(saturation))
    cc.append(float(center))

#cc = array(cc)
#ss = array(ss)
colormap(cc, ss, cc, showcolorbar=0, s=250, alpha=0.5)
spectral()
#clim(0, 5.5)
#clim(0, 5.2)
clim(0.3, 5.3)
#ticks = multiples(0.5, 5, 0.5)
#colorbar(ticks=ticks)
#colorbar(orientation='horizontal', ticks=ticks)

#semilogy()
#tight()
#xlim(0.6, 5.0)
yhi = 30
yhi = 72
ylo, yhi = 7, 400
ylo, yhi = 18, 9
ylo, yhi = 12, 3
ylo, yhi = 11.7, 2.7
ylo, yhi = 6.7, -2.3
ylim(ylo, yhi)
yticks(multiples(yhi, ylo))

xlo, xhi = 0.5, 5.1
xlim(xlo, xhi)

#xticks(multiples(xlo, xhi, 0.5))

xlabel('Wavelength (microns)')
#ylabel('saturation  (10-sigma in 10 ks)')
#ylabel('saturation  (10$\sigma$ in 10 ks)')
#ylabel('Saturation (Vega K for G2V star; 80% well)')
ylabel('Saturation K mag (Vega) for G2V star')
#title('Saturation (80% well) w/ WLP8 and 160x160 subarray (2 reads)')
title('Saturation (80% well) WLP8 + 160x160 subarray (2 reads)')
#ylabel('Saturation (Vega K for G2V star; 80% full well in 21.4 sec)')
#outroot = 'NIRCam saturation WLP8 160x160 all'
outroot = 'NIRCam saturation WLP8 160x160'
savepng(outroot)

show()
