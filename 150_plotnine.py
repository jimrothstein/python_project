# This is PYTHON !


from plotnine import *
from plotnine.data import mtcars, mpg


(
    ggplot(mpg, aes("cty", "hwy"))
    # to create a scatterplot
    + geom_point()
    # to fit and overlay a loess trendline
    + geom_smooth(method="lm", color="blue")
)
