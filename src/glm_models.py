import statsmodels.api as sm

def fit_frequency_glm(X, y, exposure):
    X = sm.add_constant(X)
    model = sm.GLM(
        y,
        X,
        family=sm.families.Poisson(),
        offset=np.log(exposure)
    )
    return model.fit()


def fit_severity_glm(X, y):
    X = sm.add_constant(X)
    model = sm.GLM(
        y,
        X,
        family=sm.families.Gamma(link=sm.families.links.Log())
    )
    return model.fit()
