import pandas as pd

repository = \
    "https://github.com/lmassaron/ml4dummies_3ed/"
release = "releases/download/v1.0/"
filename = repository + release + "tennis.csv"
tennis = pd.read_csv(filename)
print(tennis)

X = tennis[["outlook", "temperature",
            "humidity", "wind"]]
X = pd.get_dummies(X)
y = tennis.play


from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=0)
dt.fit(X, y)
     
import dtreeviz

viz = dtreeviz.model(dt, X, y,
                     target_name="play_tennis",
                     feature_names=X.columns,
                     class_names=["No", "Yes"])
viz.view(fontname="monospace", scale=2.0)
