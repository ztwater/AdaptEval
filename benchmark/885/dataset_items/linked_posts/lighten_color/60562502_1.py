import matplotlib
import seaborn as sns

color = matplotlib.colors.ColorConverter.to_rgb("navy")
rgbs = [scale_lightness(color, scale) for scale in [0, .5, 1, 1.5, 2]]
sns.palplot(rgbs)
