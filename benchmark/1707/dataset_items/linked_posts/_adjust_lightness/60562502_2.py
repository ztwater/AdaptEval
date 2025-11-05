from colorsys import rgb_to_hls
import seaborn as sns

color = (1.0, 0.0, 0.0)     # RGB

print(f"Input color:    \t Lightness:  {rgb_to_hls(*color)[1]: .2g}\t RGB:  {color}")

rgbs = []
for scale in [0, .5, 1, 1.5, 2]:

    # scale the lightness (The values should be between 0 and 1)
    lightness = min(1, rgb_to_hls(*color)[1] * scale)

    # manipulate h, l, s channel of a rgb color
    rgb = sns.set_hls_values(color = color, h = None, l = lightness, s = None)

    print(f"Scale factor: {scale: .2g}\t Lightness:  {lightness: .2g}  \t RGB:  {rgb}")
    rgbs.append(rgb)

sns.palplot(rgbs)
